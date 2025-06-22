def login(parque):
    print("\n======= LOGIN =======")
    print("Cargos disponíveis: gerencia, operador, bilheteiro, <login de barraca>")
    usuario = input("Digite o login: ").lower()
    senha = input("Digite a senha: ")

   
    if usuario in parque.lista_logins and parque.lista_logins[usuario] == senha:
        if not parque.aberto and usuario != 'gerencia':
            print("Parque fechado. Apenas gerência pode acessar o sistema.")
            return None, None
        print(f"Login bem-sucedido como {usuario}!\n")
        return usuario, None 

   
    if usuario in parque.logins_barracas and parque.logins_barracas[usuario][0] == senha:
        id_barraca = parque.logins_barracas[usuario][1]
        
        if not parque.aberto:
            print("Parque fechado. Acesso às barracas bloqueado.")
            return None, None
        
        barraca = parque.barracas[id_barraca]
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