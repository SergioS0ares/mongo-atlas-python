import pandas as pd

# Converter DataFrame Pandas para JSON (MongoDB aceita esse formato)
dados_json = df.to_dict(orient="records")

# Inserir os dados na coleção do MongoDB
collection.insert_many(dados_json)

print("Dados enviados para o MongoDB Atlas com sucesso!")
