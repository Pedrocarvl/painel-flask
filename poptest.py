numeros = [100, 200, 300, 400]

print("Lista original:", numeros)

numeros.pop()        # remove o último: 400
print("Após pop() sem índice:", numeros)

numeros.pop(0)       # remove o primeiro: 100
print("Após pop(0):", numeros)

numeros.pop(1)       # remove o número na posição 1 (agora será o 300)
print("Após pop(1):", numeros)
