from config import Blueprint, send_file, jsonify, render_template, request
from models import Veiculos
from io import BytesIO


views = Blueprint("views", __name__)




@views.route("/vehicle_information/<int:vehicle_id>")
def get_vehicle(vehicle_id):

     vehicle = Veiculos.query.get_or_404(vehicle_id)

     

     return render_template("vehicle.html" , vehicle=vehicle)

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

     for v in vehicles:
          print(v.preco)


     return render_template('index.html', vehicles=vehicles)


@views.route('/filter', methods=['GET'])
def filter_vehicles():

     query = Veiculos.query

     search_marca = request.args.get("search_marca", "")

     search_modelo = request.args.get("search_modelo", "")

     num_pessoas = request.args.get("num_pessoas", type=int)

     tipo_de_veiculo = request.args.get("tipo_de_veiculo")

     preco_do_veiculo = request.args.get("preco_do_veiculo")

     ordem_prod = request.args.get("ordem_prod", "price_asc")



     print(query)

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


     return render_template('index.html', 
                            vehicles=vehicles,
                            search_marca = search_marca,
                            search_modelo=search_modelo,
                            num_pessoas=num_pessoas,
                            tipo_de_veiculo= tipo_de_veiculo,
                            preco_do_veiculo=preco_do_veiculo,
                            ordem_prod=ordem_prod)

# @views.route('/checkout', methods=['GET', 'POST'])
# def checkout():
#      if request.method == 'POST':

#           checkout_data = checkout(
#           first_name = request.form['first_name']
#           last_name = request.form['last_name']
#           email = request.form['email']
#           address = request.form['address']
#           city = request.form['city']
#           )
#           return render_template('checkout.html', 
#                                  first_name=first_name, 
#                                  last_name=last_name,
#                                  email=email,
#                                  address=address,
#                                  city=city,)


          
     
     