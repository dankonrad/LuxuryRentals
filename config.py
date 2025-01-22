from flask import Flask, send_file, jsonify, render_template, request, redirect, url_for, flash, Blueprint, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///luxuryrentals.db"

app.config["SECRET_KEY"] = "asidufsjakdbslankdcdsfc"

db = SQLAlchemy(app)


