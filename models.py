from config import db
from flask_login import UserMixin
from datetime import date


class Cliente(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    user = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    reservas = db.relationship("Reservas")



class Veiculos(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    marca = db.Column(db.String(150))
    modelo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    tipo_de_veiculo = db.Column(db.String(150))
    numero_de_portas = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    numero_de_assentos = db.Column(db.Integer)
    tipo_de_cambio = db.Column(db.String(150))
    velocidade_maxima = db.Column(db.Integer)
    imagem_do_veiculo = db.Column(db.LargeBinary)
    preco = db.Column(db.Float)
    desc_rapida = db.Column(db.String(1000))
    desc_detatalhada = db.Column(db.String(1000))
    data_de_inspecao = db.Column(db.Date, nullable=False)
    data_de_revisao = db.Column(db.Date, nullable=False)
    reservas = db.relationship("Reservas")

    def esta_disponivel(self, inicio, fim):  

        # A data de hoje
        hoje = date.today()
        # A data de hoje - 1 ano para fazer o calculo da ultima revisão
        um_ano_atras = hoje.replace(year = hoje.year - 1)
        # Caso a data da utima inspeção for maior do que a 1 ano atrás siginifica que o veículo está disponível

        if not self.data_de_inspecao > um_ano_atras or self.data_de_revisao < hoje:
            return False
        
        for reserva in self.reservas:
            # If there is an overlap between reservation dates, it's not available
            if not (reserva.data_de_fim < inicio or reserva.data_de_inicio > fim):
                return False
    

        return True
    

 
class Reservas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_de_inicio = db.Column(db.Date, nullable=False)
    data_de_fim = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    distrito = db.Column(db.String(150))
    codigo_postal = db.Column(db.String(150))
    nome_do_cartao = db.Column(db.String(50))
    numero_do_cartao = db.Column(db.String(50))
    data_de_validade = db.Column(db.String(50))
    cvv = db.Column(db.String(50))
    metodo_de_pagamento_id = db.Column(db.String(50), db.ForeignKey("pagamento.id"))
    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculos.id"))
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))



class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    forma_de_pagamento = db.Column(db.String(50))
    reservas = db.relationship("Reservas")