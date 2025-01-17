from config import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    

 
class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    formade = db.Column(db.Integer)
    reservas = db.relationship("Reservas")



class Reservas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_inicio = db.Column(db.DateTime(timezone=True), default=func.now())
    data_fim = db.Column(db.DateTime(timezone=True), default=func.now())
    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculos.id"))
    cliente_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    pagamento_id = db.Column(db.Integer, db.ForeignKey("pagamento.id"))

