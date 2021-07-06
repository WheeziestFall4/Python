# Nome: Vinicius Rodrigues da Costa Almeida         RA: 254843
# Descrição: Programa lê um dicionario de sinonimos de palavras do usuario, uma pergunta qualquer como texto e suas possiveis respostas.
# Após isso, ele faz diversos procedimentos nas respostas e na pergunta para depois poder achar a unica resposta certa para essa pergunta.
# Os procedimentos tem como intuito separar os textos em palavras chaves

from PontStop import*

def Padronização(texto): # Função que faz o que todo texto recebido fique em minusculo

    texto = texto.lower()
    return texto

def Tokenização(texto): # Função que separa as palavras do texto em uma lista

    final = len(texto)
    novotexto = []
    inicio = -1

    for x in range(0, len(texto)):  # For de repetição que indentifica o inicio e o fim das palavras pelo espaço entre elas
                                    # e faz a separação colocando as palavras em uma nova lista
        if texto[x] == " ":
            novotexto.append(texto[inicio + 1:x])
            inicio = x

    novotexto.append(texto[inicio + 1:final])

    return novotexto

def Limpeza(novotexto):     # Funcao que faz a limpeza do texto, ou seja, tira pontuações e palavras desnecessarias no texto.

    for x in range(0, len(novotexto)):  # For de repetição que substitui as pontuações de dentro da lista recebida em espaço vazios.

        for pontuacao in pontuacoes:    # As possiveis pontuacoes que devem ser substituidas estao na biblioteca PontStop e devem ser percorridas por estrutura de Repetição

            novotexto[x] = novotexto[x].replace(pontuacao, "")

    tamanho = len(novotexto)

    for x in range(0, tamanho): # For de repetição que percorre o toda a lista recebida

        for palavrainuteis in stop_words: # For que percorre as palavras que são consideradas inuteis pela biblioteca StopWords

            try:    # Tenta remover as palavras inuteis

                    novotexto.remove(palavrainuteis)

            except:  # Caso determinadas palavra inutil não estiver, ao inves de dar erroValue, pode continuar a percorrer as outras palavras

                    continue

    listafinal = novotexto

    return listafinal

def Reescrita(novalista, dicionario):   # Função de reescrita que troca as palavras sinonimos pelo seu valor chave.

    for key, value in dicionario.items(): # For que permite percorrer as chaves e os respectivos valores do dicionario

        for valor in value: # For que percorre as palavras que estao dentro de cada valor na forma de lista

            for x in range(0, len(novalista)): # For de repetição que percorre a lista texto recebida pela função

                if novalista[x] == valor:   # Se a palavra da lista recebida ser igual a um das palavras dentro de um valor no dicionario, entao pode remover essa palavra
                                            # e trocar pelo seu sinonimo chave
                    novalista.remove(novalista[x])
                    novalista.insert(0,key)

    return novalista

def Representacao(listafinal): # Função que retira todas as palavras repetidas que estiver no texto lista

    conjunto = set()
    lista = []

    for x in range(0, len(listafinal)): # For de repeticao que adiciona todas as palavras (dentro da lista recebida) para um conjunto

        conjunto.add(listafinal[x])

    # O conjunto retira as repetições por conta propria visto que se trata de um conjunto, dessa forma, se passarmos para uma lista novamente, não haverá mais repetições.

    for palavra in conjunto: # For de repeticao que adiciona as palavras do conjunto para uma nova lista desde que não seja uma string vazia.

        if palavra != "":

            lista.append(palavra)

    return lista


dicionariosinonimos = {} # Variavel que declara um novo dicionario para os sinonimos que o usuario irá digitar
representante = ""
sinonimo = []   # Lista que armazenerá os sinonimos lidos do usuario de forma temporaria
sinonimo2 = []  # Lista que realiza a transferencia para o dicionario

palavra = input() # Lê do usuario o {
palavra = input() # Lê do usuario a primeira lista de sinonimos e a palavra chave do novo dicionario

while palavra != "}": # Enquanto o usuario nao digitar }, entao continue a pedir novos sinonimos e palavras chaves

     sinonimo.insert(0, []) # Insere uma nova lista na posição 0, consequentemente, as outras listas de sinonimos são empurradas para posicoes posteriores

     for x in range(0, len(palavra)): # For de repetição que percorre a string digitada pelo usuario, buscando a palavra chave

         if palavra[x] == ":": # Se a string de determinada posicao tiver :, entao quer dizer que eh o fim da palavra CHAVE

            representante = palavra[0:x] # Atribui á variavel representante a palavra CHAVE
            break

     inicio = x

     for l in range(x, len(palavra)): # For de repetição que percorre o resto da string digitada procurando os sinonimos da palavra CHAVE

         if palavra[l] == ",": # Se tiver uma virgula, entao quer dizer que há uma nova palavra de sinonimos na STRING

             sinonimo[0].insert(0, palavra[inicio + 1:l]) # Insere na posiçao 0 da posição 0 da lista sinonimos a nova palavra.
             inicio = l

     sinonimo[0].insert(0, palavra[inicio + 1:len(palavra)]) # Insera a ultima palavra sinonimos na posicao 0 da posicao 0 da lista sinonimos
     sinonimo2.insert(0,sinonimo[0]) # Insere em uma nova lista a lista que está na posicao 0 da lista sinonimos
     dicionariosinonimos[representante] = sinonimo2[0] # Atribui a palavra Chave e o valor lista do dicionario
     palavra = input()

pergunta = input()
qtdrespostas = input()
qtdrespostas = int(qtdrespostas)
respostas = []  # As respostas digitadas serão armazenas em uma lista respostas
descricaoresposta = [] # Lista que armazenará a descricao resposta
respostafinal = ""

for x in range(0, qtdrespostas): # For de repetição que le do usuario cada resposta possivel e armazena elas na lista respostas

    respostas.append(input())
    descricaoresposta.append(0)

descricaopergunta = set(Representacao(Reescrita(Limpeza(Tokenização(Padronização(pergunta))),dicionariosinonimos))) # Recebe a pergunta apos ter passados por todas as funçoes de reorganização
print("Descritor pergunta: "+",".join(sorted(descricaopergunta))) # Printa a descricao da pergunta (resultado da pergunta apos ter passado pelas funcoes)

for x in range(0, len(respostas)): # Percorre cada resposta da lista resposta

    descricaoresposta[x] = set(Representacao(Reescrita(Limpeza(Tokenização(Padronização(respostas[x]))),dicionariosinonimos))) # Recebe cada resposta apos ter passado por todas as funcoes de reorganização
    print("Descritor resposta "+str(x+1)+": "+",".join(sorted(descricaoresposta[x])))

    if descricaopergunta.issubset(descricaoresposta[x]) == True: # Se determinada descricaoresposta estiver contida no conjunto pergunta, entao eh considerada como resposta final

        respostafinal = respostas[x]

    elif respostafinal == "" and descricaopergunta.issubset(descricaoresposta[x]) == False : # Se resposta final ainda for vazia e a descricao resposta nao tiver contida na descricao pergunta,
                                                                                            # entao a resposta final será 42
        respostafinal = '42'

print('')
print('A resposta para a pergunta "'+pergunta+'" é "'+respostafinal+'"') # Printa a pergunta e a sua respectiva resposta final.