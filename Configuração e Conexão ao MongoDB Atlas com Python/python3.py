import pandas as pd
import pymongo
import urllib.parse

# Definir o caminho do arquivo CSV
csv_path = r"C:\Users\sergy\OneDrive\Documentos\Configuração e Conexão ao MongoDB Atlas com Python\sales_data_sample.csv"

# Ler o CSV usando Pandas
df = pd.read_csv(csv_path)

# Exibir as 5 primeiras linhas
print(df.head())

#------------------------------------------------------------------------------------------------------------------

# Definir usuário e senha
username = "Juliokawahata"
password = "Essasenhaehboa"

# Codificar a senha (caso tenha caracteres especiais)
password_encoded = urllib.parse.quote_plus(password)

# Criar a URI corretamente formatada
MONGO_URI = f"mongodb+srv://{username}:{password_encoded}@clustersuspeito.twhb.mongodb.net/?retryWrites=true&w=majority&appName=ClusterSuspeito"

# Conectar ao MongoDB Atlas
client = pymongo.MongoClient(MONGO_URI)

# Acessar o banco e a coleção
db = client["filmes"]
collection = db["filmes-series"]

print("Conexão com MongoDB Atlas estabelecida!")

#------------------------------------------------------------------------------------------------------------------

# Converter DataFrame Pandas para JSON (MongoDB aceita esse formato)
dados_json = df.to_dict(orient="records")

# Inserir os dados na coleção do MongoDB
collection.insert_many(dados_json)

print("Dados enviados para o MongoDB Atlas com sucesso!")
