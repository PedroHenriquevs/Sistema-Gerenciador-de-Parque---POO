import random
from brinquedo import Brinquedo
from barraca import *
from abc import ABC


class Funcionario(ABC):
    def __init__(self, id_func, nome, cpf, telefone):
        self._id_func = id_func
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone


class GerenteParque(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone, parque):
        super().__init__(id_func, nome, cpf, telefone)
        self.parque = parque

    def adicionar_brinquedo(self):
        id = str(random.randint(1000, 9999))
        if id in self.parque.brinquedos:
            print("ID já cadastrado.")
            return

        nome = input("Nome do brinquedo: ").strip()
        try:
            capacidade = int(input("Capacidade: "))
            altura = float(input("Altura mínima: "))
        except ValueError:
            print("Valor inválido para capacidade ou altura.")
            return

        brinquedo = Brinquedo(id, nome, capacidade, altura)
        self.parque.brinquedos[id] = brinquedo
        print(f"Brinquedo {nome} adicionado com sucesso!")

    def adicionar_barraca(self):
        id_barraca = input("ID da barraca: ").strip()
        if id_barraca in self.parque.barracas:
            print("ID de barraca já cadastrado.")
            return
        nome_barraca = input("Nome da barraca: ").strip()
        estoque = {}

        print("Digite os itens do estoque da barraca (vazio para sair):")
        while True:
            item = input("Item: ").strip()
            if item == "":
                break
            try:
                quantidade = int(input(f"Quantidade de {item}: "))
                preco = float(input(f"Preço unitário de {item}: "))
            except ValueError:
                print("Entrada inválida para quantidade ou preço.")
                continue
            estoque[item] = {'quantidade': quantidade, 'preco': preco}

        login_barraca = input("Defina o login da barraca: ").strip()
        if login_barraca in self.parque.lista_logins or login_barraca in self.parque.logins_barracas:
            print("Login já existe. Escolha outro.")
            return
        senha_barraca = input("Defina a senha da barraca: ").strip()

        Barraca(id_barraca, nome_barraca, estoque, self.parque)

        self.parque.logins_barracas[login_barraca] = (senha_barraca, id_barraca)
        print(f"Barraca '{nome_barraca}' adicionada com sucesso! Login: {login_barraca}")

    def adicionar_funcionario(self):
        opcao = input("Adicionar (operador, barraca, bilheteiro): ").lower()

        id_func = input("ID do funcionário: ").strip()
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()

        if id_func in self.parque.funcionarios_parque:
            print("ID de funcionário já cadastrado.")
            return

        if opcao == 'operador':
            funcionario = OperadorBrinquedo(id_func, nome, cpf, telefone)
            self.parque.funcionarios_parque[id_func] = funcionario
            print(f"Operador {nome} adicionado com sucesso!")

        elif opcao == 'barraca':
            if not self.parque.barracas:
                print("Não há barracas cadastradas.")
                return

            for id, barraca in self.parque.barracas.items():
                print(f"ID: {id} | {barraca.nome_barraca}")

            id_barraca = input("ID da barraca: ").strip()
            barraca = self.parque.barracas.get(id_barraca)

            if not barraca:
                print("Barraca não encontrada.")
                return

            funcionario = FuncionarioBarraca(id_func, nome, cpf, telefone, id_barraca, self.parque)
            self.parque.funcionarios_parque[id_func] = funcionario
            barraca.lista_funcionarios[id_func] = funcionario
            print(f"Funcionário {nome} adicionado à barraca.")

        elif opcao == 'bilheteiro':
            funcionario = FuncionarioBilheteiro(id_func, nome, cpf, telefone, self.parque.bilheteria, self.parque)
            self.parque.funcionarios_parque[id_func] = funcionario
            self.parque.bilheteria.lista_funcionarios[id_func] = funcionario
            print(f"Bilheteiro {nome} adicionado com sucesso!")

        else:
            print("Opção inválida. Informe: operador, barraca ou bilheteiro.")

    def remover_funcionario(self):
        id_func = input("ID do funcionário: ").strip()

        if id_func in self.parque.funcionarios_parque:
            self.parque.funcionarios_parque.pop(id_func)
            self.parque.bilheteria.lista_funcionarios.pop(id_func, None)

            for barraca in self.parque.barracas.values():
                barraca.lista_funcionarios.pop(id_func, None)

            print("Funcionário removido com sucesso.")
        else:
            print("Funcionário não encontrado.")



class OperadorBrinquedo(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone):
        super().__init__(id_func, nome, cpf, telefone)

    def iniciar_brinquedo(self, brinquedo):
        if brinquedo.estado != 'parado':
            print("Brinquedo não pode ser iniciado. Verifique o estado.")
        else:
            brinquedo.estado = 'funcionando'
            print(f"{brinquedo.nome_brinquedo} está funcionando.")

    def parar_brinquedo(self, brinquedo):
        if brinquedo.estado != 'funcionando':
            print("Brinquedo não está em funcionamento.")
        else:
            brinquedo.estado = 'parado'
            print(f"{brinquedo.nome_brinquedo} foi parado.")

    def manutencao(self, brinquedo):
        brinquedo.estado = 'manutencao'
        print(f"{brinquedo.nome_brinquedo} está em manutenção.")

    def reativar(self, brinquedo):
        brinquedo.estado = 'parado'
        print(f"{brinquedo.nome_brinquedo} reativado e parado.")



class FuncionarioBarraca(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone, id_barraca, parque):
        super().__init__(id_func, nome, cpf, telefone)
        self.id_barraca = id_barraca
        self.parque = parque

    def ver_estoque(self):
        barraca = self.parque.barracas.get(self.id_barraca)
        if barraca:
            barraca.ver_estoque()
        else:
            print("Barraca não encontrada.")

    def adicionar_itens_venda(self):
        barraca = self.parque.barracas.get(self.id_barraca)
        if barraca:
            barraca.adicionar_itens_venda()
        else:
            print("Barraca não encontrada.")



class FuncionarioBilheteiro(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone, bilheteria, parque):
        super().__init__(id_func, nome, cpf, telefone)
        self.bilheteria = bilheteria
        self.parque = parque

    def vender_ingresso(self):
        if not self.parque.aberto:
            print("Parque fechado. Não é possível vender ingressos.")
            return
        try:
            preco = float(input("Valor do ingresso: "))
            if preco <= 0:
                print("O preço do ingresso deve ser maior que zero.")
                return
        except ValueError:
            print("Valor inválido para preço.")
            return

        self.bilheteria.vender_ingresso(preco)
