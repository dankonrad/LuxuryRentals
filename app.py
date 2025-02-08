from config import app, db, LoginManager
from auth import auth
from views import views
from user import usuario
from models import Cliente



app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(usuario)
app.register_blueprint(views)


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Cliente.query.get(user_id)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 
