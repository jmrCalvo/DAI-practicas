# ./app/app.py

import re
from flask import Flask, render_template, Markup
from exercises import burbuja_sort, insercion_sort, seleccion_sort, criba_eratostenes, fib, check_bracket, check_email_card_style
from random import randrange

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/simpson')
def static_file():
    return app.send_static_file('index.html')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/ordena/<path>')
def sort(path):
    string_check_special = re.compile('[@_!#$%^&*()[]<>?/\|}{~:]')
    string_check_letters = re.compile('[A-Za-z]')
    if(string_check_special.search(path) != None or string_check_letters.search(path) != None):
        return 'Characters not correct'
    # else is only numbers and comma
    arr = path.split(',')
    burbuja_sorted = burbuja_sort(arr)
    arr_sorted_burbuja = ', '.join(burbuja_sorted[0])
    time_burbuja_sort = burbuja_sorted[1]

    seleccion_sorted = seleccion_sort(arr)
    arr_sorted_seleccion = ', '.join(seleccion_sorted[0])
    time_seleccion_sort = burbuja_sorted[1]

    inserccion_sorted = insercion_sort(arr)
    arr_sorted_inserccion = ', '.join(inserccion_sorted[0])
    time_inserccion_sort = inserccion_sorted[1]

    return f'<p>Burbuja:  { arr_sorted_burbuja }, time: {time_burbuja_sort}</p> <p> Seleccion: {arr_sorted_seleccion}, time: {time_seleccion_sort}</p><p> inserccion: {arr_sorted_inserccion}, time:{time_inserccion_sort}</p>'


@app.route('/criba/<number>')
def criba(number):
    string_check_special = re.compile('^[0-9]*$')
    if(string_check_special.search(number) == None):
        return 'not correct input'
    if(int(number) == 0):
        return '0'
    eratostenes = criba_eratostenes(int(number))
    return f'{eratostenes}'


@app.route('/fibonacci/<number>')
def fibonacci(number):
    string_check_number = re.compile('^[0-9]*$')
    if(string_check_number.search(number) == None):
        return 'not correct input'
    if(int(number) == 0):
        return '0'
    fibonacci = fib(int(number))
    return f'{fibonacci}'


@app.route('/brackets/<brackets>')
def bracket(brackets):
    string_check_letters = re.compile('[A-Za-z]')
    string_check_numbers = re.compile('[0-9]')
    string_check_special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(string_check_special.search(brackets) != None or string_check_numbers.search(brackets) != None or string_check_letters.search(brackets) != None):
        return 'not correct input'
    checked = check_bracket(brackets)
    return f'{checked}'


@app.route('/identify/<str_to_check>')
def identify(str_to_check):
    checked = check_email_card_style(str_to_check)
    return f'{checked}'


def generateRectangle():
    background_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    border_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    positionX = str(randrange(360))
    positionY = str(randrange(360))
    positionZ = str(randrange(360))
    height = str(randrange(500))
    width = str(randrange(500))
    svg_data = f'<svg transform="rotate({positionX} {positionY},{positionZ})" width=\"{height}\" height=\"{width}\"><rect width=\"{height}\" height=\"{width}\" style=\"fill:rgb({background_colors});stroke-width:5;stroke:rgb({border_colors})\" /></svg>'
    return svg_data


def generatCircle():
    background_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    border_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    height = str(randrange(500))
    width = str(randrange(500))
    cx = str(randrange(200))
    cy = str(randrange(200))
    rx = str(randrange(200))
    ry = str(randrange(200))
    svg_data = f'<svg height = "{height}" width = "{width}" ><ellipse cx = "{cx}" cy = "{cy}" rx = "{rx}" ry = "{ry}" style = "fill:rgb({background_colors});stroke:rgb({border_colors});stroke-width:2" /></svg>'
    return svg_data


@app.route("/svg", methods=["GET"])
def svg():
    svg_data = "<div>"
    number_rectangle = randrange(20)
    for i in range(number_rectangle):
        svg_data = svg_data + generateRectangle()

    number_circle = randrange(20)
    for i in range(number_circle):
        svg_data = svg_data + generatCircle()

    svg_data = svg_data + '</div>'
    return render_template("svg.html", svg=Markup(svg_data))
