import random
from abc import ABC

# =========================================================
# ========================= PARQUE ========================
# =========================================================
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

        # Novo dicionário para logins/senhas das barracas
        self._logins_barracas = {}  # {'login_barraca': ('senha', 'id_barraca')}

        self.aberto = True

    # ---------------- PROPERTIES ----------------
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

    # ---------------- SETTERS ----------------
    @ingressos_vendidos.setter
    def ingressos_vendidos(self, quantidade):
        self._ingressos_vendidos += quantidade

    @total_vendidos.setter
    def total_vendidos(self, valor):
        self._total_vendidos += valor

    # ---------------- MÉTODOS ----------------
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


# =========================================================
# ======================= FUNCIONÁRIO ====================
# =========================================================
class Funcionario(ABC):
    def __init__(self, id_func, nome, cpf, telefone):
        self._id_func = id_func
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone


# =========================================================
# ===================== GERENTE ===========================
# =========================================================
class GerenteParque(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone, parque):
        super().__init__(id_func, nome, cpf, telefone)
        self.parque = parque

    def adicionar_brinquedo(self):
        id = str(random.randint(1000, 9999))
        if id in self.parque.brinquedos:
            print("ID já cadastrado.")
            return

        nome = input("Nome do brinquedo: ")
        capacidade = int(input("Capacidade: "))
        altura = float(input("Altura mínima: "))

        brinquedo = Brinquedo(id, nome, capacidade, altura)
        self.parque.brinquedos[id] = brinquedo
        print(f"Brinquedo {nome} adicionado com sucesso!")

    def adicionar_barraca(self):
        id_barraca = input("ID da barraca: ")
        if id_barraca in self.parque.barracas:
            print("ID de barraca já cadastrado.")
            return
        nome_barraca = input("Nome da barraca: ")
        estoque = {}

        print("Digite os itens do estoque da barraca (digite vazio para parar):")
        while True:
            item = input("Item: ")
            if item == "":
                break
            try:
                quantidade = int(input(f"Quantidade de {item}: "))
                preco = float(input(f"Preço unitário de {item}: "))
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue
            estoque[item] = {'quantidade': quantidade, 'preco': preco}

        # Criar login e senha para a barraca
        login_barraca = input("Defina o login para esta barraca: ").strip()
        if login_barraca in self.parque.lista_logins or login_barraca in self.parque.logins_barracas:
            print("Login já existe. Tente outro.")
            return
        senha_barraca = input("Defina a senha para esta barraca: ").strip()

        # Criar a barraca
        Barraca(id_barraca, nome_barraca, estoque, self.parque)

        # Salvar login/senha na estrutura de logins das barracas
        self.parque.logins_barracas[login_barraca] = (senha_barraca, id_barraca)

        print(f"Barraca '{nome_barraca}' adicionada com sucesso! Login: {login_barraca}")

    def adicionar_funcionario(self):
        opcao = input("Adicionar (operador, barraca, bilheteiro): ").lower()

        id_func = input("ID do funcionário: ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")

        if opcao == 'operador':
            funcionario = OperadorBrinquedo(id_func, nome, cpf, telefone)
            self.parque.funcionarios_parque[id_func] = funcionario
            print(f"Operador {nome} adicionado!")

        elif opcao == 'barraca':
            if not self.parque.barracas:
                print("Não há barracas cadastradas.")
                return
            for id, barraca in self.parque.barracas.items():
                print(f"ID: {id} | {barraca.nome_barraca}")

            id_barraca = input("ID da barraca: ")

            if id_barraca not in self.parque.barracas:
                print("Barraca não encontrada.")
                return

            funcionario = FuncionarioBarraca(id_func, nome, cpf, telefone, id_barraca, self.parque)
            self.parque.funcionarios_parque[id_func] = funcionario
            self.parque.barracas[id_barraca].lista_funcionarios[id_func] = funcionario
            print(f"Funcionário {nome} adicionado à barraca.")

        elif opcao == 'bilheteiro':
            funcionario = FuncionarioBilheteiro(id_func, nome, cpf, telefone, self.parque.bilheteria, self.parque)
            self.parque.funcionarios_parque[id_func] = funcionario
            self.parque.bilheteria.lista_funcionarios[id_func] = funcionario
            print(f"Bilheteiro {nome} adicionado!")

        else:
            print("Opção inválida.")

    def remover_funcionario(self):
        id_func = input("ID do funcionário: ")

        if id_func in self.parque.funcionarios_parque:
            self.parque.funcionarios_parque.pop(id_func)
            self.parque.bilheteria.lista_funcionarios.pop(id_func, None)

            for barraca in self.parque.barracas.values():
                barraca.lista_funcionarios.pop(id_func, None)

            print("Funcionário removido!")
        else:
            print("Funcionário não encontrado.")


