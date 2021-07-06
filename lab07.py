# Nome: Vinicius Rodrigues da Costa Almeida
# RA: 254843
# Descrição: Programa faz um mini rpg envolvendo o duelo de dois herois de reinos diferentes. Há uso de cartas que atribui diferentes efeitos nos atributos dos herois.
# O programa define quem será o vencedor quando o max_vida de um deles chegar a 0 após as rodadas de ataques.

def magicas(linha, heroi, heroi_valores_iniciais): # Função Cartas magicas que possui todas as cartas que o jogador pode chamar

    while linha[0] != 'A': #Enquanto o jogador não digitar A, continuará pedindo para digitar novas cartas

        if linha[1] == 'C': #  quando o jogador digitar M C, indicará que ele encontrou a carta Cura

            print(heroi.nome+" encontrou a carta Cura") #Printa que encontrou a carta

            custo = int(linha[2])# Na linha[2] (que recebeu o que foi digitado antes) está atribuido o custo de mana que a carta exige
            pontos = int(linha[3])# Na linha[3] (que recebeu o que foi digitado antes) está atribuido os pontos de vida que a carta vai dar.

            if (heroi.max_mana - custo) >= 0: # Se a subtracao da mana do heroi com o custo for maior ou igual a 0 = há mana suficiente para ativar a carta

                heroi.max_mana = heroi.max_mana - custo # Calcula o que sobrou da mana

                if (pontos + heroi.max_vida) < heroi_valores_iniciais[1]: # Se os pontos adicionado com a vida do heroi for menor que o maximo de vida que ele tinha, entao pode fazer conta

                    heroi.max_vida = heroi.max_vida + pontos # Calcula a vida final apos a ativacao da carta Cura

                else: # Se a soma pontos + vida passar, então a vida do heroi será restaurada ao que era antes

                    heroi.max_vida = heroi_valores_iniciais[1]

            else: # Caso a mana nao for suficiente para ativar a carta, entao entra aqui
                print(heroi.nome+" não possui mana suficiente para a mágica")

        elif linha[1] == 'F':# Quando usuario digitar M F indicara que ele encontrou a carta FORÇA

            print(heroi.nome + " encontrou a carta Força")

            custo = int(linha[2])# Na linha[2] (que recebeu o que foi digitado antes) está atribuido o custo de mana que a carta exige
            pontos = int(linha[3])# Na linha[3] (que recebeu o que foi digitado antes) está atribuido os pontos que a carta pode dar para o dano do heroi

            if (heroi.max_mana - custo) >= 0:# Se o custo subtraido da mana do heroi for maior ou igual 0 = há mana suficiente para ativar a carta

                heroi.dano = heroi.dano + pontos # Dano do heroi eh aumentado
                heroi.max_mana = heroi.max_mana - custo # A mana do heroi eh subtraido do custo

            else: # Caso a mana não for suficiente, entra aqui

                print(heroi.nome + " não possui mana suficiente para a mágica")

        elif linha[1] == 'P': # Se o usuario digitar M P .. indicara que ele encontrou a carta Proteção

            print(heroi.nome + " encontrou a carta Proteção")

            custo = int(linha[2]) # Na linha[2] (que recebeu o que foi digitado antes) está atribuido o custo de mana que a carta exige
            percentual = int(linha[3])# Na linha[3] (que recebeu o que foi digitado antes) está atribuido o porcentual de bloqueio que a carta poderá doar.

            if (heroi.max_mana - custo) >= 0:# Caso a mana for suficiente para ativar a carta entra aqui

                heroi.max_mana = heroi.max_mana - custo # calcula o resto de mana que resulta apos ativar a carta

                if (heroi.bloqueio + percentual) > 100: # Caso a soma do bloqueio do heroi com o percentual foi maior 100, entao o bloqueio deve ser 100 (maximo permitdo)

                    heroi.bloqueio = 100

                else: # Caso a soma do bloqueio do heroi com o percentual for menor que 100, entao podera o bloqueio do heroi será essa soma

                    heroi.bloqueio = heroi.bloqueio + percentual

            else: #Caso não tiver mana suficiente para ativar a carta, printa na tela

                print(heroi.nome + " não possui mana suficiente para a mágica")

        elif linha[1] == 'E':  #Se o usuario digitar M E .... indicará que ele encontrou a carta Eter

            print(heroi.nome + " encontrou a carta Éter")

            pontos = int(linha[2])# Na linha[2] (que recebeu o que foi digitado antes) está atribuido a qtd de pontos de mana que a carta pode dar.

            if (pontos + heroi.max_mana) <= heroi_valores_iniciais[4]: # Se a soma dos pontos com a mana do heroi for menor que mana maxima do heroi, entao pode receber a soma

                 heroi.max_mana = heroi.max_mana + pontos # a mana do heroi eh somado com os pontos

            else: # Caso a soma dos pontos com a mana do heroi passar da mana maxima, entao a mana do heroi será a maxima ja atribuida a ele anteriormente

                 heroi.max_mana = heroi_valores_iniciais[4]

        elif linha[1] == 'D': #Caso o usuario digitar M D ... indicará que ele encontrou a carta Drenagem

            print(heroi.nome + " encontrou a carta Drenagem")
            pontos = int(linha[2]) # Na linha[2] (que recebeu o que foi digitado antes) está atribuido os pontos de mana que o heroi poderá tirar do oponente

            if heroi.cartaDrenagem[0] == 0: # A posicao da cartaDrenagem indica a situacao da carta, assim se for 0, irá indicar que não há nenhuma carta guardado no inventario

                heroi.cartaDrenagem[0] = 2  # O 2 agora indica que na posição da cartaDrenagem do heroi, terá uma carta que foi ativada
                heroi.cartaDrenagem[1] = pontos #Guarda na cartaDrenagem do heroi os pontos de mana que deve ser tirada do oponente a cada ataque

            else: # Caso na posição tiver um numero diferente de 0, entao significa que ele ja possui a carta Drenagem e ela pode estar ativada.
                print(heroi.nome+" já possui a carta Drenagem")

        elif linha[0] == 'I': # Caso o usuario digitar I somente, indicará que ele quer ativar a carta Insano do seu inventario

            if (heroi.max_mana - heroi.cartaInsano[1] >= 0) and heroi.cartaInsano[0] == 1: # Se a mana do heroi for suficiente para o custo da carta e tb se tiver carta no inventario
            # indicada por 1, entao a carta poderá ser ativada

                print(heroi.nome + " ativou a carta Insano")

                heroi.cartaInsano[0] = 2       # O num 2 marca que a carta agora está ativada
                custo = heroi.cartaInsano[1]    # Atribui a variavel custo o custo que tava guardada na posição 1 da carta Insano do heroi
                heroi.max_mana = heroi.max_mana - custo # Calcula o resto de mana que sobra para o heroi apos subtrair o custo

            elif heroi.cartaInsano[0] == 0: # Caso na posição 0 da Carta Insano do heroi estiver 0, entao indica que o inventario esta vazio e ai printa mensagem na tela
                print(heroi.nome + " não possui a carta Insano")

            elif heroi.cartaInsano[0] == 2: #Caso na posição 2 da Carta Insano estiver 2, entao indica que ja há uma carta ativada em ação e ai printa mensagem na tela
                print(heroi.nome + " já ativou a carta Insano")

            else: # Se o heroi nao tiver mana sufienciente para ativar a carta, entao printa mensagem
                print(heroi.nome + " não possui mana suficiente para a mágica")

        elif linha[1] == 'I': # Se o usuario digitar M I .... indicará que ele encontrou e quer guardar a carta Insano no inventario

            print(heroi.nome +" encontrou a carta Insano")

            if heroi.cartaInsano[0] == 0: # Se na posicao 0 da carta Insano do heroi tiver igual a 0, significa que não há nada no inventario e pode guardar a nova carta

                heroi.cartaInsano[0] = 1            # Na posicao 0 da carta Insano vai receber 1 = indicará que agora há uma nova carta no inventario guardada
                heroi.cartaInsano[1] = int(linha[2])# Na linha[2] (que recebeu o que foi digitado antes) está atribuido o custo de mana que a carta exige para ser ativada
                heroi.cartaInsano[2] = int(linha[3])# Na linha[3] (que recebeu o que foi digitado antes) está atribuido a qtd de especiais da carta q ira durar apos ser ativada
                heroi.cartaInsano[3] = int(linha[4])# Na linha[4] (que recebeu o que foi digitado antes) está atribuido o dano adicional que a carta pode dar apos ativada.
                #Todos os valores foram atribuidos a cartaInsano.
            else:    # Se na posicao 0 da carta Insano do heroi tiver igual a 1 ou 2, entao printa que ja possui a carta Insano no inventario.
                print(heroi.nome + " já possui a carta Insano")

        elif linha[0] == 'S': #Caso o usuario digitar S somente,indicara que ele quer ativar a carta Estrela do seu inventario

            if (heroi.max_mana - heroi.cartaEstrela[1]) >= 0 and heroi.cartaEstrela[0] == 1: # Caso a mana for suficiente para ativar a carta e na posicao 0 da carta Estrela
        # tiver 1, entao quer dizer que a carta pode ser ativada
                print(heroi.nome + " ativou a carta Estrela")

                heroi.cartaEstrela[0] = 2                # O numero 2 marca a carta como ativa
                custo = heroi.cartaEstrela[1]            # A variavel custo recebe o custo de mana que a carta Estrela tava guardando
                heroi.max_mana = heroi.max_mana - custo # Calcula a qtd de mana que restou

            elif heroi.cartaEstrela[0] == 0:            # Se tiver 0 na posicao 0 da cartaEstrela, entao indica que nao ha carta armazenada no inventario
                print(heroi.nome + " não possui a carta Estrela")

            elif heroi.cartaEstrela[0] == 2:    # Se tiver 2 na posicao 0 da cartaEstrela, entao indica que ja ha uma carta ativada no inventario

                print(heroi.nome + " já ativou a carta Estrela")

            else:
                print(heroi.nome + " não possui mana suficiente para a mágica")

        elif linha[1] == 'S': #Caso o usuario digitar M S ... indicara que ele encontrou e esta tentando guardar uma carta Estrela

            print(heroi.nome +" encontrou a carta Estrela")

            if heroi.cartaEstrela[0] == 0: #Se na posição 0 da cartaEstrela estiver 0, entao indicara que nao ha carta guardada no inventario e assim pode guardar a encontrada

                heroi.cartaEstrela[0] = 1                  # Vai receber 1 para indicar que há uma cartaEstrela no inventario
                heroi.cartaEstrela[1] = int(linha[2])      # Na linha[2] (que recebeu o que foi digitado antes) está atribuido o custo de mana que a carta exige
                heroi.cartaEstrela[2] = int(linha[3])      # Na linha[3] (que recebeu o que foi digitado antes) está atribuido a qtd de especiais que carta ira durar

            else:   # Se na posicao 0 da cartaEstrela tiver um numero diferente de 0, logo indica que ja ha uma carta no inventaria ou que ja esta ativada uma carta
                print(heroi.nome + " já possui a carta Estrela")

        elif linha[1] == 'X': # Caso o usuario digitar M X entao indicara que ele nao encontrou nenhuma carta
            print(heroi.nome+" não encontrou nenhuma carta")

        linha = input().split(" ") # Pede de novo uma nova carta que encontrou ou quer usar ou um ataque com o digito A
        linha.insert(len(linha),0) # Impede que a linha fica somente com posicao 0 e que acabe dando erro nos ifs

