
from datetime import datetime



def diferenca(inicio, fim):

     if isinstance(inicio, str):  
          data_de_inicio = datetime.strptime(inicio, '%Y-%m-%d').date()
     else:
          data_de_inicio = inicio 

     if isinstance(fim, str):
          data_de_fim = datetime.strptime(fim, '%Y-%m-%d').date()
     else:
          data_de_fim = fim  

     diferenca = (data_de_fim - data_de_inicio).days

     return diferenca


def preco_total(valor_do_carro, num_de_dias):

     return valor_do_carro * num_de_dias

