from abc import ABC
import datetime

class Parque:
    def __init__(self):
        self._total_ingresso = 0
        self._total_vendidos = 0.0
        self._data = datetime.now()
        self.brinquedos = []

    @property
    def total_ingresso(self):
        return self._total_ingresso
    
    @property
    def total_vendidos(self):
        return self.total_vendidos
    
    @property
    def data(self):
        return self._data
    
    @total_vendidos.setter
    def total_vendidos(self, valor):
        if (valor >= 0):
            self._total_vendidos += valor
        
    
class Brinquedo(ABC):
    
    def __init__(self, id_brinquedo, capacidade, qtd_pessoa, altura_min):
        self._id_brinquedo = id_brinquedo
        self._capacidade = capacidade
        self._qtd_pessoa = qtd_pessoa
        self._altura_min = altura_min
        self._registrador = {}
        self.disponivel = True

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
    
    

    def adicionar_pessoa(self):
        pass

    def verifica_brinquedo

        

    
        