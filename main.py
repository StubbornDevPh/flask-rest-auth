from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'pogisibrotherspartacus'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/haxxor/Desktop/Projects/flask/restfulapi/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



if __name__ == '__main__':
    app.run(debug=True)