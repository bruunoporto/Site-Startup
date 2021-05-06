import sqlite3

class usuario:
    def __init__(self, senha, nome, idade, documento, cidade, bairro):
        self.__nome = nome
        self.__senha = senha
        self.__idade = idade
        self.__documento = documento
        self.__cidade = cidade
        self.__bairro = bairro
       
    
    def registro_usuario(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES ('"+self.__nome+"','"+self.__idade+"','"+self.__senha+"','"+self.__cidade+"','"+self.__bairro+"','"+self.__documento+"')")
        con.commit()
        con.close()


class empresa:
    def __init__(self, nome_empresa, senha , tipo_empresa, cidade_empresa, bairro_empresa, rua_empresa, numero_empresa):
        self.__nome_empresa = nome_empresa
        self.__tipo_empresa = tipo_empresa
        self.__senha = senha
        self.__cidade_empresa = cidade_empresa
        self.__bairro_empresa = bairro_empresa
        self.__rua_empresa = rua_empresa
        self.__numero_empresa = numero_empresa
      

    def registro_empresa(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO enterprises VALUES ('"+self.__nome_empresa+"','"+self.__tipo_empresa+"','"+self.__senha+"','"+self.__cidade_empresa+"','"+self.__bairro_empresa+"','"+self.__rua_empresa+"','"+self.__numero_empresa+"')")
        con.commit()
        con.close()

def login_model(nome,senha):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    for el in cur.execute("SELECT * FROM users"):
        if el[0] == nome:
            if el[2]== senha:
                con.commit()
                con.close()
                return (True, "Usuario")
    for el in cur.execute("SELECT * FROM enterprises"):
        if el[0] == nome:
            print("opa")
            if el[2]== senha:
                con.commit()
                con.close()
                return (True, "Empresa")
    con.commit()
    con.close()
    return (False, "")

# con = sqlite3.connect('database.db')
# cur = con.cursor()

# Create table
# cur.execute('''CREATE TABLE enterprises (name text, type text, password text, city text, neighborhood text, street text, number real)''')
# cur.execute('''CREATE TABLE users (name text, age real, password text, city text, neighborhood text, document real)''')

# Insert a row of data
# cur.execute("INSERT INTO users VALUES ('Pedro Henrique',18,'12345678','Rio de Janeiro','Leblon','17120554700')")
# cur.execute("INSERT INTO enterprises VALUES ('Beco dos fodao','Boca de fumo','12345678','Rio de Janeiro','Leblon','Rua Professor Saboia Ribeiro',83)")
# Save (commit) the changes
#con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()