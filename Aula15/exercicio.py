class pessoa:
    def __init__(self, nome:str, idade:int):
        self._nome = nome
        self._idade = idade

    @property 
    def nome (self):
        return  self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self._nome = novo_nome
        else:
            print("Erro: nome não é uma string")


    @property 
    def idade (self):
        return  self._idade
    
    @idade.setter
    def set_nome(self, nova_idade):
        if isinstance (nova_idade,(int, float)) and nova_idade >=0:
            self._idade = nova_idade
        else:
            print("Erro numerico")
