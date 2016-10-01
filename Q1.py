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