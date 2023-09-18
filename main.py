import pandas as pd
import requests
import json
#import openai
import random

sdw2023_api_url = "https://sdw-2023-prd.up.railway.app"

# Extrair os ID's do arquivo CSV
df = pd.read_csv("SDW2023.csv")
user_ids = df['UserID'].to_list()

# Obter os dados de cada ID usando a API do link: https://sdw-2023-prd.up.railway.app
def get_user(id):
    response = requests.get(f"{sdw2023_api_url}/users/{id}")
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
#print(json.dumps(users, indent=2))

# Código da api key gerada pela OPENAI API
"""openai_api_key = "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"

openai.api_key = openai_api_key"""

"""def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3",
        messages=[
            {"role": "system","content": "Você é um especialista em marketing bancário"},
            {"role": "user", "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"}
        ]
    )
    return completion.choices[0].message.content"""
"""
TODO Dentro do contexto dessa implementação, basta chamarmos a função generate_ai_news passando como argumento o user e atribuir o retorno a uma variável concantenando com o nome do usuário
"""

"""
Pela falta de acesso a API, implemetei uma tupla com mensagens genéricas que são concatenandas com o usuário de maneira aleatória. Ou seja, o fluxo ETL ainda continua. Os ID's dos usuários são extraídos da planilha, cada usuário recebe uma mensagem escolhida de uma tupla de mensagens e posteriormente as mensagens são carregadas na api santander dev week
"""
messages = ( "Invista no seu futuro", "Experimente o plano Vip. Essa será uma ótima decisão", "Já conhece o lounge PythonBank? Experimente!")

def generate_news():
    for m in messages:
        random_number = random.randrange(0, 2)
        for user in users:
            user_message = f"Olá, {user['name']}. {messages[random_number]}"
    return user_message


    