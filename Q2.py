todosNumeros = []
par = []
impar = []

for contador in range(20):
    numero = int(input("Digite um número: "))

    todosNumeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Par:", par)
print("Impar:", impar)
print("Todos numeros:", todosNumeros)
