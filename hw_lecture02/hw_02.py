from flask import Flask, render_template, request, redirect, url_for, session, make_response
from secrets import token_hex


app = Flask(__name__)
app.secret_key = token_hex()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.cookies.get('user_name'):
        response = make_response(redirect('/welcome/'))
        return response
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        response = make_response(redirect('/welcome/'))
        response.set_cookie('user_name', user_name)
        response.set_cookie('user_email', user_email)
        return response
    return render_template('login.html')


@app.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    if user_name := request.cookies.get('user_name'):
        return render_template('welcome.html', name=user_name)
    return redirect('/')


@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
