class usuario:
    def __init__(self, senha, nome, idade, documento, cidade, bairro):
        self.__nome = nome
        self.__senha = senha
        self.__idade = idade
        self.__documento = documento
        self.__cidade = cidade
        self.__bairro = bairro
       
    
    def registro_usuario(self):
        registro_de_usuarios = self.__nome + " - " + self.__senha  + "\n"
        arquivo = open("registro_de_usuarios.txt","a")
        arquivo.writelines(registro_de_usuarios)


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
        registro_de_empresas = self.__nome_empresa + " - " + self.__senha  + "\n"
        arquivo = open("registro_de_empresas.txt","a")
        arquivo.writelines(registro_de_empresas)
