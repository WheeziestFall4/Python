# Nome = Vinicius Rodrigues da Costa Almeida
# RA = 254843
# Descrição = Cria um codigo secreto a partir de uma mensagem e um polinomio ambos em binario.
# O programa faz comparação entre a mensagem e o polinomio por meio de XOR e assim cria um codigo.

mensagem = list(input())
polinomio = list(input())

p = 0 # Posição da lista mensagem deve começar com 0

for x in range(0,len(polinomio) - 1): # Adicionando 0 a direita da lista mensagem
    mensagem.append('0')

qtdcomparacoes = len(mensagem) - len(polinomio) + 1  # Calcula a qtd de vezes que deve haver comparacao

for n in range(0, qtdcomparacoes): # Repete o que esta dentro do for até atingir quantidade de vezes que tem q comparar polinomio com mensagem

    l = 0                               # Faz com que volte a 0 a posição da lista polinomio

    if not (mensagem[p] == '0' and polinomio[0] == '1'):    # Caso não ocorrer o caso mensagem = 0 e polinomio = 1,faz a mudança da lista mensagem.

        for x in range(p, p+len(polinomio)):         # Faz a mudança da mensagem até percorrer todo polinomio

            if mensagem[x] == polinomio[l]:
                 mensagem[x] = '0'
            else:
                 mensagem[x] = '1'

            l = l +1 #Esta aumentando a posicao do vetor do polinomio de 0 até o tamanho do polinomio toda vez

    p = p + 1 # Está aumentando a posição da mensagem em uma unidade +1, assim no proximo for, o polinomio irá comparar com a posição da mensagem mais +1 a direita.

for x in range(qtdcomparacoes,len(mensagem)): # For para printar apenas o codigo que está no vetor mensagem
    print(mensagem[x],end="") # Permite printar sem os [ ]

print()










