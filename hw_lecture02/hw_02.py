from flask import Flask, render_template, request, redirect, url_for, session, make_response


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        response = make_response()
        response.set_cookie(user_name, user_email)

    return render_template('login.html')


@app.route('/welcome/')
def welcome():
    
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(debug=True)
