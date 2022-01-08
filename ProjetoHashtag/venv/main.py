import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACca099df58699c26d9b4a2f4af45c4d61"
# Your Auth Token from twilio.com/console
auth_token  = "5fc67bd1225e954fff8e3deda5d659e5"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} Alguém batel a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511973710076",
            from_="+13342181895",
            body=f'No mês {mes} Alguém batel a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)




#Para cada arquivo:

# Verificar se algum valor é maior que 55.000