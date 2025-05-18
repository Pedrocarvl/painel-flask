def dobrar_onumero(numero):
    return numero * 2

#Local do input para inserir o numero
valor = int(input("Digite o número: "))
resultado = dobrar_onumero(valor)
print (f"O dobro de {valor} é o {resultado}")