# Nome: Vinicius Rodrigues da Costa Almeida
# RA: 254843
# Descrição: Programa lê do usuario os paises que deseja cadastrar e ordena eles de acordo com os criterios desejados pelo usuario (PIB,IDH,OrdemNormal, População e Nome)

def CadastrarPaises(): # Função que cadastra paises, pedindo a qtd de paises desejada e os atributos para cada um deles.

    qtdpaises = input()
    qtdpaises = int(qtdpaises)
    paises = [x for x in range(0,qtdpaises)]

    for y in range(0, qtdpaises): # For que le do usuario os atributos para cada pais e adiciona eles em uma matriz (Cada linha = um pais e seus atributos)

        paises[y] = input().split(" ") # Le do usuario e reconhece cada espaço como um novo atributo de uma lista
        paises[y][1] = int(paises[y][1]) # Posição 1 da lista y = Guarda a População do pais
        paises[y][2] = int(paises[y][2]) # Posição 2 da lista y =  Guarda o PIB do pais
        paises[y][3] = int(paises[y][3]) # Posição 3 da lista y = Guarda longevidade
        paises[y][4] = int(paises[y][4]) # Posição 4 da lista y = Guarda educação
        paises[y][5] = int(paises[y][5]) # Posição 5 da lista y= Guarda renda
        paises[y][6] = int(paises[y][6]) # Posição 6 da lista y = Guarda desigualdade
        paises[y].append(0) # Cria a posição 7 da lista y com valor 0
        paises[y][7] = IDH(paises[y]) # Posição 7 da lista y = Guarda o idh calculado pela função IDH

    return paises # Retorna a lista de todos os paises com seus atributos

def OrdenarCadastro(paises,verificacaodeprint): # Função que ordena os paises pela ordem de cadastro e printa eles.

    result = PrintaOrdem(paises,"Cadastro", verificacaodeprint) # Chama a função printar. Variavel verificacaodeprint verifica se ja foi printado alguma notificacao de erro
    return result # Retorna a verificacaodeprint, Se for TRUE, entao nao poderá mais Printar nada na tela devido ao erro de digitação do atributo

def OrdenarNome(paises, verificacaodeprint): # Função que ordena os paises pela ordem de nomes (Alfebetica) e printa eles.

    Paises = paises.copy() # Copia a lista original paises para outra variavel chamada Paises

    for x in range(0, len(Paises)): # For de repetição que tem como intuito realizar a ordenação por INSERTION SORT

        for y in range(x - 1, -1, -1):

            if Paises[y][0] > Paises[y + 1][0]: # > pois deve ser na ordem alfabetica

                Paises[y + 1], Paises[y] = Paises[y], Paises[y + 1]

    result = PrintaOrdem(Paises,"Nome",verificacaodeprint)
    return result

def OrdenarPopulacao(paises,verificacaodeprint): # Função que ordena os paises pelo numero de população e printa eles.

    Paises = paises.copy()

    for x in range(0, len(Paises)): # For de repetição que tem como intuito realizar a ordenação por INSERTION SORT

        for y in range(x - 1, -1, -1):

            if Paises[y][1] < Paises[y + 1][1]: # < pois deve ser na ordem DECRESCENTE

                Paises[y], Paises[y + 1] = Paises[y + 1], Paises[y]

    result = PrintaOrdem(Paises, "População",verificacaodeprint)
    return result

def OrdenarPib(paises,verificacaodeprint): # Função que ordena os paises pelo numero do PIB e printa eles.

    Paises = paises.copy()

    for x in range(0, len(Paises)): # For de repetição que tem como intuito realizar a ordenação por INSERTION SORT

        for y in range(x - 1, -1, -1):

            if Paises[y][2] < Paises[y + 1][2]: # < pois deve ser na ordem DECRESCENTE

                Paises[y], Paises[y + 1] = Paises[y + 1], Paises[y]

    result = PrintaOrdem(Paises, "PIB",verificacaodeprint)
    return result

