from flask import Flask, request, render_template, redirect, url_for, flash, session,jsonify
from models import TrendsTitle, db
from flask_migrate import Migrate
import json

from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:hassan1998@localhost/trends"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        pass
    else:
        return render_template("sign_in.html")


@app.route("/view_data")
def view_data():
    data = TrendsTitle.query.order_by(TrendsTitle.counters.desc()).all()
    titles = [i.title for i in data]
    counts = [i.counters for i in data]
    print(titles)
    print(counts)

    return render_template(
        "view_data.html",
        data=data,
        counts=json.dumps(counts[:10]),
        titles=json.dumps(titles[:10]),
    )


@app.route("/redirect/<int:id>")
def redirect(id):
    print(id)
    data = TrendsTitle.query.get_or_404(id)
    return redirect(data.link)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        return "validation"
    else:
        return render_template("signup.html")


@app.route("/updateChart")
def updateChart():
    data = TrendsTitle.query.order_by(TrendsTitle.counters.desc()).all()
    titles = [i.title for i in data][:5]
    counts = [i.counters for i in data][:5]
    return {'title': titles, 'counts': counts}