class Heroi: # Classe Heroi para atribuir atributos para um heroi e a ação de atacar
    def __init__(self,nome, max_vida, dano, bloqueio,max_mana): # Metodo da classe para atribuir atributos para um novo heroi
        self.nome = nome
        self.max_vida = max_vida
        self.dano = dano
        self.bloqueio = bloqueio
        self.max_mana = max_mana
        self.cartaDrenagem = [0,0] # posicao 0 - situacao da carta, posicao 1 - qtd de mana tirada do oponente
        self.cartaInsano = [0,0,0,0]  # posicao 0 - situacaodacarta, posicao 1 - custo, posicao 2 - qtddeespeciais, posicao 3 - danoadicional
        self.cartaEstrela = [0,0,0]  #posicao 0 - situacaocarta, posicao 1 - custo, posicao 2 - qtddeespeciais

# Nas cartas, a posicao 0 indica a situacao da carta:
    # 0 - Nao há carta no inventario
    # 1 - Indica que há uma carta guardada
    # 2 - Indica que a carta guardada foi ativada

    def __str__(self): # Metodo da classe Heroi para printar seus atributos
        return(self.nome+" possui "+str(self.max_vida)+" de vida, "+str(self.max_mana)
              +" pontos mágicos, "+str(self.dano)+" de dano e "+str(self.bloqueio)+
              "% de bloqueio")

    def ataque(self,oponente): # Metodo da classe Heroi que faz o calculo da qtd dano tirada no ataque baseado nos efeitos das cartas ativadas

        if (self.cartaInsano[2] > 0) and self.cartaInsano[0] == 2: # Se a qtddeespeciais da cartaInsano for maior que 0 e a cartaInsana tiver ativada (indicada por 2)

            if oponente.cartaEstrela[0] != 2: # Se a carta Estrela nao foi ativada, entao havera dano insano no oponente sem ele estar invulneravel

                print(self.nome+" deu um ataque insano em "+oponente.nome)

                danocomespecial = self.dano + self.cartaInsano[3] #Calcula o dano total com o dano adicional da carta Insano
                dano_recebido = danocomespecial - int((danocomespecial * oponente.bloqueio) / 100) #Calcula o dano recebido descontando o dano bloqueado

                if (oponente.max_vida - dano_recebido) > 0: # Caso a vida oponente menos o dano for maior que 0, entao pode receber todo o dano
                    oponente.max_vida = oponente.max_vida - dano_recebido
                else: # Se a vida do oponente menos o dano pode dar negativo, entao ele a vida dele eh apenas zerada
                    oponente.max_vida = 0

                self.cartaInsano[2] = self.cartaInsano[2] - 1   # Esta tirando 1 da qtddeespeciais da carta Insano

                if self.cartaInsano[2] == 0: # Se qtd de especiais da carta Insano for igual a 0, entao nao ha mais cartaInsano no inventario
                    self.cartaInsano[0] = 0

            elif oponente.cartaEstrela[0] == 2 and (oponente.cartaEstrela[2] > 0): # Se a carta  Estrela do oponente estiver ativada e a qtd de especiais da carta for maior q 0 entao

                print(self.nome+" deu um ataque insano em "+oponente.nome)
                print(oponente.nome+" estava invulnerável")
                oponente.cartaEstrela[2] = oponente.cartaEstrela[2] - 1 # Esta tirando 1 da qtddeespeciais da carta estrela
                self.cartaInsano[2] = self.cartaInsano[2] - 1  # Esta tirando 1 da qtddeespeciais da carta Insano

                if self.cartaInsano[2] == 0: # Se a qtddeespeciais da carta Insano acabar, logo deve sinalizar com 0 que nao ha mais cartaInsano no inventario
                    self.cartaInsano[0] = 0

                if oponente.cartaEstrela[2] == 0: # Se a qtddeespeciais da carta Estrela do oponente acabar, logo deve sinalizar com 0 que nao ha mais cartaEstrela no Inventario
                    oponente.cartaEstrela[0] = 0

        else: # Se a cartaInsano nao tiver ativada, entao entra aqui

             if oponente.cartaEstrela[0] != 2: # Se a carta Estrela nao tiver ativada tb

                print(self.nome+" atacou "+oponente.nome)

                dano_recebido = self.dano - int((self.dano * oponente.bloqueio) / 100) # Calcula o dano recebido sem adicionais e descontando o bloqueio

                if (oponente.max_vida - dano_recebido) > 0: # Se a vida do oponente menos o dano recebido for maior que 0, entao pode o oponente pode receber todo o dano
                    oponente.max_vida = oponente.max_vida - dano_recebido
                else: # Se o dano recebido for maior que a vida atual do oponente, entao a vida dele vai ser apenas zerada
                    oponente.max_vida = 0

             elif oponente.cartaEstrela[0] == 2 and oponente.cartaEstrela[2] > 0: # Se a carta Estrela do oponente estivar ativada e a qtd de especiais for maior que 0, entao a carta ta ativada

                 print(self.nome + " atacou " + oponente.nome)
                 print(oponente.nome + " estava invulnerável")
                 oponente.cartaEstrela[2] = oponente.cartaEstrela[2] - 1 # Esta tirando 1 da qtddeespeciais da carta Estrela do oponente

                 if oponente.cartaEstrela[2] == 0: # Se a qtd de especiais da carta Estrela do oponente for igual a 0, entao deve indicar com 0 a situacao da carta
                    oponente.cartaEstrela[0] = 0  #O 0 ira indicar que nao mais carta Estrela no inventario do oponente

        if heroi.cartaDrenagem[0] == 2: # Se a situacao da carta Drenagem foi igual a 2, entao quer dizer que há a carta esta ativada

            oponente.max_mana = oponente.max_mana - heroi.cartaDrenagem[1]  #Tira parte da mana do oponente devido ao ataque

            if oponente.max_mana < 0: # Se a mana do oponente menos os pontos tirados  for menos que 0, entao a mana do oponente sera apenas zerada
                oponente.max_mana = 0

