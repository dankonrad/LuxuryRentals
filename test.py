# import random
# from datetime import datetime, timedelta
from config import db, app
from datetime import date, datetime
from models import Veiculos, Reservas, Pagamento
# # Lista de modelos de veículos
# vehicle_models = [
#     "F-Pace"
# ]

# # Função para gerar uma data aleatória
# def generate_random_date():
#     today = datetime.now()
#     random_days = random.randint(-365, 365)  # Gera um intervalo de datas aleatórias dentro de +/- 1 ano
#     return (today + timedelta(days=random_days)).strftime('%Y-%m-%d')

# # Gerar o dicionário com as inspeções obrigatórias
# vehicle_inspections = {}
# vehicles_unpaid_inspection = random.sample(vehicle_models, int(len(vehicle_models) * 0.15))  # 15% sem inspeção paga

# for model in vehicle_models:
#     if model not in vehicles_unpaid_inspection:
#         inspection_date = generate_random_date()
#         vehicle_inspections[model] = inspection_date

# # Exibindo o dicionário gerado
# print(vehicle_inspections)

# today = datetime.now()
# um_ano_atras = today.replace(year = today.year - 1)
# data = datetime.strptime("2024-11-01", "%Y-%m-%d")

# if data > um_ano_atras:
#     print("Yes")

# print(um_ano_atras, data)
with app.app_context():

    def dispon(inicio, fim):
        for veiculo in Veiculos.query.all():
            if veiculo.reservas:
                for reserva in veiculo.reservas:
                    if inicio >= reserva.data_de_inicio and fim <= reserva.data_de_fim:
                        print("Não está disponível!")
                    else:
                        print("Está disponível")
    

def diferenca(inicio, fim):

    data_de_inicio = datetime.strptime(inicio, '%Y-%m-%d').date()
    data_de_fim = datetime.strptime(fim, '%Y-%m-%d').date()

    diferenca = data_de_fim - data_de_inicio
    
    print(diferenca)