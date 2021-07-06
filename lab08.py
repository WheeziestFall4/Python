# Nome: Vinicius Rodrigues da Costa Almeida RA:254843
# Descrição: Programa que gerencia a solicitação e entrega do auxilio emergencial que está em vigor no Brasil em 2020 para pessoas de baixa renda
# Detalhes: Programa cadastra novos beneficiarios, além do usuario poder fazer transferencia, solicitar auxilio e imprimir seus dados. Além disso,
# o programa permite que o governo possa acessar os novos beneficiarios, gerenciar a receita e a entrega do auxilio

class Beneficiario: # Classe beneficiarios que permite criar objeto com atributos de beneficiario

    def __init__(self, nome="", sobrenome = "", cpf="", rendapercapita = 0, rendatotal = 0, idade = 0, emprego=""): # registra os atributos que o objeto beneficiario pode ter
        self.nome = nome                # Nome do novo beneficiario
        self.sobrenome = sobrenome      # Sobrenome do novo beneficiario
        self.cpf = cpf                  # CPF do novo beneficiario
        self.status = "Perfil incompleto"   # Atribui, assim que criar um objeto inicial, o status de inicio sera Perfil Incompleto
        self.rendapercapita = rendapercapita   # Renda per capita do novo beneficiario
        self.rendatotal = rendatotal    # Renda Total do novo beneficiario
        self.idade = idade              # Idade do novo beneficiario
        self.emprego = emprego          # Emprego do novo beneficiario pode ser Desempregado(a), Autonomo(a) e Microempreendedor(a)
        self.tempoderecebimento = 0     # Tempo em meses (1 a 3) que o novo beneficiario ira receber caso for aprovado o auxilio.
        self.saldo = 0                  # Guarda o dinheiro do auxilio caso o novo beneficiario for aprovado

    def solicitar_beneficio(self): # Metodo da classe que faz a solicitação do beneficio para o beneficiario ja registrado

        if self.status == "Perfil completo": # Se o status estiver como Perfil Completo, entao pode iniciar a solicitacao do beneficio

            self.status = "Pendente" # Muda o status do beneficiario para Pendente pois foi enviado a solitacao para analise
            governo.beneficios_pendentes.append(self) #Envia o objeto beneficiario que pediu a solicitacao para o metodo que faz a analise
            print("Auxílio solicitado, aguarde avaliação")

        elif self.status == "Perfil incompleto": # Caso o status estiver Perfil Incompleto, significa que o beneficiario nao preencheu todos os dados e assim nao pode pedir auxilio,
            print("Complete seu perfil e tente novamente")

    def receber_beneficio(self): # Metodo da classe que faz o recebimento do auxilio daqueles beneficiarios que tiveram o auxilio aprovado

            self.saldo += 600       # adiciona 600 no saldo do beneficiario
            self.tempoderecebimento+= 1 # Adiciona +1 no tempo de recebimento significando que falta menos meses para ele receber todo o auxilio.

            if self.tempoderecebimento == 3:    #Caso o tempo de recebimento chegar a 3, entao muda o status para Finalizado visto que ele ja recebeu todo o auxilio possivel

                self.status = "Auxílio finalizado"
            else: #Caso, o tempo ainda for menor que 3 , entao o status continua sendo Com Auxilio

                self.status = "Com auxílio"

    def transferir_beneficio(self, numconta): # Metodo da classe que permite o beneficiario transferir o dinheiro do seu saldo para uma conta corrente

            dinheiro = self.saldo # Uma nova variavel ira receber a copia do saldo que o beneficiario possui
            self.saldo = 0  # Zera o saldo que o beneficiario tinha =  significa que houve a transferencia
            print("Valor de R$ {:.2f}".format(dinheiro)+" transferido para a conta corrente "+str(numconta)) # Imprime o dinheiro que foi retirado e o num da conta que recebeu

    def imprimir_nome(self): # Metodo da classe que imprime na tela o NOME do beneficiario que pedir

        print("Nome completo: "+self.nome+" "+self.sobrenome)

    def imprimir_status(self): # Metodo da classe que imprime na tela o STATUS do beneficiario que pedir

        print("Status: "+self.status)

    def imprimir_cpf(self): # Metodo da classe que imprime na tela o CPF do beneficiario que pedir

        print("CPF: "+self.cpf)

    def imprimir_informacoes(self): # Metodo da classe que imprime na tela TODOS OS DADOS do beneficiario que pedir

        print("Nome completo: "+self.nome+" "+self.sobrenome+
                 "\nStatus: "+self.status+"\nCPF: "+self.cpf+"\nRenda per capita: R$ {:.2f}".format(self.rendapercapita)+
                 "\nRenda total: R$ {:.2f}".format(self.rendatotal)+
                 "\nIdade: "+str(self.idade)+"\nEmprego: "+self.emprego+
                 "\nTempo de recebimento: "+str(self.tempoderecebimento)+" meses")

    def inserir_nome(self, nome): # Metodo da classe que insere um nome para o objeto que foi criado na MAIN principal

        sobrenome = ""

        for x in range(0, len(nome)): # For de repetição que procura qual parte da lista nome começa o sobrenome
            if nome[x] == " ":          # Se na lista nome tiver espaço, entao significa que as proximas posições estarão o nome
                sobrenome = nome[x+1 : ]    # Define qual parte da lista nome ira ser o sobrenome (PROCESSO DE SLICE) = variavel sobrenome recebe
                nome = nome[ : x]           #Define qual parte da lista nome será o nome principal (PROCESSO DE SLICE) = variavel nome recebe
                break           # Significa que nao precisa mais percorrer o resto da lista visto que ja achou o ponto do inicio do sobrenome

        self.nome = nome # Atribui o nome principal para o beneficiario
        self.sobrenome = sobrenome  #Atribui o sobrenome para o beneficiario
        print("Nome inserido")

    def inserir_cpf(self , cpf): #Metodo da classe que insere um CPF para o objeto que foi criado na MAIN principal

        Cpf = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'] # Inicia a variavel com valores padrão

        for x in range(0, len(cpf)): # For de repeticao que faz a lista Cpf receber os valores da string cpf enviado
            Cpf[x] = cpf[x]

        if Cpf[3] != '.': # Se na posição 3 da lista Cpf não tiver o ponto que representa o CPF brasileiro, entao adiciona esse ponto
            Cpf.insert(3, '.') # Insere o ponto na posicao 3 na lista
            del Cpf[len(Cpf) - 1] #retira 0 do final que surge devido a funcao insert

        if Cpf[7] != '.': # Se na posição 7 da lista Cpf não tiver o ponto que representa o CPF brasileiro, entao adiciona esse ponto
            Cpf.insert(7, '.')  # Insere o ponto na posicao 7 na lista
            del Cpf[len(Cpf) - 1]   #retira 0 do final que surge devido a funcao insert

        if Cpf[11] != '-':  # Se na posição 11 da lista Cpf não tiver a barra que representa o CPF brasileiro, entao adiciona esse ponto
            Cpf.insert(11, '-') # Insere o ponto na posicao 11 na lista
            del Cpf[len(Cpf) - 1]   # retira 0 do final que surge devido a funcao insert

        self.cpf = "".join(Cpf) # Converte a lista Cpf em string e atribui ela ao beneficiario objeto
        print("CPF inserido")

    def inserir_renda_per_capita(self, renda): # Metodo da classe que insere a renda per capita para o objeto beneficiario

        self.rendapercapita = renda # Atribui a renda per capita para o beneficiario objeto
        print("Renda per capita inserida")

    def inserir_renda_total(self, rendatotal): # Metodo da classe que insere a renda total para o objeto beneficiario

        self.rendatotal = rendatotal # Atribui a renda total para o beneficiario objeto
        print("Renda total inserida")

    def inserir_idade(self, idade): # Metodo da classe que insere a idade para o objeto beneficiario

        self.idade = idade # Atribui a idade para o beneficiario objeto
        print("Idade inserida")

    def inserir_emprego(self, emprego): # Metodo da classe que insere o emprego para o objeto beneficiario

        self.emprego = emprego # Atribui o emprego para o beneficiario objeto
        print("Emprego inserido")

    def mudarstatus(self): # Metodo da classe que muda o status do beneficiario caso ele completar todos os dados

        if self.nome != "" and self.sobrenome != "" and self.cpf != "": # Caso os dados forem diferentes dos valores padrões atribuidos,
                                                                        # entao atribui status do beneficiario como Perfil Completo
            if self.idade != 0:

                if self.emprego != "":

                    self.status = "Perfil completo"


