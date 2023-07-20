from flask import Flask
from flask import render_template
from datetime import date


app = Flask(__name__)
HTML = "html_template.html"


@app.route('/')
@app.route('/home/')
def home():
    context = {'title': 'Главная',}
    return render_template(HTML, **context)


@app.route('/news/')
def news():
    context = {'title': 'Задание 7',
               'text': 'Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.\n'
               'Каждый блок должен содержать заголовок новости, краткое описание и дату публикации. \n'
               'Данные о новостях должны быть переданы в шаблон через контекст.',
               'news': [
                   {'title': 'Title 1',
                    'text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis, culpa.',
                    'date': date('12.04.2000'),},
                   {'title': 'Title 2',
                    'text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis, culpa.',
                    'date': date('19.05.2001'), },
                   {'title': 'Title 3',
                    'text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis, culpa.',
                    'date': date('23.11.2002'), },
               ]
               }
    return render_template('static/news.html', **context)


if __name__ == '__main__':
    app.run()
