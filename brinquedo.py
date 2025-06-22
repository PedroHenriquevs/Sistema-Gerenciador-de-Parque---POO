from abc import ABC
class Brinquedo(ABC):
    
    def __init__(self, id_brinquedo, capacidade, qtd_pessoa, altura_min):
        self._id_brinquedo = id_brinquedo
        self._capacidade = capacidade
        self._qtd_pessoa = qtd_pessoa
        self._altura_min = altura_min
        self._registrador = {}
        self.estado = "ativo"

    @property
    def id_brinquedo(self):
        return self._id_brinquedo
    
    @property
    def capacidade(self):
        return self._capacidade
    
    @property
    def qtd_pessoa(self):
        return self._qtd_pessoa
    
    @property
    def altura_min(self):
        return self._altura_min
    
    @capacidade.setter
    def capacidade(self, nova_capacidade):
        if(nova_capacidade >= 0):
            self._capacidade = nova_capacidade
        else:
            print("Erro: capacidade inválida")        

    @qtd_pessoa.setter
    def qtd_pessoa(self, qtd):
        if(qtd >= 0):
            self._qtd_pessoa = qtd
        else:
            print("Error: Quantidade inválida")

    @altura_min.setter
    def altura_min(self, altura):
        if(altura >= 0):
            self._altura_min = altura
        else:
            print("Error: Altura inválida!")
    
    @property
    def registrador(self):
        return self._registrador
