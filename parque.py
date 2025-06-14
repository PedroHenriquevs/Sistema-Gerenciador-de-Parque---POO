from abc import ABC
import datetime

class Parque:
    def __init__(self):
        self._total_ingresso = 0
        self._total_vendidos = 0.0
        self._data = datetime.now()
        self.brinquedos = []
        self._funcionarios = {}
        self._registro_brinquedos = {} #Adicionar o get para esse atributo

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
        

class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone

class Funcionario(Pessoa):
    def __init__(self, id,  nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)
        self._id = id

class OperadorBrinquedo(Funcionario):
    def __init__(self, id, nome, cpf, telefone, brinq_res):
        super().__init__(id, nome, cpf, telefone)
        self._brinq_res = brinq_res
        
class Zelador(Funcionario):
    def __init__(self, id, nome, cpf, telefone, setor):
        super().__init__(id, nome, cpf, telefone)
        self._setor = setor
        
    

        
    
    

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
    

    def adicionar_pessoa(self):
        pass
    
    def esvaziar_brinquedo(self):
        pass

    def mostrar_brinquedo(self):
        pass

    def em_manutencao(self):
        pass

    def iniciar_brinquedo(self):
        pass

    def parar_brinquedo(self):
        pass

    def reativar_brinquedo(self):
        pass

    def status(self):
        pass

    def verifica_tempo(self):
        pass

#Provável alteração na criação das classes derivadas, para atributo em brinquedo
class Montanha_Russa(Brinquedo):
    def __init__(self, id_brinquedo, capacidade, qtd_pessoa, altura_min):
        super().__init__(id_brinquedo, capacidade, qtd_pessoa, altura_min)
        self._qtd_ingresso = 0
        self._total_venda = 0.0       

    def adicionar_pessoa(self):
        

    