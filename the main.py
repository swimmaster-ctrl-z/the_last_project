from flask import Flask, render_template, redirect, url_for, request
#from flask_sqlalchemy import SQLAlchemy

#from data import db_session
#from data.users import User


app = Flask(__name__)

#app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#db = SQLAlchemy(app)


@app.route('/', methods=["GET"])
def hello_world():
    return render_template('main_page.html')



if __name__ == '__main__':
    #db_session.global_init("db/blogs.db")
    app.run(port=8070, host='127.0.0.1', debug=True)