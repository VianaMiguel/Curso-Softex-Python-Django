class Estudante (Pessoa):
    def __init__ (self, nome, idade, matricula):
      super().__init__(nome, idade)
      self.matricula = matricula

    @property
    def matricula (self):
        return self.matricula

    @matricula.setter
    def  matrricula(self, nova_matricula):
        if isinstance(nova_matricula, float) and nova_matricula.strip():
            self._matricula = nova_matricula
        else:
            print("Erro: Digite numeros ")


p1 = {matematica:9.0, portugues:10, python:5}
dicionario_estudante:dict [str, list[Estudante]] = {"pessoa": [],}
dicionario_estudante["pessoa'"].append(p1)
    