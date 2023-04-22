#!/usr/bin/python3
"""
Script that starts a Flask web application:
returns even or odd
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """ Display text """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """ Display text """
    return 'HBNB'


@app.route('/c/<text>')
def display_ctext(text):
    """ Display C text """
    return "C {}".format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """ Display Python text with a default of 'is cool' """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def n_int(n):
    """ Display n only if it's an int """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_if_int(n):
    """ Display html page only if n is int """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    """ Display html page only if n is int """
    if n % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    return render_template('6-number_odd_or_even.html', n=n, even_odd=even_odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
