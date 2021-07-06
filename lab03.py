# Nome = Vinicius Rodrigues da Costa Almeida
# RA = 254843

texto1 = """Você apresenta pelo menos 4 dos sintomas principais do COVID-19? (Tosse, febre, dor de garganta, congestão nasal, coriza, dor de cabeça, cansaço, dores pelo corpo)
(1) sim
(2) não"""

texto2 = """Você realizou o teste do COVID-19 desde que esses sintomas surgiram?
(1) não
(2) sim, deu positivo
(3) sim, deu negativo"""

texto3 = """Você se encontra em estado grave de saúde?
(1) sim
(2) não"""

texto4 = """Você se enquadra em um grupo de risco? (gestante; portador de doenças crônicas; problemas respiratórios; fumante; pessoa de extremos de idade, seja criança ou idoso)
(1) sim
(2) não"""

texto5 = """Você entrou em contato recentemente com alguém que foi diagnosticado com o vírus?
(1) sim
(2) não"""

textoerro = "Opção inválida, recomece a avaliação"

print(texto1) # Mostra 1 pergunta
sentiusintomas = int(input()) #Pede o valor para sentir sintomas

if sentiusintomas == 1:             #Opção sim para sentiu sintomas
    print(texto2)  # Mostra 2 pergunta
    fezteste = int(input())  #Pede o valor para fez teste

    if fezteste == 2:               #Opção SIM, DEU POSITIVO para fez teste
        print(texto3)   # Mostra 3 pergunta
        estadodesaude = int(input()) # Pede o valor para estado de saude

        if estadodesaude == 2:      #Opção Não para estado grave
            print(texto4)  # Mostra 4 pergunta
            grupoderisco = int(input()) #Pede o valor para grupo de risco

            if grupoderisco == 1:   #Opção SIM, está em grupo de risco
                print("Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado")
            elif grupoderisco == 2: #Opção Não está em grupo de risco
                print("Baseado em suas respostas, a orientação é que você entre em isolamento")
            else:
                print(textoerro) # Mostra mensagem de erro devido a ter digitado numero diferente

        elif estadodesaude == 1:    #Opção SIM, para estado grave
            print("Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado")
        else:
            print(textoerro)    # Mostra mensagem de erro devido a ter digitado numero diferente
    elif fezteste == 3:            #Opção SIM, DEU NEGATIVO para fez teste
        print("Baseado em suas respostas, a orientação é que você permaneça em distanciamento social")
    elif fezteste ==1:
        print("Baseado em suas respostas, a orientação é que você vá ao hospital para ser testado para o COVID-19")
    else:
        print(textoerro) # Mostra mensagem de erro devido a ter digitado numero diferente

elif sentiusintomas == 2:             #Opção NAO para sentiu sintomas
    print(texto5)   # Mostra 5 pergunta
    contatocomalguem = int(input())   #Pede o valor para contato com alguem
    if contatocomalguem == 1:         #Opção SIM, teve contato com alguem infectado
        print("Baseado em suas respostas, a orientação é que você entre em isolamento")
    elif contatocomalguem ==2:        #Opção NAO, para nao teve contato com alguem infectado
        print("Baseado em suas respostas, a orientação é que você permaneça em distanciamento social")
    else:
        print(textoerro) # Mostra mensagem de erro devido a ter digitado numero diferente

else:
    print(textoerro) # Mostra mensagem de erro devido a ter digitado numero diferente