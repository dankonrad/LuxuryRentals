from config import Blueprint, login_user, login_required, logout_user, current_user, db, request, check_password_hash,generate_password_hash, flash, render_template, redirect, url_for
from models import Cliente


# Está página servirá para tratar de tudo que diz respeito a autentificação
auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["POST", "GET"])
def signup():

    if request.method == "POST":

        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
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
            newUser = Cliente(
                first_name=first_name, last_name=last_name, user=username, email=email, password=generate_password_hash(pword1, method="pbkdf2:sha256"))
            
            db.session.add(newUser)
            db.session.commit()

            login_user(newUser, remember=True)


            return redirect(url_for("views.index"))
    return render_template("signup.html")
    

@auth.route("/login", methods= ["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cliente = Cliente.query.filter_by(email=email).first()

        if cliente:
            if check_password_hash(cliente.password, password):
                flash("Bem vindo, " + cliente.user)
                login_user(cliente, remember=True)
                return redirect(url_for("views.index"))
            else:
                flash("A palavra-passe está incorreta.")
        else: 
            flash("Não existe uma conta com este correio eletrónico.")
            
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.index"))