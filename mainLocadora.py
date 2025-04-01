def opcaoUser():
    while True:
        try:
            opcao = int(input("Digite sua escolha: "))
            return opcao  
        except ValueError:
            print("Erro! Digite um número válido.")


def subOpcaoUser():
    while True:
        try:
            subopcao = int(input("Digite sua escolha: "))
            return subopcao  
        except ValueError:
            print("Erro! Digite um número válido.")
