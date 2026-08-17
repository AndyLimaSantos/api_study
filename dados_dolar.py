import requests
import os
import pprint #apenas para testar as coisas que preciso quando preciso ver os arquivos que vem das requisições da api
from dotenv import load_dotenv
load_dotenv(override=True)

#importação de dados do Filme
parametros = {'t':"spider-man: brand new day"}
SITE_API  = os.getenv("OMDb_SITE")

resposta = requests.get(SITE_API, params=parametros)
#pprint.pprint(resposta.status_code)
#pprint.pprint(resposta.content)
if resposta.status_code == 200:
    dados_resposta = resposta.json()
    print(f'\
        O titulo do filme pesquisado é: {dados_resposta['Title']}\n\
        O ano de lançamento é: {dados_resposta['Year']}\n\
        O gênero é: {dados_resposta['Genre']}\n\
        Diretor: {dados_resposta['Director']}\n\
        Plot: {dados_resposta['Plot']}\n\
        País de lançamento: {dados_resposta['Country']}\n\
        Prêmios: {dados_resposta['Awards']}\n\
        Ratings: {dados_resposta['Ratings'][0]['Value']}\n\
        Metascore: {dados_resposta['Metascore']}\n\
        imdbRating: {dados_resposta['imdbRating']}\n\
        imdbVotes: {dados_resposta['imdbVotes']}\n\
        ID no imdb: {dados_resposta['imdbID']}\n\
          ')
