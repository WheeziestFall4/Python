# Nome: Vinicius Rodrigues da Costa Almeida
# RA: 254843
# Descrição: Programa que simula um jogo da vida no qual o jogador deve colocar(em um plano 2D) peças que representam celulas vivas no meio de varias mortas e analisar suas interações ao longo do tempo.
# O programa le do usuario qual eh a ordem do tabuleiro(M * N), a quantidade de celulas vivas que deve ter e suas coordenadas e tambem a quantidade de interações que ira fazer.
# Apos isso, organiza as interações entre as celulas vivas e mortas seguindo as seguintes regras:
#       1 - Celula que tem menos de 2 vizinhos = morre por solidão
#       2 - Celula que tem mais de 3 vizinho = morre por superpopulação
#       3 - Celula que tem 3 vizinho = passa a viver novamente
#       4 - Outra qtd de vizinhos = a celula continua a mesma

def printartabuleiro(tabuleiro,linhas,colunas): # Função que printa na tela o tabuleiro quando requisitado

    for x in range(0, linhas):  # For de repetição que percorre as linhas
        for y in range(0, colunas): # For de repetição que percorre as colunas
            print(tabuleiro[x][y],end='')

        print("")
    print("-")


linhas = input()  # Le do usuario qual eh a qtd de linhas que o tabuleiro deve ter
colunas = input()   # Le do usuario qual eh a qtd de colunas que o tabuleiro deve ter
qtdinterações = input()     # Le do usuario a qtd de interações entre as celulas que deve ter
qtdcelulas = input()    # Le do usuario a qtd de celulas vivas que ira colocar no tabuleiro
tabuleiro = []  # Inicia o tabuleiro como vazio
tabuleiroreserva = []   # Tabuleiro reserva que serve para fazer a troca das celulas
numcelulasproxima = 0   # Variavel que armazena a qtd de celulas vivas que esta proxima de uma celula especifica

# Transformam as variaveis lidas como string para INT
linhas = int(linhas)
colunas = int(colunas)
qtdinterações = int(qtdinterações)
qtdcelulas = int(qtdcelulas)
numero = 0  # Numero que determina a qtd de repetições que deve ter na hora de fazer interação

# Ambos os FOR faz com que o tabuleiro inicie todo com celulas mortas
for n in range(0, linhas):
    tabuleiro.append(["."])         # Forma as linhas
    tabuleiroreserva.append(["."])

for n in range(0, linhas):
    for l in range(0 ,colunas - 1):
        tabuleiro[n].append(".")    # Forma as colunas com celulas mortas
        tabuleiroreserva[n].append(".")

for n in range (0, qtdcelulas):     # FOR de repetição que coloca as celulas vivas no tabuleiro
    x,y = input().split(",")        # Pede as coordenadas da celula vida que deve colocar no tabuleiro
    x = int(x)                      # Transforma a coordenada linha para int
    y = int(y)                      # Transforma a coordenada coluna para int
    tabuleiro[x][y] = "+"           # Coloca o valor + no tabuleiro nas coordenadas pedidas

printartabuleiro(tabuleiro,linhas,colunas) # Chama a função printar para mostrar na tela o tabuleiro inicial antes da interação

# Vocabularios seguinte:
# - Celula referencia : celula que esta sendo analisada  no momento
while numero != qtdinterações: # While de repetição que realiza interações até chegar no limite desejado pelo usuario

    for x in range(0, linhas): # For de repetição que percorre todas as linhas da matriz

        for y in range(0, colunas): # For de repetição que percorre, dentro de cada linha, todas as colunas

            if x < linhas - 1: # Se a posicao em que x (linha) está for menor que a ultima posição entao pode continuar = Senao poderia dar erro de lista fora de alcance

                if tabuleiro[x + 1][y - 1] != "." and y > 0: # Se a celula posicionado embaixo a esquerda em relacao a celula referencia for viva e
                                                                # a celula referencia nao estivar nas beiradas. entao continue
                    numcelulasproxima += 1                      # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

                if tabuleiro[x + 1][y] != ".":  # Se a celula posicionada embaixo da celula referencia for viva entao continue

                    numcelulasproxima += 1  # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

            if x < linhas - 1 and y < colunas - 1:    # Se a posicao em que x (linha) e y (coluna) estão for menores que a ultima posicao deles, entao continue = Para nao dar erro de lista fora de alcance

                if tabuleiro[x + 1][y + 1] != ".":  # Se a celula posicionada embaixo a direita em relação a celula referencia for viva, entao continue

                    numcelulasproxima += 1      # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

            if y < colunas - 1:        # Se a posicao em que y (coluna) está for menor que a ultima posicao entao pode continuar = Para nao dar erro de lista fora de alcance

                if tabuleiro[x - 1][y + 1] != "." and x > 0:   # Se a celula de cima da direita em relação a celula referencia for viva e a celula referencia nao estiver nas beiradas, entao continue

                    numcelulasproxima += 1      # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

                if tabuleiro[x][y + 1] != ".":      # Se a celula a direita da celula referencia for viva entao pode continuar

                    numcelulasproxima += 1  # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

            if tabuleiro[x - 1][y - 1] != "." and x > 0 and y > 0:    # Se a celula de baixo a esquerda em relação a celula referencia for viva e a celula referencia nao estiver nos cantos, entao continue

                numcelulasproxima += 1  # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

            if tabuleiro[x - 1][y] != "." and x > 0:   # Se a celula posiciona em cima da celula referencia for viva e a celula referencia nao estiver nas beiradas entao continue

                numcelulasproxima += 1  # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

            if tabuleiro[x][y - 1] != "." and y > 0:   # Se a celula da esquerda em relação a celula referencia for viva e a celula nao estiver nas beiradas entao continue

                numcelulasproxima += 1  # Soma +1 a qtd de celulas vivas que estao proximas da celula referencia

            if numcelulasproxima < 2 or numcelulasproxima > 3:  # Por fim, se numero de celulas vivas proximas for menor que 2 ou maior que 3, entao a celula referecia morre

                tabuleiroreserva[x][y] = "."

            elif numcelulasproxima == 3:    # Por fim, se numero de celulas vivas proximas for igual a 3, entao a celula ficará viva

                tabuleiroreserva[x][y] = "+"
            else:                           # Se a qtd de celulas vivas for 2 , entao a celula referencia continua do mesmo jeito de antes
                tabuleiroreserva[x][y] = tabuleiro[x][y]

            numcelulasproxima = 0   # Reinicia a variavel numero de celulas proximas como 0 para ser reutilizada na proxima analise de outra celula.

    printartabuleiro(tabuleiroreserva,linhas,colunas)   # Printa o tabuleiro apos a interação

    for n in range(0,linhas):           # For de repetição que percorre as linhas
        for h in range(0, colunas):     # For de repetição que percorre as colunas
            tabuleiro[n][h] = tabuleiroreserva[n][h]        # Atribui todos valores guardados no tabuleiro reservado para o verdadeiro tabuleiro

    numero += 1  # Incrementa +1 para indicar que houve mais uma interação ja feita