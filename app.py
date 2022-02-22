from flask import Flask, request, render_template
from models import TrendsTitle, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '"mysql+pymysql://root:password@localhost/trends'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        pass
    else:
        return render_template('sign_in.html')


@app.route('/view_data')
def view_data():
    data = TrendsTitle.query.all()
    titles = [i.title for i in data]
    print(titles)
    return render_template('view_data.html', data=data, titles=titles[::5])