# Heroi [ Nome, Maximo Vida, Dano, Bloqueio, Maximo Mana]
Heroi1_valores_iniciais = [0,0,0,0,0] # Guarda os atributos originais do heroi 1
Heroi2_valores_iniciais = [0,0,0,0,0] # Guarda os atributos originais do heroi 2
num = 1 # Indica o numero de ataques houve no total
rodada = 1 # Indica numero de rodadas que teve

Heroi1_valores_iniciais[0] = input() # Pede o primeiro valor a ser guardada na variavel heroi1 valores iniciais =  deve ser o nome

for x in range(1, 5): # For percorre as posicoes  1 ao 4 pedindo seus atributos
    Heroi1_valores_iniciais[x] = input() # Le os atributos digitados em ordem
    Heroi1_valores_iniciais[x] = int(Heroi1_valores_iniciais[x]) # Transforma eles de string para int

heroi1 = Heroi(Heroi1_valores_iniciais[0],Heroi1_valores_iniciais[1],Heroi1_valores_iniciais[2],Heroi1_valores_iniciais[3],Heroi1_valores_iniciais[4]) #Atribui os atributos no objeto heroi11

print("O reino Snowland indicou o herói "+heroi1.nome)

Heroi2_valores_iniciais[0] = input() # Pede o primeiro valor a ser guardada na variavel heroi2 valores iniciais =  deve ser o nome

