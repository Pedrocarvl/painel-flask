#Lista de nomes
nomes = []

#Função para cadastrar nomes
def cadastrar_nome():
    nome = input("Insira o nome a ser cadastrado: ")
    nomes.append(nome)
    print(f"Nome '{nome}' cadastrado com sucesso")

#Função para cadastrar nomes
def listar_nomes():
    if not nomes:
        print("Não há nomes cadastrados!")
    else:
        print("\n--- Lista de nomes ---")
        for i, nome in enumerate(nomes, 1):
            print(f"{i}. {nome}")
        
#Função para remover um nome
def remover_nome():
    listar_nomes()
    nome = input("Digite num nome que gostaria de remover: ")
    if nome in nomes:
        nomes.remove(nome)
        print(f"Nome '{nome}' removido com sucesso!")
    else:
        print("Nome não encontrado no sistema!")

#Menu principal
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Remover nome")
    print("4 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_nome()
    elif escolha == "2":
        listar_nomes()
    elif escolha == "3":
        remover_nome()
    elif escolha == "4":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida!")
        