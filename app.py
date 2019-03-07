from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from flask.helpers import make_response
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('mysql+pymysql://root:''@localhost/test', echo=True)

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')

    else:
        session['edit'] = False
        Session = sessionmaker(bind=engine)
        s = Session()

        user_dic = s.query(User).get(session['user_id']).to_dict()
        return render_template('welcome.html', user_info=user_dic)


@app.route('/welcome', methods=['POST'])
def do_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()

    if result:
        session['logged_in'] = True
        session['user_id'] = result.id
        user_dic = s.query(User).get(session['user_id']).to_dict()
        if user_dic['admin']:
            session['admin'] = True
        else: session['admin'] = False

        return render_template('welcome.html', user_info=user_dic, userid=result.id)

    else:
        flash('wrong password!')
    return home()


@app.route("/edit_user", methods=['POST'])
def edit_profile():

    Session = sessionmaker(bind=engine)
    s = Session()

    user = s.query(User).filter_by(id=session['user_id']).first()

    user.firstname = str(request.form['firstname'])
    user.lastname = str(request.form['lastname'])
    user.email = str(request.form['email'])
    user.username = str(request.form['username'])
    user.password = str(request.form['password'])
    user.firstlogin = False

    s.commit()

    user_dic = s.query(User).get(session['user_id']).to_dict()
    return render_template('welcome.html', user_info=user_dic, userid=session['user_id'], edited=True)


@app.route("/admin_panel", methods=['POST'])
def admin_panel():
    Session = sessionmaker(bind=engine)
    s = Session()
    users = s.query(User).all()
    return render_template('admin_panel.html', users=users)


@app.route("/admin_edit", methods=['POST'])
def admin_edit():

    userid = int(request.form['users'])
    Session = sessionmaker(bind=engine)
    s = Session()
    user_dic = s.query(User).filter(User.id.in_([userid])).first().to_dict()
    session['edit'] = True
    return render_template('welcome.html', user_info=user_dic, userid=userid)


@app.route("/admin_successful_edited", methods=['POST'])
def successful_edited():
    session['edit'] = False
    Session = sessionmaker(bind=engine)
    s = Session()

    user = s.query(User).filter_by(id=int(request.form['id'])).first()

    user.firstname = str(request.form['firstname'])
    user.lastname = str(request.form['lastname'])
    user.email = str(request.form['email'])
    user.username = str(request.form['username'])
    user.password = str(request.form['password'])
    user.admin = 'admin' in request.form
    user.firstlogin = False

    s.commit()
    users = s.query(User).all()
    return render_template('admin_panel.html', users=users, msg=user.username+" Edited Successfully!")

@app.route("/register", methods=['POST'])
def register():
    return render_template('register.html')

@app.route("/add_user", methods=['POST'])
def add_user():
    Session = sessionmaker(bind=engine)
    s = Session()

    admin = 'admin' in request.form
    user = User(str(request.form['firstname']), str(request.form['lastname']),
                str(request.form['email']), str(request.form['username']), str(request.form['password']),
                admin)
    s.add(user)
    s.commit()

    s.commit()
    users = s.query(User).all()

    return render_template('admin_panel.html', msg=user.username+" Added Successfully!", users=users)

@app.route("/logout")
def logout():
    session['logged_in'] = False

    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)