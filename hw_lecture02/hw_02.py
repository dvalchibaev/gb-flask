from flask import Flask, render_template, request, session


app = Flask(__name__)
HTML = "base.html"


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']

    return render_template(HTML)


@app.route('/loged/')
def login():

    return render_template(HTML)


if __name__ == '__main__':
    app.run()
