from flask import Flask, send_file, jsonify, render_template, request, redirect, url_for, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///luxuryrentals.db"

app.config["SECRET_KEY"] = "asidufsjakdbslankdcdsfc"

db = SQLAlchemy(app)


