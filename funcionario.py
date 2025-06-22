from classeABCPessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id,  nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)
        self._id = id

class OperadorBrinquedo(Funcionario):
    def __init__(self, id, nome, cpf, telefone, brinq_res):
        super().__init__(id, nome, cpf, telefone)
        self._brinq_res = brinq_res