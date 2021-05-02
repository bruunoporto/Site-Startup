class user:
    def __init__(self, nome, idade, documento, cidade, bairro):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.cidade = cidade
        self.bairro = bairro
        pass

    def user_info_register(self, nome, idade, documento, cidade, bairro):
        pass  # salvar num txt metodo post/get


class enterprise:
    def __init__(self, nome_empresa, tipo_empresa, cidade_empresa, bairro_empresa, rua_empresa, numero_empresa):
        self.nome_empresa = nome_empresa
        self.tipo_empresa = tipo_empresa
        self.cidade_empresa = cidade_empresa
        self.bairro_empresa = bairro_empresa
        self.rua_empresa = rua_empresa
        self.numero_empresa = numero_empresa
        pass

    def entreprise_info_register(self, nome, idade, documento, cidade, bairro):
        pass  # salvar num txt metodo post/get