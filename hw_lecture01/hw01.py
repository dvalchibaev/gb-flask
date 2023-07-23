from flask import Flask, render_template
from datetime import date


app = Flask(__name__)
HTML = "base.html"


@app.route('/')
@app.route('/home/')
def home():
    context = {'title': 'Главная',}
    return render_template(HTML, **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('static/clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('static/shoes.html', **context)


if __name__ == '__main__':
    app.run()
