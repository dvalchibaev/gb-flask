from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


"""
Создать форму для регистрации пользователей на сайте. 
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". 
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_pwd_hash = db.Column(db.String(128), nullable=False)

    # def __init__(self, id, first_name, last_name, email, pwd_hashed):
    #     self.id, self.first_name, self.last_name, self.email = id, first_name, last_name, email
    #     self.user_pwd_hash = pwd_hashed


if __name__ == '__main__':
    db.create_all()
