# Nome: Vinicius Rodrigues da Costa Almeida RA: 254843
# Descricao: Programa simula um jogo de trapaça no qual o jogador (bot) deve pegar cartas do mesmo tipo da carta alvo escolhida na rodada
# e o outro jogador (outro bot) deve adivinhar se o jogador esta blefando ou nao.
# Dependendo da situacao, um dos jogadores fica com tudo da pilha. Ganha aquele que ficar sem cartas.

class jogadorbot(): # Classe jogadores que possue os atributos que o jogador deve ter.

    def __init__(self, mao, duvidaoponente, maodesordenada, pilhaatual = []):

        self.cartasmao = mao
        self.cartamaosemordenar = maodesordenada # Guarda o baralho antes de ordenar (na pratica, guarda o baralho na forma alfabetica)
        self.blefou = "" # Guarda a informação se o jogador bot blefou ou nao

        if pilhaatual == ['']: # Se a variavel que o usuario digitou for igual um espaço vazio, entao o programa registra como '', o deve ser alterado.

            self.pilhaatual = [] # Altera para uma lista vazia e nao como um espaço a ser guardado.

        else:

            self.pilhaatual = pilhaatual

        self.duvidaoponente = duvidaoponente # Guarda se o usuario duvidou ou nao do oponente

    def verificacartaalvo(self, cartaalvorodada): # Funcao que verifica se o tipo da carta alvo esta contida na mao do jogador

        self.cartasdesordenada() # Desordena a variavel self.cartamaodesordenada e coloca em ordem alfabetica
        esquerda = 0
        direita = len(self.cartamaosemordenar) - 1
        cartaalvo = cartaalvorodada
        resultado = []

        while esquerda <= direita: # Laço de repetição que faz uma busca binaria

            posicaomeio = ((esquerda + direita)//2)

            if self.cartamaosemordenar[posicaomeio][0] == cartaalvo[0]: # Se encontrar carta do mesmo tipo da carta alvo, entao busca se no lado dessa carta existe outras do mesmo tipo

                resultado.append(self.cartamaosemordenar[posicaomeio])
                self.blefou = "N"

                for x in range(posicaomeio + 1, posicaomeio + 4, +1): # Procura cartas (que tem o mesmo tipo) do lado direito da carta encontrada

                    try: # Como se procura 3 posicoes (lado direito) apos a carta encontrada, entao o try/except evite que dê erro de lista fora de tamanho caso a lista terminar.

                        if self.cartamaosemordenar[x][0] == cartaalvo[0]:

                            resultado.insert(len(resultado) - 1, self.cartamaosemordenar[x])

                    except: # Caso nao tiver mais posições a direita da carta encontrada, entao o laço de repeticao vai ser quebrado

                        break

                for y in range(posicaomeio - 1, posicaomeio - 4, -1):  # Procura cartas (que tem o mesmo tipo) do lado esquerda da carta encontrada

                    try: # Como se procura 3 posicoes (lado esquerdo) apos a carta encontrada, entao o try/except evite que dê erro de lista fora de tamanho caso a lista terminar.

                        if self.cartamaosemordenar[y][0] == cartaalvo[0] and (posicaomeio - 1 + y) >= 0:

                            resultado.insert(len(resultado) - 1, self.cartamaosemordenar[y])
                    except: # Caso nao tiver mais posições a esquerda da carta encontrada, entao o laço de repeticao vai ser quebrado

                        break

                resultado = self.ordenamao(resultado) # Guarda todos resultados encontrados de cartas compativeis na variavel resultado
                self.pilhaatual.extend(resultado) # Devido ao descarte de cartas pelo jogador bot, entao a pilha aumenta e ha a retirada dessas cartas da mao do jogador
                self.removecartas(self.cartasmao,resultado)
                self.cartasmao = self.ordenamao(self.cartasmao)
                return resultado

            elif self.cartamaosemordenar[posicaomeio][0] < cartaalvo[0]:

                self.blefou = "S"
                esquerda = posicaomeio + 1

            elif self.cartamaosemordenar[posicaomeio][0] > cartaalvo[0]:

                self.blefou = "S"
                direita = posicaomeio - 1

        self.cartasmao = self.ordenamao(self.cartasmao) # Ordenada a cartasmao

        resultado.append(self.cartasmao[0]) # Se a funcao ainda nao retornou, entao nao ha cartas compativeis a carta alvo e deve se pegar cartas da primeira posicao da mao do jogador

        for x in range(1, 4): # For de repeticao que verifica se há outras cartas do mesmo tipo daquela pegada da primeira posicao

            try:

                if self.cartasmao[x][0] == self.cartasmao[0][0]:

                    resultado.append(self.cartasmao[x])

            except:

                break

        self.pilhaatual.extend(resultado)
        self.removecartas(self.cartasmao,resultado)
        self.cartasmao = self.ordenamao(self.cartasmao)
        return resultado

    def imprimiresultadojogada(self,resultadoverificacarta): # Imprime o resultado de acordo com a escolha que o jogador bot e o outro bot fizeram

        # A variavel duvidaoponente verifica se o oponente duvidou ou nao e a variavel blefou registra se o jogador bot blefou ou nao

        print("Jogada: "+" ".join(resultadoverificacarta))

        if self.duvidaoponente == "S" and self.blefou == "S": # Nesse caso, como o jogador blefou e o outro duvidou, entao o jogador recebe toda a pilha

            print("Um bot adversário duvidou")
            print("O bot estava blefando")
            lista = self.pilhaatual.copy()
            self.cartasmao.extend(lista)
            self.cartasmao = self.ordenamao(self.cartasmao)
            self.pilhaatual = []
            print("Mão: "+" ".join(self.cartasmao))
            print("Pilha: "+" ".join(self.pilhaatual))

        elif self.duvidaoponente == "N" and self.blefou == "S": # Nesse caso, como o jogador blefou mas o outro nao duvidou, entao nenhum dos dois recebe a pilha

            print("Nenhum bot duvidou")
            print("Mão: " + " ".join(self.cartasmao))
            print("Pilha: "+" ".join(self.pilhaatual))
            self.venceu()

        elif self.duvidaoponente == "S" and self.blefou == "N": # Nesse caso, como o jogador nao blefou mas o outro duvidou, entao o outro recebe a pilha ( Contudo, nao ha necessidade de mostrar a outra mao)

            print("Um bot adversário duvidou")
            print("O bot não estava blefando")
            self.pilhaatual = []
            print("Mão: " + " ".join(self.cartasmao))
            print("Pilha: "+" ".join(self.pilhaatual))
            self.venceu()

        else: # Nesse caso, ninguem duvidou e nem blefou, as cartas continuam na pilha

            print("Nenhum bot duvidou")
            print("Mão: " + " ".join(self.cartasmao))
            print("Pilha: "+" ".join(self.pilhaatual))
            self.venceu()

    def ordenamao(self, lista): # Funcao que ordena a mao conforme a ordem A,2,3,4,5,6,7,8,9,10,J,Q,K

        posicao = 0

        for x in range(0, len(lista)): # Forma de ordenação do tipo INSERTION SORT

            for y in range(x - 1, -1, -1):

                if lista[y] > lista[y + 1]:

                    lista[y], lista[y + 1] = lista[y + 1], lista[y]

                if lista[y][0] == "K" and lista[y + 1][0] == "Q": # No caso de ter K e Q, entao a ordem deles deve ser mudado para Q K

                    lista[y], lista[y + 1] = lista[y + 1], lista[y]

        y = 0

        for x in range(0, len(lista)): # Coloca as cartas A no inicio do baralho

            if lista[x][0] == "A":
                mudanca = lista[x]
                lista.remove(lista[x])
                lista.insert(y, mudanca)
                y += 1

        for x in range(0, len(lista)): # Procura aonde começa as cartas alfabeticas com exceção do A

            if lista[x][0] == 'J' or lista[x][0] == "Q" or lista[x][0] == "K":
                posicao = x # Registra a posicao que começa as cartas alfabeticas (J,K OU Q)
                break

        for h in range(0, posicao):  # Forma de ordenação do tipo INSERTION SORT para as cartas que começam com 10, colocando elas na posição correta

            for z in range(h - 1, -1, -1):

                if lista[z][0] == '1': # Se a carta começar com 1 entao

                    if int(lista[z][:2]) > int(lista[z + 1][0]):

                        lista[z], lista[z + 1] = lista[z + 1], lista[z]

                if lista[z][0] == '1' and lista[z + 1][0] == '1':

                    if lista[z][2] > lista[z + 1][2]:

                        lista[z], lista[z + 1] = lista[z + 1], lista[z]

        return lista

    def removecartas(self, lista, remover): # Função que remove uma lista de cartas de acordo com o que o usuario pedir e de qual baralho

        for x in range(0, len(remover)):

            try:

                lista.remove(remover[x])

            except:

                continue

    def venceu(self): # Função que verifica se o jogador bot venceu a rodada ou nao, caso vencer deve printar uma mensagem

        if self.cartasmao == []:

            print("O bot venceu o jogo")

    def cartasdesordenada(self): # Função que ordena as cartas de forma alfabetica para facilicar na hora de realizar uma possivel busca binaria

        for x in range(0, len(self.cartamaosemordenar)):

            for y in range(x - 1, -1, -1):

                if self.cartamaosemordenar[y] > self.cartamaosemordenar[y + 1]:

                    self.cartamaosemordenar[y], self.cartamaosemordenar[y + 1] = self.cartamaosemordenar[y + 1], self.cartamaosemordenar[y]


cartasmao = list(input().split(" ")) # Le as cartas que estarão na mao do jogador bot e coloca elas em uma lista
pilha = list(input().split(" ")) # Le as cartas que estarão na pilha e coloca elas em uma lista
cartaalvo = input() # Le o tipo de carta que deve ser buscado na mao do jogador bot
duvidou = input() # Le se o outro jogador duvidou ou nao do jogador bot

jogador = jogadorbot(cartasmao,duvidou,cartasmao,pilha)
jogador.cartasmao = jogador.ordenamao(jogador.cartasmao)
resultado = jogador.verificacartaalvo(cartaalvo)
jogador.imprimiresultadojogada(resultado)
