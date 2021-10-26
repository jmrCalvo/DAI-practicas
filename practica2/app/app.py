# ./app/app.py

import json
import re
from flask import Flask, flash, render_template, make_response, Markup, request, redirect, url_for
from utils.credential import login, signup, get_token, set_token
from exercises import burbuja_sort, insercion_sort, seleccion_sort, criba_eratostenes, fib, check_bracket, check_email_card_style, generatCircle, generateRectangle
from utils.visited_url import generate_stack, append_to_stack, get_stack
from random import randrange

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
random_number = randrange(100)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    # POST
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        correct = login(email, password)
        if not correct:
            flash('It was not possible to login', 'error')
        else:
            resp = make_response(redirect('/'))
            resp.set_cookie('user', set_token(email, password))
            flash('Welcome to Coala', 'success')
            return resp
    # GET
    token = request.cookies.get('user')
    if token != None:
        current_user = get_token(token)
        is_correct_login = login(
            current_user['email'], current_user['password'])
        if (is_correct_login):
            return redirect('/')
    return render_template('login.html'), 404


@app.route("/signup", methods=['GET', 'POST'])
def signup_page():
    # POST
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        correct = signup(email, password, repeat_password)
        if not correct:
            flash('It was not possible to sign up', 'error')
        else:
            generate_stack(email)
            resp = make_response(redirect('/'))
            resp.set_cookie('user', set_token(email, password))
            flash('Welcome to Coala', 'success')
            return resp
    # GET
    token = request.cookies.get('user')
    if token != None:
        current_user = get_token(token)
        is_correct_login = login(
            current_user['email'], current_user['password'])
        if (is_correct_login):
            return redirect('/')
    return render_template('signup.html'), 404


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/", methods=["GET"])
def main():
    user = request.cookies.get('user')
    # append_to_stack(request, '/')
    if user == None:
        return redirect('/login')

    res = json.loads(user)
    is_correct_login = login(res['email'], res['password'])
    if is_correct_login:
        last_url_arr = get_stack(request)
        return render_template("index.html", last_urls=last_url_arr)

    return redirect('/login')


@app.route("/logout", methods=["GET"])
def logout():
    resp = make_response(redirect('/login'))
    resp.delete_cookie('user')
    return resp


# The exercises routes

@app.route('/ordena/<path>')
def sort(path):
    append_to_stack(request, '/ordena/'+path)
    string_check_special = re.compile('[@_!#$%^&*()[]<>?/\|}{~:]')
    string_check_letters = re.compile('[A-Za-z]')
    if(string_check_special.search(path) != None or string_check_letters.search(path) != None):
        return 'Characters not correct'
    # else is only numbers and comma
    arr = path.split(',')
    arr_int = [int(numeric_string) for numeric_string in arr]

    burbuja_sorted = burbuja_sort(arr_int)
    arr_sorted_burbuja = ', '.join(
        [str(numeric_string) for numeric_string in burbuja_sorted[0]])
    time_burbuja_sort = burbuja_sorted[1]

    seleccion_sorted = seleccion_sort(arr_int)
    arr_sorted_seleccion = ', '.join(
        [str(numeric_string) for numeric_string in seleccion_sorted[0]])
    time_seleccion_sort = burbuja_sorted[1]

    inserccion_sorted = insercion_sort(arr_int)
    arr_sorted_inserccion = ', '.join(
        [str(numeric_string) for numeric_string in inserccion_sorted[0]])
    time_inserccion_sort = inserccion_sorted[1]

    return f'<p>Burbuja:  { arr_sorted_burbuja }, time: {time_burbuja_sort}</p> <p> Seleccion: {arr_sorted_seleccion}, time: {time_seleccion_sort}</p><p> inserccion: {arr_sorted_inserccion}, time:{time_inserccion_sort}</p>'


@ app.route('/criba/<number>')
def criba(number):
    append_to_stack(request, '/criba/'+number)
    string_check_special = re.compile('^[0-9]*$')
    if(string_check_special.search(number) == None):
        return 'not correct input'
    if(int(number) == 0):
        return '0'
    eratostenes = criba_eratostenes(int(number))
    return f'{eratostenes}'


@ app.route('/fibonacci/<number>')
def fibonacci(number):
    append_to_stack(request, '/fibonacci/'+number)
    string_check_number = re.compile('^[0-9]*$')
    if(string_check_number.search(number) == None):
        return 'not correct input'
    if(int(number) == 0):
        return '0'
    fibonacci = fib(int(number))
    return f'{fibonacci}'


@ app.route('/brackets/<brackets>')
def bracket(brackets):
    append_to_stack(request, '/brackets/'+brackets)
    string_check_letters = re.compile('[A-Za-z]')
    string_check_numbers = re.compile('[0-9]')
    string_check_special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(string_check_special.search(brackets) != None or string_check_numbers.search(brackets) != None or string_check_letters.search(brackets) != None):
        return 'not correct input'
    checked = check_bracket(brackets)
    return f'{checked}'


@ app.route('/identify/<str_to_check>')
def identify(str_to_check):
    append_to_stack(request, '/identify/'+str_to_check)
    checked = check_email_card_style(str_to_check)
    return f'{checked}'


@ app.route("/svg", methods=["GET"])
def svg():
    append_to_stack(request, '/svg')
    svg_data = "<div>"
    number_rectangle = randrange(20)
    for i in range(number_rectangle):
        svg_data = svg_data + generateRectangle()

    number_circle = randrange(20)
    for i in range(number_circle):
        svg_data = svg_data + generatCircle()

    svg_data = svg_data + '</div>'
    return render_template("svg.html", svg=Markup(svg_data))


@ app.route("/guess", methods=['GET', 'POST'])
def guess():
    if request.method == 'POST':
        global random_number
        number = int(request.form['number'])
        if number == random_number:
            random_number = randrange(100)
            flash('The number is correct', 'suscces')
        elif number < random_number:
            flash('The number is less', 'error')
        else:
            flash('The number is great', 'error')
    append_to_stack(request, '/guess')
    return render_template("guess.html")
