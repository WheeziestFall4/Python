# Nome: Vinicius Rodrigues da Costa Almeida
# RA: 254843
# Descrição: O programa faz uma simulação de uma fabrica de cajuina que realiza 4 processos para que cajus se transformam em cajuina
# O programa organiza as remessas dos cajus em fila e a ordem dos processos. Dessa forma, calcula
# no final a quantidade da cajuinas produzidas por cada remessa colocada.

def classificacao(remessa): # Função que calcula a qtd de cajus que sobra da etapa de classificação

    remessa = remessa * 2 / 3   # o que ira sobrar de cajus da remessa para a proxima etapa
    remessa = int(remessa)

    return remessa  #retorna a remessa resultante do processo de classificação

def pressagem(remessa): # Funcao que calcula a qtd de cajus da remessa que irao virar suco pela etapa de prensagem

    if remessa >= 10:   # Se qtd de cajus da remessa for menor que 10, os cajus rendem 2* mais suco

        remessa = 2 * remessa

    else:               # Se for maior que 10, os cajus passa por um processo de rendimento em 5* mais suco

        remessa = 5 * remessa

    return remessa # retorna a qtd de suco da remessa resultante do processo de pressagem da remessa

def filtragem(remessa): # Funcao que calcula a qtd de suco da remessa que ira sobrar apos a etapa de filtragem

    if remessa > 45: # Se a qtd for maior que 45, 9/10 do suco será perdido

        remessa = remessa * (1/10)

    else: # Se a qtd de suco for menor que 45, apenas 1/9 será perdido

        remessa = remessa * (8/9)

    remessa = int(remessa)

    return remessa # retorna a qtd de suco que sobra da remessa do processo de filtragem

def tratamento(remessa): # Funcao que calcula a qtd de cajuina feita pelo processo de tratamento

    remessa = 2 * remessa #qtd de suco multiplicada por 2 devido a adicao de agua

    return remessa # retorna a qtd de cajuina da remessa feito pelo processo de tratamento.

numeroremessas = 0 # Total de remessas que ira entrar no processo
qtdcadaremessa = [] # Indica que as remessas serão organizadas na forma de lista com nome qtdcadaremessa
processamento = [0, 0, 0, 0] # indica cada processo que as remessas estarao em ordem de chegada
resultado = [] #lista que irá guarda as remessas que passaram por todos os processos
num = 0

numeroremessas = int(input()) # Pede para o usuario a qtd de remessas que irá entrar no processo

for y in range(0, numeroremessas): # Repete o que está dentro do for e vai até atingir a numero de remessas

    qtdcadaremessa.append(input()) # Pede a qtd de cajus de cada remessa
    qtdcadaremessa[y] = int(qtdcadaremessa[y])

    if qtdcadaremessa[y] <= 1: # Se a qtd de cajus da remessa for menor que 2

        print("É necessário pelo menos dois cajus para produção de cajuína!")
        break # Quebra a repetição do for = houve uma remessa com menos de 2 cajus e o processo não poderá ocorrer

if qtdcadaremessa[len(qtdcadaremessa) - 1] > 1: # Se a qtd de cajus da remessa for maior que 1, ocorrerá o processamento

    print("T=" + str(num) + " | " + str(qtdcadaremessa) + " -> " + str(processamento) + " -> " + str(resultado)) # Printa como ficou as remessas antes de entrar no processo e sem entrar no resultado

    while len(qtdcadaremessa) != len(resultado): #Enquanto o tamanho da lista qtdcadaremessa for diferente do tamanho da lista resultado, continua repetindo = significa
# que nem todas as remessas iniciais passarão por todos os resultados
        num = num + 1 # Está incrementando o numero

        for x in range(0, len(qtdcadaremessa)): # For de repetição que passa por todas as posições da qtdcadaremessa

            if qtdcadaremessa[x] != 0: # Se a qtdcadaremessa for diferente de 0, significa que essa remessa é a proxima a entrar no processo de classificação

                processamento[0] = classificacao(qtdcadaremessa[x]) # a posição 0 da lista de processamento (etapa de classificacao) irá receber a remessa da vez.

                qtdcadaremessa[x] = 0 # na posição em que estava a remessa da vez agora passa a ser 0.

                break # Se entrar no if, então o for deve ser quebrado para que os proximos processos possam ocorrer

        print("T="+str(num)+" | "+str(qtdcadaremessa)+" -> "+str(processamento)+" -> "+str(resultado)) # Printa a situação atual de todo processo.

        if processamento[3] != 0: # Se a etapa de Filtragem for diferente de 0

             resultado.append(processamento[3]) # Faz com que a lista resultado receba a remessa que tava no processamento[3]

        processamento[3] = tratamento(processamento[2]) # O processamento[3] da lista processamento irá receber a remessa (que estava no processemento[2] que passou pelo processo de tratamento
        processamento[2] = filtragem(processamento[1]) # O processamento[2] da lista processamento irá receber a remessa (que estava no processemento[1] que passou pelo processo de filtragem
        processamento[1] = pressagem(processamento[0]) # O processamento[1] da lista processamento irá receber a remessa (que estava no processemento[0] que passou pelo processo de pressagem
        processamento[0] = 0 # A remessa que estava aqui agora foi para o processo de prensagem, assim agora no processo[0] ira receber 0.

    print("T=" + str(num+1) + " | " + str(qtdcadaremessa) + " -> " + str(processamento) + " -> " + str(resultado)) # Printa a situação final depois das remessas passarem de todos os processos.



