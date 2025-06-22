from parque import *
from menus import *
from funcionario import *
from login import *
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
                funcionario_barraca = funcionarios_barraca[0]  
                menu_barraca(funcionario_barraca)
            else:
                print("Nenhum funcionário cadastrado para esta barraca.")
        else:
            print("Usuário não identificado no sistema.")


if __name__ == "__main__":
    main()