from config import Blueprint, send_file, jsonify, render_template, request, db, redirect, url_for, login_required, session, current_user, flash
from models import Veiculos, Reservas, Pagamento
from io import BytesIO
from datetime import datetime, date, timedelta


user = Blueprint("user", __name__)


@user.route('/reservas', methods=["GET"])
@login_required
def user_page():



    reserva = current_user.reservas

    veiculo = Veiculos.query.filter_by(id=reserva.veiculo_id)

    for reserva in current_user.reservas:
        for veiculo in Veiculos.query.filter_by(id=reserva.veiculo_id):
            print(veiculo.marca)
    

    return render_template('reservas.html', 
                           reserva=reserva)