class Governo(Beneficiario): # Classe Governo que permite criar objeto com atributos de Governo, tambem pode utilizar os atributos do Beneficiario como classe filha

    def __init__(self): # Metodo inicial da classe que atribui os atributos para um objeto
        self.beneficios_concedidos = [] # Atributo que guarda os beneficios que foram aprovados e nao sao mais pendentes
        self.recursos_disponiveis = 0   # Atributo que guarda o dinheiro que ira ser utilizado para dar o auxilio
        self.beneficios_pendentes = []   # Atributo que guarda os beneficios que devem ser analisados

    def avaliar_beneficiarios_pendentes(self): # Metodo da classe que avalia as solicitacoes de auxilio que os beneficiarios registrados mandaram

        for x in range(0, len(self.beneficios_pendentes)): # For de repetição que percorre todos os objetos beneficiarios dentro da lista beneficios pendentes e avalia se cada um deve receber ou nao o auxilio

            if self.beneficios_pendentes[x].idade >= 18:

                if self.beneficios_pendentes[x].rendapercapita <= 522.50 or self.beneficios_pendentes[x].rendatotal <= 3135.00 :

                    if self.beneficios_pendentes[x].emprego == "desempregado" or self.beneficios_pendentes[x].emprego == "desempregada" or self.beneficios_pendentes[x].emprego == "autonomo" or self.beneficios_pendentes[x].emprego == "autonoma" or self.beneficios_pendentes[x].emprego == "microempreendedora" or self.beneficios_pendentes[x].emprego == "microempreendedor":

                        self.beneficios_concedidos.append(self.beneficios_pendentes[x]) # O objeto que for aprovado entao ira ser incluido na lista Beneficios Concedidos
                        self.beneficios_concedidos[len(self.beneficios_concedidos)-1].status = "Com auxílio" # O objeto que for aprovado muda seu status para "Com Auxilio"
                    else:
                        self.beneficios_pendentes[x].status = "Negado" # Coloca o status do objeto como negado =  nao cumpruiu todos os requisitos
                else:
                    self.beneficios_pendentes[x].status = "Negado" # Coloca o status do objeto como negado =  nao cumpruiu todos os requisitos
            else:
                self.beneficios_pendentes[x].status = "Negado" # Coloca o status do objeto como negado =  nao cumpruiu todos os requisitos

        print("Beneficiários avaliados")
        print("Lista de beneficiários atualizada")

    def adicionar_recursos(self, quantia): # Metodo da classe que adiciona mais dinheiro aos recursos de um objeto

        self.recursos_disponiveis += quantia # adiciona o valor enviado (quando o metodo foi chamado) para o deposito recursos
        print("Recursos adicionados")

    def imprimir_recursos_disponiveis(self): # Metodo da classe que imprime na tela o dinheiro disponivel para o auxilio

        print("Recursos disponíveis: R$ {:.2f}".format(self.recursos_disponiveis))

    def imprimir_beneficiarios_atuais(self): # Metodo da classe que imprime na tela o CPF, o NOME E SOBRENOME dos beneficiarios que sao contemplados pelo auxilio

        print("Beneficiários atuais:")

        for x in range (0, len(self.beneficios_concedidos)): # For de repetição que percorre todos os objetos dentro da lista beneficios concedidos e imprime eles

            if self.beneficios_concedidos[x].status != "Auxílio finalizado": # Se os beneficiarios ja tiverem recebido todo o auxilio, entao nao sao imprimidos na tela

                print(self.beneficios_concedidos[x].cpf+": "+self.beneficios_concedidos[x].nome+" "+self.beneficios_concedidos[x].sobrenome)

    def enviar_auxilio_mensal(self): # Metodo da classe que envia o auxilio a todos os beneficiarios que foram aprovados para receber

        num = 0

        for x in range (0, len(self.beneficios_concedidos)): #For de repetição que percorre todos os beneficiarios objetos que foram aprovados para receber o auxilio

            if self.recursos_disponiveis - 600 >= 0 and self.beneficios_concedidos[x].tempoderecebimento <= 3: # Se ainda haver recurso e o beneficiario nao ter recebido os 3 meses de auxilio
                                                                                                                # Entao recebe auxilio
                self.beneficios_concedidos[x].receber_beneficio() # Chama funcao da classe Beneficiario que organiza o recebimento do auxilio
                self.recursos_disponiveis -= 600 # retira - 600 do dinheiro total do governo
                num += 1 # Incrementa +1 na variavel num ate acabar o for

            elif (self.recursos_disponiveis - 600) < 0: # Se o dinheiro do governo nao for suficiente, entao para o for e imprime Recursos Insuficientes
                print("Recursos insuficientes")
                break # Para o for

        if num == len(self.beneficios_concedidos): # Se num for igual ao tamanho da lista, entao quer dizer que percorrer todo a lista beneficios concedidos e imprime que enviou o auxilio
            print("Auxílio mensal enviado")


