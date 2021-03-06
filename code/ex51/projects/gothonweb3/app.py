from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
    name = request.args.get('name', '名もない人')
    greeting = f"ハロー、{name}"
    return render_template("index.html", greeting=greeting)
