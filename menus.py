
from barraca import *
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
        print("3- Mostrar Funcionarios")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            funcionario_bilheteiro.vender_ingresso()
        elif opcao == '2':
            funcionario_bilheteiro.bilheteria.ver_caixa()
        elif opcao == '3':
            funcionario_bilheteiro.bilheteria.mostrar_funcionarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")


def menu_barraca(funcionario_barraca):
    while True:
        if not funcionario_barraca.parque.aberto:
            print("Parque fechado. Operações na barraca não são permitidas.")
            break

        barraca = funcionario_barraca.parque.barracas[funcionario_barraca.id_barraca]
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