x = 0
beneficiario = [] # Lista beneficiario que ira armazenar todos os objetos beneficiarios
numanterior = 0 #
governo = Governo() # Cria um objeto governo que ira ter atributos da classe Governo

escolha = ""    # inicia a variavel escolha (que escolhe qual usuario ira entrar no programa) como vazia
escolha = input()
escolha = escolha.lower() # Tudo que for lido será transformado em minusculo

while escolha != 'x': # Enquanto a escolha nao for X, o programa ira continuar funcionando

    if escolha != "governo": # Se escolha for diferente de governo, as opcoes serao voltados para BENEFICIARIOS

        if escolha == "beneficiario" or escolha == "beneficiário": # Se escolha tiver somente BENEFICIARIO, entao quer criar um novo usuario

            beneficiario.insert(len(beneficiario),0) # Adiciona um valor na posicao final da lista beneficiario para que nao haja erro
            beneficiario[x] = Beneficiario() # Atribui que na posicao x ira receber um novo objeto da classe beneficiario
            pessoa = beneficiario[x] # variavel pessoa recebe o objeto que ta dentro da lista beneficiario na posicao X
            x = x + 1 # incrementa o X para que o proxima objeto, se for criado, esteja na proxima posição

        else: # Se a escolha tiver BENEFICIARIO mais algo, entao quer chamar um beneficiario ja criado

            num = 0

            cpf = escolha[13:] # Pega a parte da string digitada (escolha) que eh os digitos do cpf

            Cpf = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'] # Cria lista Cpf com valores padrão

            for x in range(0, len(cpf)): # For de repetição que copia os valores da string para outra lista
                Cpf[x] = cpf[x]

            if Cpf[3] != '.': # Se na posição 3 da lista não tiver o ponto tipico de CPF então insere ele
                Cpf.insert(3, '.')
                del Cpf[len(Cpf) - 1] # Remove o valor da ultima posição ( eh igual a 0)

            if Cpf[7] != '.': # Se na posicao 7 da lista não tiver o ponto tipico de CPF entao insere ele
                Cpf.insert(7, '.')
                del Cpf[len(Cpf) - 1] # Remove o valor da ultima posicao (eh igual a 0)

            if Cpf[11] != '-': # Se na posição 11 da lista não tiver a barra tipico do CPF entao insere ele
                Cpf.insert(11, '-')
                del Cpf[len(Cpf) - 1] # Remove o valor da ultima posicao (eh igual a 0)

            cpf = "".join(Cpf) # Transforma a lista Cpf em string e armazena na variavel cpf

            for i in range(0, len(beneficiario)): # For de repetição que percorre a lista de objetos beneficiarios

                if cpf == beneficiario[i].cpf: # Se encontrar um objeto beneficiario que tiver com o mesmo CPF do que foi digitado na busca entao entra

                    pessoa = beneficiario[i] # a variavel pessoa recebe o objeto beneficiario que foi encontrado
                    break # Quebra o laço de repetição visto que ja encontrou o beneficiario com mesmo CPF

        opcao = ""         # Reinicia a variavel opcao com valor vazio para não dar problema na hora de digitar a opcao novamente
        opcao = input()    # Le a opcao desejada pelo usuario

        while opcao != 'F': # Enquanto opcao for diferente de F, entao o usuario pode continuar escolhendo mais opcoes

            if opcao[0] == "1" and opcao[1] == " ":   # Se for digitado 1 e espaço , ai quer dizer que o usuario quer inserir um novo nome

                nome = opcao[2:]       # Depois do espaço vazio na posicao 1, o resto que foi digitado eh o nome e sobrenome do usuario
                nome = nome.upper()      # Coloca a string nome como maiuscula
                pessoa.inserir_nome(nome)  # Transfere a variavel nome para a funcao inserir nome poder atribuir o nome do beneficiario
                pessoa.mudarstatus()        # Testa se todos atributos necessarios foram atribuidos. Se foram ai muda o status para Perfil Completo

            elif opcao[0] == "2":       # Se for digitado 2, entao quer dizer que o usuario quer inserir um novo cpf

                cpf = opcao[2:]         # Depois do espaço, toda a string da variavel opcao sera os digitos do cpf
                pessoa.inserir_cpf(cpf) # envia o valor da variavel cpf para a funcao que atribui o CPF do beneficiario
                pessoa.mudarstatus()    # Testa se todos atributos necessarios foram atribuidos. Se foram, ai muda o status para Perfil Completo

            elif opcao[0] == "3":       # Se for digitado 3, entao quer dizer que o usuario quer inserir uma nova renda per capita

                renda = opcao[2:]       # Depois do espaço, toda a string da variavel opcao sera os digitos da renda per capita
                renda = float(renda)    # Transforma a renda lida como string para float.
                pessoa.inserir_renda_per_capita(renda)      # Envia o valor da variavel renda para a funcao que atribui a renda per capita do beneficiario
                pessoa.mudarstatus()      # Teste se todos atributos necessarios foram atribuidos. Se foram, ai muda o status para Perfil Completo

            elif opcao[0] == "4":       # Se for digitado 4, entao quer dizer que o usuario quer inserir um nova renda total

                rendatotal = opcao[2:]      # Depois do espaço, toda a string da variavel opcao sera os digitos da renda total
                rendatotal = float(rendatotal)      # Transforma a renda lida como string para float
                pessoa.inserir_renda_total(rendatotal)      # Envia o valor da variavel renda total para a funcao que atribui a renda total do beneficiario
                pessoa.mudarstatus()        # Testa se todos os atributos necessarios foram atribuidos; Se foram, ai muda o status para Perfil Completo

            elif opcao[0] == "5":       # Se for digitado 5, entao quer dizer que o usuario quer inserir uma nova idade.

                idade = opcao[2:]       # Depois do espaço, toda a string da variavel opcao sera os digitos da renda total.
                idade = int(idade)      # Transforma a idade lida com string para int
                pessoa.inserir_idade(idade)         # Envia o valor da variavel idade para a funcao que atribui a idade do beneficiario
                pessoa.mudarstatus()        # Testa se todos os atributos necessarios foram atribuidos. Se foram, ai muda o status para Perfil Completo

            elif opcao[0] == "6":       # Se for digitado 6, entao quer dizer que o usuario quer inserir um novo emprego

                emprego = opcao[2:]     # Depois do espaço, toda a string da variavel opcao sera os digitos do emprego
                emprego = emprego.lower()       # Transforma o valor da string emprego para minuscula
                pessoa.inserir_emprego(emprego)   # Envia o valor da variavel emprego para a funcao que atribui o emprego do beneficiario
                pessoa.mudarstatus()            # Teste se todos os atributos necessarios foram atributos. Se foram, ai muda o status para Perfil Completo

            elif opcao[0] == "7":       # Se for digitado 7, entao quer dizer que o usuario quer solicitar o beneficio do auxilio

                pessoa.solicitar_beneficio()    # Função da classe Beneficiario que analisa se o usuario pode solicitar o auxilio ou nao

            elif opcao[0] == "8":       # Se for digitado 8, entao quer dizer que o usuario quer solicitar transferencia do auxilio para uma conta.

                numconta = opcao[2:]    # Depois do espaço, toda a string da variavel opcao sera os digitos da conta que o dinheiro sera transferido
                numconta = int(numconta)        # Transforma o num conta que foi lido com string para int.
                pessoa.transferir_beneficio(numconta)        # Funcao da classe Beneficiario que transfere o auxilio para uma conta

            elif opcao[0] == "9":       # Se for digitado 9, entao quer dizer que o usuario quer imprimir o nome seu na tela

                pessoa.imprimir_nome()      # Funcao da classe Beneficiario que imprimi o nome do beneficiario na tela.

            elif opcao[0] == "1" and opcao[1] == "0":       # Se for digitado 1 e depois 0, entao quer dizer que o usuario quer imprimir o status seu na tela.

                pessoa.imprimir_status()    # Funcao da classe Beneficiario que imprimi o status do beneficiario na tela

            elif opcao[0] == "1" and opcao[1] == "1":       # Se for digitado 1 e depois 1, entao quer dizer que o usuario quer imprimir o CPF seu na tela

                pessoa.imprimir_cpf()       # Funcao da classe Beneficiario que imprimir o CPF do beneficiario na tela

            elif opcao[0] == "1" and opcao[1] == "2":   # Se for digitado 1 e depois 2, entao quer dizer que o usuario quer imprimir todos os seus dados na tela

                pessoa.imprimir_informacoes()   # Funcao da classe Beneficiario que imprimi todos os dados na tela

            opcao = ""          # Reinicia a variavel opcao como vazio
            opcao = input()     # Le a nova opcao digitada

    else:

        opcao = ""          # Reinicia a variavel opcao como vazio
        opcao = input()     # Le a opcao digitada pelo usuario Governo

        while opcao != "F":     # Enquanto a opcao F nao for digitada, entao o usuario pode pedir outras opcoes

            if opcao[0] == "1":         # Se a opcao for apenas 1, entao o usuario quer requisitar que todos os beneficiarios que solicitaram o auxilio sejam analisados

               governo.avaliar_beneficiarios_pendentes()  # Funcao do Classe Governo que analisa a solicitacao de todos os beneficiarios

            elif opcao[0] == "2":   # Se a opcao for apenas 2, entao o usuario quer depositar mais dinheiro na conta do Governo voltada para o auxilio

                quantia = opcao[2:]         # Depois do espaço, o restante da string opcao sera os digitos da quantia digitada
                quantia = float(quantia)     # Transforma a string quantia em float
                governo.adicionar_recursos(quantia)  # Funcao do Governo que adiciona a quantia para as reservas do governo

            elif opcao[0] == "3":   # Se a opcao for apenas 3, entao o usuario quer imprimir os recursos disponiveis para o auxilio dos beneficiarios

                governo.imprimir_recursos_disponiveis()     # Funcao do Governo que imprimir os recursos disponiveis para o auxilio dos beneficiarios

            elif opcao[0] == "4":   # Se a opcao for apenas 4, entao o usuario quer imprimir os beneficiarios que estao recebendo atualmente.

                governo.imprimir_beneficiarios_atuais() # Funcao do Governo que imprimi os beneficiaros que estao recebendo atualmente

            elif opcao[0] == "5":  # Se a opcao for apenas 5, entao o usuario quer enviar o auxilio a aqueles que foram comtemplados.

                governo.enviar_auxilio_mensal()   # Função do Governo que envia os beneficios para aqueles que foram comtemplados

            opcao = ""      # Reinicia a variavel opcao como vazio
            opcao = input()  # Le opcao que o usuario digitar

    escolha = ""    # Reinincia a variavel escolha como vazio
    escolha = input()   # Le de novo a variavel escolha
    escolha = escolha.lower()   # Transforma a variavel escolha como minuscula