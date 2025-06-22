import random
from abc import ABC
from bilheteria import Bilheteria


class Parque:
    def __init__(self):
        self._ingressos_vendidos = 0
        self._total_vendidos = 0.0

        self._funcionarios_parque = {}
        self._barracas = {}
        self._brinquedos = {}
        self._bilheteria = Bilheteria(self)

        self._lista_logins = {
            'operador': 'op123',
            'gerencia': 'parque0!3',
            'bilheteiro': 'ingresso067'
        }

        self._logins_barracas = {}

        self.aberto = True

    @property
    def ingressos_vendidos(self):
        return self._ingressos_vendidos

    @property
    def total_vendidos(self):
        return self._total_vendidos

    @property
    def funcionarios_parque(self):
        return self._funcionarios_parque

    @property
    def barracas(self):
        return self._barracas

    @property
    def brinquedos(self):
        return self._brinquedos

    @property
    def bilheteria(self):
        return self._bilheteria

    @property
    def lista_logins(self):
        return self._lista_logins

    @property
    def logins_barracas(self):
        return self._logins_barracas

    @ingressos_vendidos.setter
    def ingressos_vendidos(self, quantidade):
        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                print("Quantidade inválida. Não pode ser negativa.")
                return
            self._ingressos_vendidos += quantidade
        except:
            print("Erro: quantidade de ingressos deve ser um número inteiro.")

    @total_vendidos.setter
    def total_vendidos(self, valor):
        try:
            valor = float(valor)
            if valor < 0:
                print("Valor inválido. Não pode ser negativo.")
                return
            self._total_vendidos += valor
        except:
            print("Erro: valor total deve ser numérico.")

    def abrir_parque(self):
        if self.aberto:
            print("Parque já está aberto.")
        else:
            self.aberto = True
            print("Parque aberto!")

    def fechar_parque(self):
        if not self.aberto:
            print("Parque já está fechado.")
        else:
            self.aberto = False
            print("Parque fechado.")

    def gerar_relatorio(self):
        try:
            print("\n===== RELATÓRIO DO PARQUE =====")
            print(f"Ingressos vendidos: {self.ingressos_vendidos}")
            print(f"Total arrecadado: R${self.total_vendidos:.2f}\n")

            print("== Barracas e Itens Vendidos ==")
            if not self.barracas:
                print("Nenhuma barraca cadastrada.")
            else:
                for barraca in self.barracas.values():
                    print(f"\nBarraca: {barraca.nome_barraca} (ID: {barraca.id_barraca})")
                    if not barraca.itens_venda:
                        print("  Nenhum item vendido.")
                    else:
                        for item, qtd in barraca.itens_venda.items():
                            print(f"  {item}: {qtd} unidades vendidas")

            print("\n== Brinquedos Cadastrados ==")
            if not self.brinquedos:
                print("Nenhum brinquedo cadastrado.")
            else:
                for b in self.brinquedos.values():
                    print(f"ID: {b.id_brinquedo} | Nome: {b.nome_brinquedo} | Estado: {b.estado}")

            print("\n== Funcionários Cadastrados ==")
            if not self.funcionarios_parque:
                print("Nenhum funcionário cadastrado.")
            else:
                for f in self.funcionarios_parque.values():
                    print(f"ID: {f._id_func} | Nome: {f._nome}")
            print("==============================\n")
        except:
            print(f"Ocorreu um erro ao gerar o relatório!")
