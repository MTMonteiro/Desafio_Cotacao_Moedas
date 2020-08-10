# Obter cotação da moeda a partir do site do Banco Central(Solução desafio) 
O objetivo era um programa para obter dados utilizando como referencia o site
do banco central, o programa recebe uma data como parametro no formato YYYYMMDD e retornar
os dados separados por virgula do:
- o símbolo da moeda com menor cotação,
- o nome do país de origem da moeda e
- o valor da cotação desta moeda frente ao dólar na data especificada.

# Requisitos 

Requisitos necessários para executar o programa:
- python3
- Linux

# Instalando dependências
```shell
$ pip install -r requirements
```
ou 
```shell
$ pip install pandas requests
```
# Utilização
```shell
$ python3 csvcotacao.py YYYYMMDD

```
EX:
``` shell
$ python3 csvcotacao.py 20150805
IRR, IRA - REPUBLICA ISLAMICA DO, 29710,00000000
```
Um arquivo 'relation.csv' será criado no diretório atual, 
para agilizar as próximas consultas.

# OBS
No site do Banco Central é possivel encontrar uma API para obter os dados,
Porém a API não possui maturidade além de ter poucas moedas disponiveis para consulta,
logo não segui por esse caminho.

# Script utilizando API do bcb

```shell 
python3 apicotacao.py YYYYMMDD
```

Code by _Matheus Monteiro_.
