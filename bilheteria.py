class Bilheteria:
    def __init__(self, parque):
        self.caixa = 0.0
        self.ingressos_vendidos = 0
        self.parque = parque
        self.lista_funcionarios = {}

    def vender_ingresso(self, preco):
        self.caixa += preco
        self.ingressos_vendidos += 1
        self.parque.ingressos_vendidos += 1
        self.parque.total_vendidos += preco
        print(f"Ingresso vendido por R${preco:.2f}")

    def ver_caixa(self):
        print(f"Caixa atual: R${self.caixa:.2f}")

    def mostrar_funcionarios(self):
        if not self.lista_funcionarios:
            print("Nenhum funcionário na bilheteria.")
        else:
            for id_func, funcionario in self.lista_funcionarios.items():
                print(f"ID: {id_func} | Nome: {funcionario._nome}")