# =========================================================
# =================== OPERADOR DE BRINQUEDO ===============
# =========================================================
class OperadorBrinquedo(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone):
        super().__init__(id_func, nome, cpf, telefone)
        self.brinquedo_responsavel = None

    def iniciar_brinquedo(self, brinquedo):
        if brinquedo.estado != 'parado':
            print("Não pode iniciar. Verifique o estado atual.")
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


# =========================================================
# ==================== FUNCIONÁRIO BARRACA ================
# =========================================================
class FuncionarioBarraca(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone, id_barraca, parque):
        super().__init__(id_func, nome, cpf, telefone)
        self.id_barraca = id_barraca
        self.parque = parque

    def ver_estoque(self):
        barraca = self.parque.barracas[self.id_barraca]
        barraca.ver_estoque()

    def adicionar_itens_venda(self):
        barraca = self.parque.barracas[self.id_barraca]
        barraca.adicionar_itens_venda()


# =========================================================
# ================== FUNCIONÁRIO BILHETEIRO ===============
# =========================================================
class FuncionarioBilheteiro(Funcionario):
    def __init__(self, id_func, nome, cpf, telefone, bilheteria, parque):
        super().__init__(id_func, nome, cpf, telefone)
        self.bilheteria = bilheteria
        self.parque = parque

    def vender_ingresso(self):
        if not self.parque.aberto:
            print("Parque fechado. Não é possível vender ingressos no momento.")
            return
        preco = float(input("Valor do ingresso: "))
        self.bilheteria.vender_ingresso(preco)


# =========================================================
# ======================== BRINQUEDO ======================
# =========================================================
class Brinquedo:
    def __init__(self, id_brinquedo, nome_brinquedo, capacidade, altura_min):
        self.id_brinquedo = id_brinquedo
        self.nome_brinquedo = nome_brinquedo
        self.capacidade = capacidade
        self.altura_min = altura_min
        self.estado = 'parado'


# =========================================================
# ======================== BARRACA ========================
# =========================================================
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


# =========================================================
# ======================= BILHETERIA ======================
# =========================================================
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


# ===================== LOGIN =====================
def login(parque):
    print("\n======= LOGIN =======")
    print("Cargos disponíveis: gerencia, operador, bilheteiro, <login de barraca>")
    usuario = input("Digite o login: ").lower()
    senha = input("Digite a senha: ")

    # Verificar se é login de funcionário comum
    if usuario in parque.lista_logins and parque.lista_logins[usuario] == senha:
        if not parque.aberto and usuario != 'gerencia':
            print("Parque fechado. Apenas gerência pode acessar o sistema.")
            return None, None
        print(f"Login bem-sucedido como {usuario}!\n")
        return usuario, None  # None para id_barraca

    # Verificar se é login de barraca
    if usuario in parque.logins_barracas and parque.logins_barracas[usuario][0] == senha:
        id_barraca = parque.logins_barracas[usuario][1]
        # Verificar se o parque está aberto
        if not parque.aberto:
            print("Parque fechado. Acesso às barracas bloqueado.")
            return None, None
        # Verificar se existe funcionário cadastrado para essa barraca
        barraca = parque.barracas.get(id_barraca)
        if barraca is None:
            print("Barraca não encontrada.")
            return None, None
        if not barraca.lista_funcionarios:
            print("Nenhum funcionário cadastrado para esta barraca.")
            return None, None

        print(f"Login bem-sucedido como barraca '{usuario}' vinculada à barraca ID {id_barraca}!\n")
        return 'tbarraca', id_barraca

    print("Usuário ou senha incorretos!\n")
    return None, None


# ===================== MENUS =====================
def menu_gerente(gerente):
    while True:
        print("\n=== Menu Gerente ===")
        print("1 - Adicionar brinquedo")
        print("2 - Adicionar funcionário")
        print("3 - Remover funcionário")
        print("4 - Mostrar brinquedos")
        print("5 - Mostrar funcionários")
        print("6 - Adicionar barraca")
        print("7 - Abrir parque")
        print("8 - Fechar parque")
        print("9 - Gerar relatório do parque")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            gerente.adicionar_brinquedo()
        elif opcao == '2':
            gerente.adicionar_funcionario()
        elif opcao == '3':
            gerente.remover_funcionario()
        elif opcao == '4':
            if not gerente.parque.brinquedos:
                print("Nenhum brinquedo cadastrado.")
            else:
                for b in gerente.parque.brinquedos.values():
                    print(f"ID: {b.id_brinquedo} | Nome: {b.nome_brinquedo} | Estado: {b.estado}")
        elif opcao == '5':
            if not gerente.parque.funcionarios_parque:
                print("Nenhum funcionário cadastrado.")
            else:
                for f in gerente.parque.funcionarios_parque.values():
                    print(f"ID: {f._id_func} | Nome: {f._nome}")
        elif opcao == '6':
            gerente.adicionar_barraca()
        elif opcao == '7':
            gerente.parque.abrir_parque()
        elif opcao == '8':
            gerente.parque.fechar_parque()
        elif opcao == '9':
            gerente.parque.gerar_relatorio()
        elif opcao == '0':
            print("Saindo do menu gerente.")
            break
        else:
            print("Opção inválida.")


