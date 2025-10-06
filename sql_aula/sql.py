import sqlite3

conn= sqlite3.connect('meu_banco.db')

print("Banco de dados 'meu_banco.db' criado com sucesso")
      
conn.close()