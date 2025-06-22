class Barraca:
    def __init__(self, id_barraca, nome_barraca, estoque, parque):
        self.id_barraca = id_barraca
        self.nome_barraca = nome_barraca
        self.estoque = estoque  
        self.lista_funcionarios = {}
        self.itens_venda = {}
        self.parque = parque
        parque.barracas[id_barraca] = self

    def ver_estoque(self):
        if not self.estoque:
            print(f"A barraca {self.nome_barraca} não possui itens no estoque.")
            return

        print(f"\n=== Estoque da barraca {self.nome_barraca} ===")
        for item, info in self.estoque.items():
            print(f"{item}: {info['quantidade']} unidades - R${info['preco']:.2f} cada")
        print("============================================")

    def adicionar_itens_venda(self):
        if not self.estoque:
            print("Não há itens cadastrados no estoque para venda.")
            return

        item = input("Item para venda: ").strip()

        if item == "":
            print("Nenhum item informado.")
            return

        if item not in self.estoque:
            print(f"Item '{item}' não encontrado no estoque.")
            return

        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Quantidade deve ser um número positivo.")
                return
        except:
            print("Quantidade inválida. Digite um número inteiro.")
            return

        if self.estoque[item]['quantidade'] < quantidade:
            print(f"Quantidade insuficiente no estoque. Disponível: {self.estoque[item]['quantidade']}")
            return

       
        self.estoque[item]['quantidade'] -= quantidade
        self.itens_venda[item] = self.itens_venda.get(item, 0) + quantidade

        valor_venda = quantidade * self.estoque[item]['preco']
        self.parque.total_vendidos += valor_venda

        print(f"{quantidade} unidades de '{item}' vendidas por R${valor_venda:.2f}.")
