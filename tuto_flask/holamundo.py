import flask
import mysql.connector
from mysql.connector import cursor

app = flask.Flask(__name__)

midb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="testing",
    password="12345",
    database="Employees",
)

cursor = midb.cursor()


@app.route("/")
def index():
    return "hola mundo"


# HTTPS methods, GET POST PUT DELETE PATCH
# GET is used to list or show something
# POST when you want to create
# PUT to update, or replace a resource, and PATCH to parcially update a resource
@app.route("/post/<post_id>", methods=["GET", "POST"])
def lala(post_id):
    if flask.request.method == "GET":
        return "El id del post es: " + post_id  # http://127.0.0.1:5000/post/1
    else:
        return "Este es otro metodo y no GET"


@app.route("/lele", methods=["GET", "POST"])
def lele():
    cursor.execute('SELECT * FROM Employees')
    usuarios = cursor.fetchall()
    return flask.render_template('lele.html', usuarios=usuarios)


@app.route("/home", methods=["GET"])
def home():
    return flask.render_template("home.html", mensaje="Hola Mundo")
