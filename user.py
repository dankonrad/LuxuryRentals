from config import Blueprint, send_file, jsonify, render_template, request, db, redirect, url_for, login_required, session, current_user, flash
from models import Veiculos, Reservas, Pagamento
from views import diferenca, preco_total
from datetime import datetime, date, timedelta


user = Blueprint("user", __name__)



@user.route('/reservas')
@login_required  # Ensure only logged-in users can access this page
def minhas_reservas():
    # Retrieve reservations for the current user, joining with the Veiculos table

    reserva_data = (
    db.session.query(Reservas, Veiculos)
    .join(Veiculos, Reservas.veiculo_id == Veiculos.id)
    .filter(Reservas.cliente_id == current_user.id)
    .all()
    )   

     

    return render_template('reservas.html', reserva_data=reserva_data, diferenca=diferenca, preco_total=preco_total)

