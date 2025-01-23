from config import Blueprint, send_file, jsonify, render_template, request, db, redirect, url_for, login_required, session, current_user, flash
from models import Veiculos, Reservas, Pagamento
from io import BytesIO
from datetime import datetime, date, timedelta


user = Blueprint("user", __name__)


@user.route('/reservas', methods=["GET"])
@login_required
def user_page():

    user = current_user.is_authenticated

    current_user_reservas = Reservas.query.filter_by(cliente_id=current_user.id).all()

    print(current_user.reservas)

    for things in current_user.reservas:
        print(things.data_de_inicio)

    return render_template('reservas.html', user=user)