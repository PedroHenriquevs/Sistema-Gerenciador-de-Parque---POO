class Brinquedo:
    def __init__(self, id_brinquedo, nome_brinquedo, capacidade, altura_min):
        self.id_brinquedo = id_brinquedo
        self.nome_brinquedo = nome_brinquedo
        self.capacidade = capacidade
        self.altura_min = altura_min
        self.estado = 'parado'