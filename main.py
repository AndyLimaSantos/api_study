import requests
import pprint
import os
from dotenv import load_dotenv
load_dotenv()
#Vamos utilizar uma API de clima que podemos extrair informações do clima
API_KEY_WEATHER = os.getenv("API_KEY_WEATHER") #Não deixar aqui essa chave
link_api = "http://api.weatherapi.com/v1/current.json" #O link base para fazer extração de dados éhttp://api.weatherapi.com/v1


#Na documentação da API é possivel ver oque é necessário passar para se fazer as requisições
#ler a documentação é de extrema importância para que possamos não cometer erro.
parametros = {'key':API_KEY_WEATHER ,'q':'São Paulo','lang':'pt'}
resposta = requests.get(link_api, params = parametros) #O .get faz uma requisição, ou seja ele pucha um dado do link informado.

#print(resposta.status_code)
#print(resposta.content)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()  #Pega as informações em .json() e transforma em um dicionario python
    #pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"]
    print(temp)
    print(descricao)
