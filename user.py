from config import Blueprint, render_template, request, db, redirect, url_for, login_required, current_user, flash
from models import Veiculos, Reservas
from views import diferenca, preco_total
from datetime import datetime


usuario = Blueprint("usuario", __name__)


# Route para ver as reservas feitas pelo usuário

@usuario.route('/reservas')
@login_required 
def minhas_reservas():

    # "user" verifica se o usuário está logado     

    user = current_user.is_authenticated

    # reserva_data possui os dados da reserva e do veículo

    reserva_data = (
    db.session.query(Reservas, Veiculos)
    .join(Veiculos, Reservas.veiculo_id == Veiculos.id)
    .filter(Reservas.cliente_id == current_user.id)
    .all()
    )   


    return render_template('reservas.html', reserva_data=reserva_data, diferenca=diferenca, preco_total=preco_total, user=user)


# Route para atualizar a data da reserva

@usuario.route('/update_reservation/<int:reserva_id>', methods=['POST'])
@login_required
def update_reservation(reserva_id):
    reserva = Reservas.query.get_or_404(reserva_id)

    if reserva.cliente_id != current_user.id:
        flash("Você não tem permissão para modificar esta reserva!", "danger")
        return redirect(url_for('minhas_reservas'))


    nova_data_inicio = request.form.get("data_de_inicio")
    nova_data_fim = request.form.get("data_de_fim")

    try:
        nova_data_inicio = datetime.strptime(nova_data_inicio, '%Y-%m-%d').date()
        nova_data_fim = datetime.strptime(nova_data_fim, '%Y-%m-%d').date()
    except ValueError:
        flash("Formato de data inválido!", "danger")
        return redirect(url_for('minhas_reservas'))

    if nova_data_inicio >= nova_data_fim:
        flash("A data de fim deve ser depois da data de início!", "warning")
        return redirect(url_for('minhas_reservas'))

    reserva.data_de_inicio = nova_data_inicio
    reserva.data_de_fim = nova_data_fim
    db.session.commit()

    flash("Reserva atualizada com sucesso!", "success")
    return redirect(url_for('minhas_reservas'))




# Route para cancelar a reserva

@usuario.route('/cancel_reservation/<int:reserva_id>', methods=['GET'])
@login_required
def cancel_reservation(reserva_id):

    reserva = Reservas.query.get_or_404(reserva_id)

    if reserva.cliente_id != current_user.id:
        flash("Você não tem permissão para cancelar esta reserva!", "danger")
        return redirect(url_for('minhas_reservas'))

    db.session.delete(reserva)
    db.session.commit()

    flash("Reserva cancelada com sucesso!", "success")
    return redirect(url_for('minhas_reservas'))
