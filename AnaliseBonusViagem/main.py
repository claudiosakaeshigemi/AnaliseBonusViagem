import os
import pandas as pd
from twilio.rest import Client

# instalar
# -- pandas
# - openpyxl
# - twilio

# passo a passo de solução:


# abrir os 6 arquivos em EXCEL
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ["ACe11480ac35b785bf59d1d973c4a3fc6f"]
#auth_token = os.environ["677b88679cf8150667a625f11f5d2419"]

account_sid = "ACe11480ac35b785bf59d1d973c4a3fc6f"
auth_token = "677b88679cf8150667a625f11f5d2419"
client = Client(account_sid, auth_token)


for mes in lista_meses:
    #    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f' no mês de {mes} o vendedor: {vendedor} vendeu: ${vendas} em vendas.')
        message = client.messages. \
            create(
            #55= código de area do pais
            to='+5544991810583',
            from_='+12396883789',
            body=(f' no mês de {mes} o vendedor: {vendedor} vendeu: ${vendas} em vendas.'))
        print(message.sid)

   # message = client.messages \
   #      .create(
   #      from_='+12396883789',
   #      to='+1544991810583',
   #      body="Join Earth's mightiest heroes. Like Kevin Bacon."
   #   )
