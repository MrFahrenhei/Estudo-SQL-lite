import sqlite3
 
#funçao para retornar todos os elemetos
def show_all():

    #cria um DB e um cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)
        
    #para fazer commit e fechar a função
    conn.commit()
    conn.close()

#adicionar um novo elemento
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    
    conn.commit()
    conn.close()

#adiciona varios elementos
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    
    conn.commit()
    conn.close()
    

#deleta elemento da tabela
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    conn.commit()
    conn.close()

# puxar elemento da tabela
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()
