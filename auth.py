from config import Blueprint, db, request, check_password_hash,generate_password_hash, flash, render_template, redirect, url_for
from models import User


# Está página servirá para tratar de tudo que diz respeito a autentificação
auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["POST", "GET"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        pword1 = request.form["pass1"]
        pword2 = request.form["pass2"]


        if len(username) < 4:
            flash("O nome de usuário deverá possuir pelo menos 4 caracteres.")
        elif len(email) < 5:
            flash("O correio eletrónico deverá ter pelo menos 5 caracteres.")
        elif len(pword1) < 8:
            flash("A palavra-passe deverá conter pelo menos 8 caracteres.")
        elif pword1 != pword2:
            flash("As palavras-passes não são iguais.")
        else:
            newUser = User(user=username, email=email, password=generate_password_hash(pword1, method="pbkdf2:sha256"))

            db.session.add(newUser)
            db.session.commit()

            return redirect(url_for("index"))
    return render_template("signup.html")
    

@auth.route("/login", methods= ["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password == password):
                flash("Bem vindo, " + user.user)
                return redirect(url_for("index"))
            else:
                flash("A palavra-passe está incorreta.")
        else: 
            flash("Não existe uma conta com este correio eletrónico.")
            
    return render_template("login.html")