for x in range(1,5): # For percorre as posicoes  1 ao 4 pedindo seus atributos
    Heroi2_valores_iniciais[x] = input() # Le os atributos digitados em ordem
    Heroi2_valores_iniciais[x] = int(Heroi2_valores_iniciais[x]) # Transforma eles de string para int

heroi2 = Heroi(Heroi2_valores_iniciais[0],Heroi2_valores_iniciais[1],Heroi2_valores_iniciais[2],Heroi2_valores_iniciais[3],Heroi2_valores_iniciais[4]) # Atribuir os atributos no objeto heroi 2

print("O reino Sunny Kingdom indicou o herói "+heroi2.nome)

while heroi1.max_vida != 0 and heroi2.max_vida != 0: # Enquanto a vida dos dois for diferente de zero, continua a repetição de rodadas

    linha = input().split(" ") # Le a proximo elemento para continuar a batalha
    linha.insert(len(linha), 0) # Impede que a lista linha fica com apenas uma posicao 0 e dê problema nos if seguintes

    if linha[1] == '1': # Se o heroi que começar for o 1, entao as variaveis da luta ira receber seus atributos e idenficar os atributos do seu oponente

        heroi = heroi1
        heroi_valores_iniciais = Heroi1_valores_iniciais
        oponente = heroi2
        oponente_valores_iniciais = Heroi2_valores_iniciais

    else:  # Se o heroi que começar for o 2, entao as variaveis da luta ira receber seus atributos e idenficar os atributos do seu oponente
        heroi = heroi2
        heroi_valores_iniciais = Heroi2_valores_iniciais
        oponente = heroi1
        oponente_valores_iniciais = Heroi1_valores_iniciais

    print("Rodada " + str(rodada) + ": vez de " + heroi.nome)
    linha = input().split(" ") # Le do usuario a proxima acao (no caso a magica) que deve ocorrer apos indicar o heroi que ira atacar
    linha.insert(len(linha), 0) # Impede que a lista linha fica com apenas uma posicao 0 e dê problema nos if seguintes
    magicas(linha, heroi, heroi_valores_iniciais) # envia os dados lidos para a funcao magica e assim reconhecar qual carta foi usada
    heroi.ataque(oponente) # indica o ataque do heroi

    if num % 2 == 0 and num != 0: # Se o resto de num dividido por 2 der 0, entao quer dizer que acabou a rodada e pode printar
        print(heroi1)
        print(heroi2)
        num = num + 1
        rodada = rodada + 1 # guarda o numero da rodada e incrementa a cada rodada
    else:
        num = num + 1 # Incrementa a variavel num indicando o n de ataques que ocorreu

if heroi2.max_vida == 0: # Se a vida do heroi2 for igual a 0 entao, entao printa que heroi 1 ganhou

    print("O herói " + str(heroi1.nome) + " do reino Snowland venceu o duelo")

else: # Se a vida do heroi1 for igual a 0 entao, entao printa que heroi 2 ganhou
    print("O herói " + heroi2.nome + " do reino Sunny Kingdom venceu o duelo")
# Printa atributos finais.
print(heroi1)
print(heroi2)