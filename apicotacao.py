import requests
import sys
from datetime import datetime

moedas_url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json'
dateIn = sys.argv[1]
data1 = datetime.strptime(dateIn,'%Y%m%d').strftime('%m-%d-%Y')
data2 = data1

def get_cotacao(moeda):
    url_base = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='" + moeda + "'&@dataInicial='"+ data1 +"'&@dataFinalCotacao='"+ data2 +"'&$top=1&$format=json&$select=cotacaoCompra"
    cotacao = requests.get(url_base)
    cotacaoValue = cotacao.json()['value']
    return cotacaoValue

moedas = requests.get(moedas_url)
mi = {'cotacaoCompra':10}
for line in moedas.json()['value']:
    aux = get_cotacao(line['simbolo'])

    if (aux[0]['cotacaoCompra'] < mi['cotacaoCompra']):
        mi['cotacaoCompra'] = aux[0]['cotacaoCompra']
        mi['simbolo'] = moedas.json()['value'][0]['simbolo']
        mi['nome'] = moedas.json()['value'][0]['nomeFormatado']

print(mi)

