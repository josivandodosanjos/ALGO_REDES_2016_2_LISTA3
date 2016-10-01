# ALGO_REDES_2016_2_LISTA3todosNumeros = []
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


numeros = list()

for i in range(10):

    numero = int(input('Insira o número:'))

    numeros.append(numero)

    print(numeros)
perguntas = ["Sabe ligar um computador ?",
             "Já trabalhou com o Windows 3.5 ?",
             "Já usou disquete ?",
             "Sabe desligar o computador ?",
             "Sabe programar em python ?"]
soma = 0

for contador in range(5):

    print(perguntas[contador])

    resposta = input("sim ou nao: ")

    if resposta == "sim":
        soma = soma + 1

if soma == 5:
    print("Hacker")

elif soma == 3 or soma == 4:
    print("Sabe alguma coisa")

elif soma == 1:
    print("Sabe de nada, inocente!!!")

else:
    print("Tá aprendendo !!!")
for i in range(10):

    contador_sim = 0
    contador_nao = 0

    respostas = [input("Telefonou para a vítima?"),
                 input("Esteve no local do crime?"),
                 input("Mora perto da vítima?"),
                 input("Devia para a vítima?"),
                 input("Já trabalhou com a vítima?")]

    for resposta in respostas:
        if resposta == 'sim':
            contador_sim = contador_sim + 1
        else:
            contador_nao = contador_nao + 1

    if contador_sim == 5:
        print('ASSASSINO')
        break
    elif contador_sim == 3 or contador_sim == 4:
        print('CUMPLICE')
    elif contador_sim == 2:
        print('SUSPEITO')
    else:
        print('INOCENTE')
