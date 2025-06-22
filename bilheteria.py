class Bilheteria:
    def __init__(self, parque):
        self.caixa = 0.0
        self.ingressos_vendidos = 0
        self.parque = parque
        self.lista_funcionarios = {}

    def vender_ingresso(self, preco):
        if not self.parque.aberto:
            print("Parque fechado. Não é possível vender ingressos.")
            return

        if preco <= 0:
            print("O valor do ingresso deve ser maior que zero.")
            return

        try:
            preco = float(preco)
        except:
            print("Preço inválido. Informe um valor numérico.")
            return

        self.caixa += preco
        self.ingressos_vendidos += 1
        self.parque.ingressos_vendidos += 1
        self.parque.total_vendidos += preco

        print(f"Ingresso vendido com sucesso por R${preco:.2f}!")

    def ver_caixa(self):
        print(f"\n===== Caixa da Bilheteria =====")
        print(f"Total arrecadado: R${self.caixa:.2f}")
        print(f"Ingressos vendidos: {self.ingressos_vendidos}")
        print("================================\n")

    def mostrar_funcionarios(self):
        if not self.lista_funcionarios:
            print("Nenhum funcionário na bilheteria.")
        else:
            for id_func, funcionario in self.lista_funcionarios.items():
                print(f"ID: {id_func} | Nome: {funcionario._nome}")
