import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

# Criando a tabela Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados")