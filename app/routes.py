from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/ecommerce")
def ecommerce():
    return render_template("ecommerce.html")

@main.route("/entertainment")
def entertainment():
    return render_template("entertainment.html")

@main.route("/ip")
def ip():
    return render_template("ip.html")

@main.route("/cases")
def cases():
    return render_template("cases.html")

@main.route("/team")
def team():
    return render_template("team.html")