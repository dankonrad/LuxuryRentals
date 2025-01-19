from config import Blueprint, send_file, jsonify, render_template, request, db, redirect, url_for, login_required
from models import Veiculos, Reservas, Pagamento
from io import BytesIO
from datetime import datetime, date, timedelta


views = Blueprint("views", __name__)






@views.route("/vehicle_image/<int:vehicle_id>")
def get_vehicle_image(vehicle_id):
     
     veiculo = Veiculos.query.get_or_404(vehicle_id)

     if veiculo.imagem_do_veiculo:
          return send_file(BytesIO(veiculo.imagem_do_veiculo), mimetype="image/png")
     else:
          return jsonify({"message" : "File wasn't found."})
     


@views.route('/', methods=["GET"])
def index():

     vehicles = Veiculos.query.all()

     today = date.today()

     tomorrow = today + timedelta(days=1)


     print(len(vehicles))

     available_vehicles = [vehicle for vehicle in vehicles if vehicle.esta_disponivel(today, tomorrow)]

     print(len(available_vehicles))

     return render_template('index.html', vehicles=available_vehicles, today=today, tomorrow=tomorrow)


@views.route('/filter', methods=['GET'])
def filter_vehicles():

     query = Veiculos.query

     search_marca = request.args.get("search_marca", "")

     search_modelo = request.args.get("search_modelo", "")

     num_pessoas = request.args.get("num_pessoas", type=int)

     tipo_de_veiculo = request.args.get("tipo_de_veiculo")

     preco_do_veiculo = request.args.get("preco_do_veiculo")

     ordem_prod = request.args.get("ordem_prod", "price_asc")
     
     data_de_inicio_str = request.args.get("data_de_inicio")

     data_de_fim_str = request.args.get("data_de_fim")

 
     if search_marca:
          query = query.filter(Veiculos.marca.ilike(f"%{search_marca}%"))
     
     if search_modelo:
          query = query.filter(Veiculos.modelo.ilike(f"%{search_modelo}%"))

     if num_pessoas:
          query = query.filter(Veiculos.numero_de_assentos >= num_pessoas )

     if tipo_de_veiculo:
          query = query.filter(Veiculos.tipo_de_veiculo == tipo_de_veiculo)

     if preco_do_veiculo:
          preco_min, preco_max = map(int, preco_do_veiculo.split("-"))
          query = query.filter(Veiculos.preco >= preco_min, Veiculos.preco <= preco_max)

     
     if data_de_inicio_str and data_de_fim_str:
        try:
            data_de_inicio = date.fromisoformat(data_de_inicio_str)
            data_de_fim = date.fromisoformat(data_de_fim_str)
        except ValueError:
            data_de_inicio = None
            data_de_fim = None
     else:
        data_de_inicio = None
        data_de_fim = None



     if ordem_prod == "preco_asc":
          query = query.order_by(Veiculos.preco.asc())
     elif ordem_prod == "preco_desc":
          query = query.order_by(Veiculos.preco.desc())
     elif ordem_prod == "nome_asc":
          query = query.order_by(Veiculos.marca.asc())
     elif ordem_prod == "nome_desc":
          query = query.order_by(Veiculos.marca.desc())
     elif ordem_prod == "ano_asc":
          query = query.order_by(Veiculos.ano.asc())
     elif ordem_prod == "ano_desc":
          query = query.order_by(Veiculos.ano.desc())
     elif ordem_prod == "velo_asc":
          query = query.order_by(Veiculos.velocidade_maxima.asc())
     elif ordem_prod == "velo_desc":
          query = query.order_by(Veiculos.velocidade_maxima.desc())
         


     vehicles = query.all()

     # Condição para veículos disponíveis

     available_vehicles = []
     for vehicle in vehicles:
        if data_de_inicio and data_de_fim:
            # Check availability for the given date range
            if vehicle.esta_disponivel(data_de_inicio, data_de_fim):
                available_vehicles.append(vehicle)
        else:
            # If no dates are provided, assume the vehicle is available
            available_vehicles.append(vehicle)



     return render_template('index.html', 
                            vehicles=available_vehicles,
                            search_marca = search_marca,
                            search_modelo=search_modelo,
                            num_pessoas=num_pessoas,
                            tipo_de_veiculo= tipo_de_veiculo,
                            preco_do_veiculo=preco_do_veiculo,
                            ordem_prod=ordem_prod,
                            data_de_inicio=data_de_inicio,
                            data_de_fim=data_de_fim)






@views.route("/vehicle_information/<int:vehicle_id>", methods=["GET", "POST"])
def get_vehicle(vehicle_id):

     vehicle = Veiculos.query.get_or_404(vehicle_id)

     if request.method == "POST":

          data_de_inicio = request.form['data_de_inicio']
          data_de_fim = request.form['data_de_fim']

          print(data_de_inicio, data_de_fim)

          return redirect(url_for("views.checkout", data_de_inicio=data_de_inicio, data_de_fim=data_de_fim, vehicle_id=vehicle_id))

 
     return render_template("vehicle.html" , vehicle=vehicle)

@views.route("/checkout/<int:vehicle_id>", methods=["GET","POST"])
@login_required
def checkout(vehicle_id):

     vehicle = Veiculos.query.get_or_404(vehicle_id)

     metodos_de_pagamento = Pagamento.query.all()

     start_date = request.args.get("data_de_inicio")
     end_date = request.args.get("data_de_fim")

     

     if request.method == "POST":


          # DADOS DO COMPRADOR

          nova_reserva = Reservas(
               first_name = request.form["firstname"],
               last_name = request.form["lastname"],
               email = request.form["email"],
               endereco = request.form["endereco"],
               cidade = request.form["cidade"],
               distrito = request.form["distrito"],
               codigo_postal = request.form["codigo_postal"],
               data_de_inicio = datetime.strptime(start_date, '%Y-%m-%d').date(),
               data_de_fim = datetime.strptime(end_date, '%Y-%m-%d').date(),

               # DADOS DE PAGAMENTO
               metodo_de_pagamento_id = request.form["metodo_de_pagamento"],
               nome_do_cartao = request.form["cc-name"],
               numero_do_cartao = request.form["cc-number"],
               data_de_validade = request.form["cc-expiration"],
               cvv = request.form["cc-cvv"],
               veiculo_id = vehicle_id
               )
          

          db.session.add(nova_reserva)
          db.session.commit()

          print(nova_reserva.data_de_inicio, nova_reserva.data_de_fim)
     
          return redirect(url_for("views.index"))


     return render_template("checkout.html",data_de_inicio=start_date, data_de_fim=end_date, metodos_de_pagamento=metodos_de_pagamento, vehicle=vehicle)