
class Barraca:
    def __init__(self, id_barraca, nome_barraca, estoque, parque):
        # estoque é dict {'item': {'quantidade': int, 'preco': float}}
        self.id_barraca = id_barraca
        self.nome_barraca = nome_barraca
        self.estoque = estoque  
        self.lista_funcionarios = {}
        self.itens_venda = {}
        self.parque = parque
        parque.barracas[id_barraca] = self

    def ver_estoque(self):
        print(f"Estoque da barraca {self.nome_barraca}:")
        for item, info in self.estoque.items():
            print(f"{item}: {info['quantidade']} unidades - R${info['preco']:.2f} cada")

    def adicionar_itens_venda(self):
        item = input("Item para venda: ")
        if item not in self.estoque:
            print("Item não disponível no estoque.")
            return

        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            return

        if self.estoque[item]['quantidade'] >= quantidade:
            self.estoque[item]['quantidade'] -= quantidade
            self.itens_venda[item] = self.itens_venda.get(item, 0) + quantidade
            
            valor_venda = quantidade * self.estoque[item]['preco']
            self.parque.total_vendidos += valor_venda

            print(f"{quantidade} unidades de {item} vendidas por R${valor_venda:.2f}.")
        else:
            print("Quantidade insuficiente no estoque.")






