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