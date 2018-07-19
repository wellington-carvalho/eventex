# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório
2. Crie um Virtualenv com python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

'''Console
git clone git@github.com:wellington-carvalho/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activite
pip install -r requerements.txt
cp contrib/env-sample .env
python manage test
...

## Como fazer o deploy?

1. Crie uma instância heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET-KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

'''Console

heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force





