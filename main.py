from flask import Flask, render_template
from utils import *


app = Flask(__name__, template_folder='templates')

@app.route("/movie/<title>")
def title_page(title):
    result = title_search(title)
    page = render_template("title_search.html", result=result)
    return page

@app.route("/movie/<int:year_from>/to/<int:year_to>/")
def range_page(year_from, year_to):
    page = render_template("range_search.html", result=range_search(year_from, year_to))
    return page

@app.route("/rating/<rate>/")
def rating_page(rate):
    result = rating_search(rate)
    page=render_template("rating_search.html", result=result)
    return page

@app.route("/genre/<genre>")
def genre_page(genre):
    result = genre_search(genre)
    page = render_template("genre_search.html", result=result)
    return page

app.run()