def OrdenarIdh(paises, verificacaodeprint): # Função que ordena os paises pelo numero do IDH e printa eles

    Paises = paises.copy()

    for x in range(0, len(Paises)):

        for y in range(x - 1, -1, -1): # For de repetição que tem como intuito realizar a ordenação por INSERTION SORT

            if Paises[y][7] < Paises[y + 1][7]: # < pois deve ser na ordem DECRESCENTE

                Paises[y], Paises[y + 1] = Paises[y + 1], Paises[y]

    result = PrintaOrdem(Paises, "IDH", verificacaodeprint)
    return result

def IDH(pais): # Função que calcula o IDH (pais = lista Paises)
    # idh = ( desigualdade * ( expectativadevida + educação + renda))/3
    idh = int((pais[6] * (pais[3] + pais[4] + pais[5]))/3)

    return idh

def PrintaOrdem(paises,String,verificacaodeprint): # Função que Printa os paises de acordo com a ordem desejada

    if verificacaodeprint != True: # Se a verificaçaodeprint for False, entao quer dizer que não há erro de atributos ou ele ainda não foi identificado

        for x in range(0, len(paises)): # For de repetição que testa os atributos 3,4 e 6 de cada pais e verifica se não estão errados.

            if paises[x][3] <= 0: # Se longevidade for menor ou igual a 0, então printa erro e retorna verificacaodeprint como TRUE

                print("Longevidade fora do intervalo")
                verificacaodeprint = True
                return verificacaodeprint

            elif paises[x][4] < 0 or paises[x][4] > 10: # Se o nivel de educação não for do intervalo entre 0 a 10, entao printa erro e returna verificaçãodeprint como TRUE

                print("Educação fora do intervalo")
                verificacaodeprint = True
                return verificacaodeprint

            elif paises[x][6] < 0 or paises[x][6] > 10: # Se o nivel de desigualdade não for do intervalo entre 0 e 10, entao printa erro e returna verificacaodeprint como TRUE

                print("Desigualdade fora do intervalo")
                verificacaodeprint = True
                return verificacaodeprint

        print("Ordenado por "+String) # Print que avisa qual tipo de ordem esta sendo printado os paises.

        for x in range(0, len(paises)): # Printa Nome, população, Pib e Idh de cada pais
            print(paises[x][0] + " " + str(paises[x][1]) + " " + str(paises[x][2]) + " " + str(paises[x][7]))
        verificacaodeprint = False # returna False avisando que não houve nos atributos dos paises
        return verificacaodeprint

    else:

        verificacaodeprint = True # Estando com erro de atributos (True) entao a variavel verificaçãodeprint deve continuar recebendo TRUE
        return verificacaodeprint

paises = []
opcao = ""
verificacaodeprint = 0

while opcao != "S":

    opcao = input() # Le do usuario qual opcao ele quer escolher para o programa

    if opcao == '1': # Indica que o usuario quer cadastrar paises.

        paises = CadastrarPaises()

    elif opcao == '2': # Indica que o usuario quer ordenar os paises ja cadastrados pela ordem de cadastro original

        verificacaodeprint = OrdenarCadastro(paises, verificacaodeprint)

    elif opcao == '3': # Indica que o usuario quer ordenar os paises ja cadastrados pela ordem alfabetica de nome

        verificacaodeprint = OrdenarNome(paises, verificacaodeprint)

    elif opcao == '4': # Indica que o usuario quer ordenar os paises ja cadastrados pela ordem de População

        verificacaodeprint = OrdenarPopulacao(paises, verificacaodeprint)

    elif opcao == '5': # Indica que o usuario quer ordenar os paises ja cadastrados pela ordem de PIB

        verificacaodeprint = OrdenarPib(paises, verificacaodeprint)

    elif opcao == '6': # Indica que o usuario quer ordenar os paises ja cadastrados pela ordem de IDH

        verificacaodeprint = OrdenarIdh(paises, verificacaodeprint)

    else: # Qualquer outro digito digitado para aqui, entao a opcao é padronizada para S, indicando que o usuario quer sair do programa.
        opcao = "S"