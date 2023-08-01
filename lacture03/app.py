from flask import Flask, render_template, request, redirect, make_response
from lacture03.models import db, User
from werkzeug.security import generate_password_hash


"""
Создать форму для регистрации пользователей на сайте. 
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/mydatabase.db'
db.init_app(app)


# Сколько не боролся, так и не получилось сделать запуск через wsgi,
# чтобы можно было вносить изменения в браузере.
# Если делаю настройку 'sqlite:///../../instance/mydatabase.db',
# то все равно создается директория  ../lecture03/instance и новые элементы
# в базу данных не добавляются
# @app.cli.command('init-db')
# def innit_db():
#     db.create_all()


@app.route('/init_db/')
def innit_db():
    db.create_all()
    response = make_response(redirect('/'))
    return response


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first name']
        last_name = request.form['last name']
        user_email = request.form['email']
        user_pwd = request.form['password']
        user_pwd_hash = generate_password_hash(user_pwd)
        user = User(first_name=first_name, last_name=last_name,
                    user_email=user_email, user_pwd_hash=user_pwd_hash)
        db.session.add(user)
        db.session.commit()
        response = make_response(redirect('/signup_success/'))
        return response
    return render_template('login.html')


@app.route('/signup_success/', methods=['GET', 'POST'])
def signup_success():
    if request.method == 'POST':
        response = make_response(redirect('/'))
        return response
    return render_template('signup_success.html')


if __name__ == '__main__':
    app.run(debug=True)
