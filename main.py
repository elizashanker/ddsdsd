from flask import Flask, render_template

app = Flask(__name__)

menu = ["Установка", "Первое положение", "Обратная связь"]


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", title="Про Flack", menu=menu)


@app.route("/about")
def about():
    return render_template(about.html, title="О сайте", menu=menu)
