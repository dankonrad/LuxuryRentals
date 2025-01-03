from config import app, db, render_template, jsonify, send_file, url_for
from auth import auth
from views import views
from models import Veiculos
from io import BytesIO



app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(views)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 
