def dobrar_num(valor):
    if valor % 2 == 0:
        return valor * 2
    else:
        return valor * 3

def verificar(valor):
    if valor % 2 == 0:
        return "par"
    else:
        return "ímpar"
    

#MENU
while True: 
    print ("\n--- MENU ---")
    print ("1 - Dobrar número")
    print ("2 - Verificar par ou ímpar")
    print ("3 - Sair")
    
    escolha = input("Escreva o número:  ")

    if escolha == "1":
        valor = int(input("Escreva o número: "))
        resultado = dobrar_num(valor)
        print (f"O resultado do cálculo de {resultado}")

    elif escolha == "2":
       valor = int(input("Escreva o número: "))
       tipo = verificar(valor)
       print (f"O valor inserido é {tipo}")

    elif escolha == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")