def menu_operador(operador, parque):
    while True:
        if not parque.aberto:
            print("Parque fechado. Operações com brinquedos não são permitidas.")
            break

        print("\n=== Menu Operador ===")
        print("Brinquedos disponíveis:")
        for b in parque.brinquedos.values():
            print(f"ID: {b.id_brinquedo} | Nome: {b.nome_brinquedo} | Estado: {b.estado}")

        escolha = input("ID do brinquedo para operar (ou '0' para sair): ")
        if escolha == '0':
            break
        if escolha not in parque.brinquedos:
            print("Brinquedo não encontrado.")
            continue

        brinquedo = parque.brinquedos[escolha]
        print(f"Operando brinquedo: {brinquedo.nome_brinquedo}")
        print("1 - Iniciar")
        print("2 - Parar")
        print("3 - Manutenção")
        print("4 - Reativar")
        opcao = input("Escolha: ")

        if opcao == '1':
            operador.iniciar_brinquedo(brinquedo)
        elif opcao == '2':
            operador.parar_brinquedo(brinquedo)
        elif opcao == '3':
            operador.manutencao(brinquedo)
        elif opcao == '4':
            operador.reativar(brinquedo)
        else:
            print("Opção inválida.")


def menu_bilheteiro(funcionario_bilheteiro):
    while True:
        if not funcionario_bilheteiro.parque.aberto:
            print("Parque fechado. Não é possível vender ingressos no momento.")
            break

        print("\n=== Menu Bilheteiro ===")
        print("1 - Vender ingresso")
        print("2 - Ver caixa")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            funcionario_bilheteiro.vender_ingresso()
        elif opcao == '2':
            funcionario_bilheteiro.bilheteria.ver_caixa()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_barraca(funcionario_barraca):
    while True:
        if not funcionario_barraca.parque.aberto:
            print("Parque fechado. Operações na barraca não são permitidas.")
            break

        barraca = funcionario_barraca.parque.barracas.get(funcionario_barraca.id_barraca)
        if funcionario_barraca._id_func not in barraca.lista_funcionarios:
            print("Funcionário não autorizado para esta barraca.")
            break

        print(f"\n=== Menu Barraca: {barraca.nome_barraca} ===")
        print("1 - Ver estoque")
        print("2 - Registrar venda")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            funcionario_barraca.ver_estoque()
        elif opcao == '2':
            funcionario_barraca.adicionar_itens_venda()
        elif opcao == '0':
            print("Saindo do menu barraca.")
            break
        else:
            print("Opção inválida.")


# ===================== MAIN =====================
def main():
    parque = Parque()

    # Cria gerente padrão para teste
    gerente = GerenteParque("0001", "Gerente Principal", "000.000.000-00", "99999-9999", parque)

    print("Bem-vindo ao sistema do Parque de Diversões!")

    while True:
        usuario, id_barraca = login(parque)
        if usuario is None:
            continue

        if usuario == 'gerencia':
            menu_gerente(gerente)
        elif usuario == 'operador':
            if not parque.aberto:
                print("Parque fechado. Operações de operador não permitidas.")
                continue
            # Pega primeiro operador cadastrado para teste
            operadores = [f for f in parque.funcionarios_parque.values() if isinstance(f, OperadorBrinquedo)]
            if operadores:
                operador = operadores[0]
            else:
                operador = OperadorBrinquedo("op000", "Operador Demo", "", "")
                parque.funcionarios_parque[operador._id_func] = operador
            menu_operador(operador, parque)
        elif usuario == 'bilheteiro':
            if not parque.aberto:
                print("Parque fechado. Operações de bilheteiro não permitidas.")
                continue
            bilheteiros = [f for f in parque.funcionarios_parque.values() if isinstance(f, FuncionarioBilheteiro)]
            if bilheteiros:
                bilheteiro = bilheteiros[0]
            else:
                bilheteiro = FuncionarioBilheteiro("bil000", "Bilheteiro Demo", "", "", parque.bilheteria, parque)
                parque.funcionarios_parque[bilheteiro._id_func] = bilheteiro
                parque.bilheteria.lista_funcionarios[bilheteiro._id_func] = bilheteiro
            menu_bilheteiro(bilheteiro)
        elif usuario == 'tbarraca':
            if not parque.aberto:
                print("Parque fechado. Operações em barraca não permitidas.")
                continue
            funcionarios_barraca = [f for f in parque.funcionarios_parque.values() if isinstance(f, FuncionarioBarraca) and f.id_barraca == id_barraca]
            if funcionarios_barraca:
                funcionario_barraca = funcionarios_barraca[0]  # Pega primeiro funcionário para teste
                menu_barraca(funcionario_barraca)
            else:
                print("Nenhum funcionário cadastrado para esta barraca.")
        else:
            print("Usuário não identificado no sistema.")


if __name__ == "__main__":
    main()
