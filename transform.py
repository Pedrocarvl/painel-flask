def transformar_numero(numero):
    if numero % 2 == 0:
        return numero * 2, "par"
    else:
        return numero * 3, "impar"

#Inserir
valor = int(input("Insira o número: "))
resultado, tipo = transformar_numero(valor)
print (f"O valor informado é {tipo}, e o resultado é {resultado}")
