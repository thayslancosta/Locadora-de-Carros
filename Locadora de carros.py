from operacoesbd import *
from mainLocadora import *

conn = criarConexao ("127.0.0.1","root","12345","locadoracarros")

#Menu principal
while True:
    print(
        "Bem-vindo à locadora Unifacisa! \n"
        "Opções: \n"
        "1) Gestão de carros \n"
        "2) Gestão de clientes\n"
        "3) Gestão de aluguéis \n"
        "4) Sair \n"
        )
    #Usuário digita a opção
    opcao = opcaoUser()
    
    #Submenu de gestão de carros
    if opcao == 1:
        print(
            "\n1) Listar carros disponíveis\n"
            "2) Cadastrar um novo carro\n"
            "3) Pesquisar carro por placa\n"
            "4) Atualizar um carro\n"
            "5) Remover um carro\n"
            "6) Informar a quantidade de carros disponíveis"
            )
        #Usuário digita a opção
        subopcao = subOpcaoUser()
        
        #Listagem de carros cadastrados
        if subopcao == 1:
            consultaListaCarros = "SELECT modelo FROM carros "
            listaCarros = listarBancoDados(conn,consultaListaCarros)

            if len(listaCarros  ) > 0:
                print("Lista de Filmes:")
                
            for item in listaCarros :
                print(f"- {item[1]} ({item[3]})")
            else:
                print("Não há carros cadastrados.\n")

        #Cadastrar novo carro -- Campos obrigatórios: modelo / fabricante / ano / placa / preço da diária
        if subopcao == 2:

             #User informa fabricante
            while True:
                novoFabricante = input("Digite o fabricante do carro a ser adicionado: ")
                if len(novoFabricante) == 0:
                    print("Fabricante inválido!")
                else:
                    break
                       
            #User informa modelo
            while True:
                novoModelo = input("Digite o modelo do carro a ser adicionado: ")
                if len(novoModelo) == 0:
                    print("Modelo inválido!")
                else:
                    break

            #User informa o ano do carro
            while True:
                try:
                    novoAno = int(input("Digite o ano do carro: "))
                    break
                except ValueError:
                    print("O ano informado é inválido!")

            #User informa placa
            while True:
                novaPlaca = input("Digite a placa do carro a ser adicionado: ")
                novaPlaca.strip().upper().replace("-","")
                
                if len(novaPlaca) == 0:
                    print("Placa informada é inválida!")
                else:
                    break

            #User informa o preço da diária do carro
            while True:
                try:
                    novoPreco = (input("Digite o valor da diária do carro: R$")).replace(",",".")
                    novoPreco = float(novoPreco)
                    break
                except ValueError:
                    print("O valor informado é inválido!")
            
            #Inserir novo carro no banco de dados:
            consultaInsert = "INSERT INTO carros (modelo, fabricante, ano, placa, preco_diaria) values (%s, %s, %s, %s, %s)"
            dados = [novoModelo, novoFabricante, novoAno, novaPlaca, novoPreco]

            #informar id do carro
            idCarro = insertNoBancoDados(conn, consultaInsert, dados)

            #Feedback para o user:
            print(f"Carro cadastrado com sucesso! O código de cadastro é {idCarro}\n"
                  f"Modelo: {novoModelo}\n"
                  f"Fabricante: {novoFabricante}\n"
                  f"Ano: {novoAno}\n"
                  f"Placa: {novaPlaca}"
                  f"Valor da diária: R${novoPreco}"                  
                  )

        if subopcao == 3:
            while True:
                try:
                    userPlacaInformada = input("Informe a placa a ser buscada (ou digite 0 para retornar ao menu): ").strip().replace("-","").upper()
                    if userPlacaInformada == "0":
                        break

                    consultaPlaca = "SELECT * FROM carros WHERE placa LIKE %s"
                    consultaUser = listarBancoDados (conn, consultaPlaca, [userPlacaInformada])

                    if consultaUser:
                        carroConsultado = consultaUser [0]
                        print("Carro encontrado com sucesso!\n"
                              f"{carroConsultado[2]} {carroConsultado[1]}\n"
                              f"Ano: {carroConsultado[3]}\n"
                              f"Placa: {carroConsultado[4]}\n"
                              f"Status: {carroConsultado[5]}\n"
                              f"Valor da diária: R${carroConsultado[6]}\n")
                        break
                    else:
                        print("Placa não encontrada!")
                
                except Exception as e:
                    print(f"Erro ao buscar placa: {e}")

    if opcao == 4:
        break

    encerrarConexao(conn)