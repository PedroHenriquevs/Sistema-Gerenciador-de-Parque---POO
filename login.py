def login(parque):
    print("\n======= LOGIN =======")
    print("Cargos disponíveis: gerencia, operador, bilheteiro, <login de barraca>")
    usuario = input("Digite o login: ").strip().lower()
    senha = input("Digite a senha: ").strip()

    
    if usuario in parque.lista_logins:
        if parque.lista_logins[usuario] == senha:
            if not parque.aberto and usuario != 'gerencia':
                print("Parque fechado. Apenas gerência pode acessar o sistema.")
                return None, None
            print(f"Login bem-sucedido como {usuario}!\n")
            return usuario, None
        else:
            print("Senha incorreta!\n")
            return None, None

   
    if usuario in parque.logins_barracas:
        senha_correta, id_barraca = parque.logins_barracas[usuario]

        if senha != senha_correta:
            print("Senha incorreta!\n")
            return None, None

        if not parque.aberto:
            print("Parque fechado. Acesso às barracas bloqueado.")
            return None, None

        barraca = parque.barracas.get(id_barraca)
        if barraca is None:
            print("Barraca não encontrada no sistema.")
            return None, None

        if not barraca.lista_funcionarios:
            print("Nenhum funcionário cadastrado para esta barraca.")
            return None, None

        print(f"Login bem-sucedido como barraca '{usuario}' (ID: {id_barraca})!\n")
        return 'tbarraca', id_barraca

    print("Usuário ou senha incorretos ou não encontrados!\n")
    return None, None
