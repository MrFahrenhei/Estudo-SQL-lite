import sqlite3

#cria um DB
conn = sqlite3.connect('customer.db')

#cria um cursor
c = conn.cursor()

#Para ordenar os elemetos
#ordem descrecente
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

#ordem alfabética do sobrenome
c.execute("SELECT rowid, * FROM customers ORDER BY last_name")

items = c.fetchall()

for item in items:
    print(item)

#print('sucesso meu parceiro')
#commit nosso comando
conn.commit()

#fechar o comando
conn.close()