import requests
import datetime
import tempfile
import pandas as pd
import os.path
import sys

# Verificar se foi passado parametro.
if len(sys.argv) < 2:
    sys.exit('Informe uma data!')

# Verificar se o parametro passado e o esperado.
def validate(date):
   try:
       datetime.datetime.strptime(date, '%Y%m%d')
   except ValueError:
       raise ValueError("Formato incorreto, YYYYMMDD")

validate(sys.argv[1])

date = sys.argv[1]
# url com csv para consultar pais da moeda
url_relation = 'https://www4.bcb.gov.br/Download/fechamento/M20200807.csv'
# url com csv da data especificada
url = f"https://www4.bcb.gov.br/Download/fechamento/{date}.csv"

# Buscar planilha da data especificada
req = requests.get(url)

# Se não existir cotacao no dia retorna x
if req.status_code != 200:
    sys.exit('x')

# Verificar se a planilha com os dados do pais existe 
if not os.path.isfile('relation.csv'):
    # Requisitando planilha com os dados dos paises das moedas
    req2 = requests.get(url_relation)
    with open('relation.csv', 'w') as f:
        f.write(req2.text.replace("  ","").replace(" ;",";"))

# Criar arquivo temporario para armazenar o csv
temp = tempfile.NamedTemporaryFile(mode='w+b', suffix='.csv', prefix='tmp', dir=None, delete=True)

# Tem anos que a quantidade de colunas mudam
tam_header = len(req.text.split('\n')[0].split(';'))
if int(tam_header) == 8:
    header = b"data;Cod Moeda;Tipo;Moeda;Taxa Compra;Taxa Venda;Paridade Compra;Paridade Venda\r\n"
else:
    header = b"data;Cod Moeda;Tipo;Moeda;Taxa Compra;Taxa Venda;Paridade Compra;Paridade Venda;PTAX\r\n"
   
with open(temp.name, "wb") as csv_file:
    csv_file.write(header)
    csv_file.write(req.content)

# Menor cotação
df = pd.read_csv(temp.name, delimiter=';')
menorc = df[df['Taxa Compra'] == df['Taxa Compra'].min()].to_dict()
moeda = menorc['Moeda'].popitem()[1]


# Informações da menor cotação
df2 = pd.read_csv('relation.csv', delimiter=';')
infoc = df2.loc[df2["Simbolo"] == moeda ].to_dict()


# Exibir Moeda, Pais, cotacao dolar
print(f"{moeda}, {infoc['País'].popitem()[1].replace(',',' -')}, {menorc['Paridade Compra'].popitem()[1]}")
