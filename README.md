# Explicação de API e alugums informações importante
## Introdução - Oque é uma API

API - Aplications programming interface.
É a parte de um sistema onde eles permitem conectar os códigos com o sistema que foi criado. Muitos sites tem api's próprias a netfix, paypal, mercado livre, todos possuem API's que permites ao úsuario a se conectar com informações do sistemas utilizando API's

**Mas como se conectar a essas API's?** A conecxão ocorre atravé de requisições, que no python são traduzidas em _REQUEST_, é um pacote de código no python que permitem fazer requisições internas ao sistema de interesse.

## PRIMEIRO PASSO PARA USO DE API
1. Criar uma conta no sistema que deseja utilizar a API.

2. Normalmente quando cair nas telas de api, você vao buscar uma API Key, ou uma API Token, ela vai ser utilizada para mostrar que a pessoa que esta logando nesse sistema é você mesmo, assim não é necessário fazer o login sempre que precisar fazer uma requisição

3. Procurar o link da api onde você vai fazer a requisição, isso ocorre na documentação da API (Request URL)

>As API's retornam sempre o formato JSON ou formato xml, preferencialmente use o JSON, os códigos em python trabalham melhor com JSON

4. Precisamos de uma biblioteca agora para fazer as requisições dos dados, para isso utilizaremos a biblioteca request do python, não vem instalado, logo é necessário fazer a instalação na primeira vez ele permite fazer eequisições.

>pip install requests




## ALGUMAS EXPLICAÇÔES
toda resposta de quauqer requisição tem um status code
**status_code**: é o codigó de status
    - 200: deu certo a requisição
    - 300: a qrequisição foi redirecionada
    - 400: não conseguiu fazer a requisiçã o(401, significa que você não possui auorização para fazer a requisição.)
    - 500: deu um erro no sistema em que você esta fazendo requisição, não tem haver com o seu código

podemos pedir para ele retornar o código de status utilizando o seguinte código, com a variavel que esta armazenada sua resposta.

>print(resposta.status_code)

**content**: nada mais é que o conteúdo da sua resposta.
Você sempre pode olhar o conteudo da resposta após a requisição, para saber oque ocorreu de errado com o sistema.

>print(resposta.content)

Toda API precisa que seja passado alguns parâmetros, oque são esses parâmetros? Nada mais são que dicíonarios em python, você deve criar um dicíonário com os parâmetros que deseja e que são necessário pela API que esta utilizando.

A requisição só da certo se o status_code = 200, logo posso utilizar isso para construção de condicionais


No entanto é muito difícil navegar nos dicionários que são devolvidos pelas api's e transformadas em dicionários com o método .json(), para isso utilizamos a biblioteca pprint, ela deixa a apresentação mais bonita.


### Gerenciamento de senha de maneira segura.

Utilização de variaveis de ambiente, são valores que só existem dentro do ambiente de produção, ou seja, é um valor que se altera de local para local (Ambiene para ambiente)

podemos criar variaveis de ambiente de duas formas. 
1. #utilizando o terminanl do windows com o setx
> setx NOME_VARIAVEL_AMBIENTE "valor_variavel_ambiente"

ele vai retornar um "ÊXITO: o valor especificado foi salvo"

para usar no código devemos importar a biblioteca os

> import os
> chave = os.getenv("NOME_VARIAVEL_AMBIENTE")

2. Criação de um arquivo chamado .env, que é um arquivo de variavel de ambiete. Esses arquivos por padrão são ignorados. No entanto para ler um arquivo env, é necessário instalar uma biblioteca que não esta no python por padrão chamado dotenv

> pip install python-dotenv

na hora de importar usamos o 

> from  dotenv import load_dotenv
> load_dotenv(overrider = True)
> chave = os.getenv("NOME_VARIAVEL_AMBIENTE")

o overrider da preferencia para a variavel no arquivo .env

3. Utilização de sistema externo, criação de senhas através de um sistema externo que você consulta ele para gerar chaves.

