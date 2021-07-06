# Nome: Vinicius Rodrigues da Costa Almeida
# RA: 254843
# Descrição: Programa calcula o juros compostos(lucro) de um valor inicial depositado e que sofre movimentacao (retirada ou deposito) a cada mes ate chegar no montante final.
# O usuario deve digitar a qtd de meses que o valor vai ficar no fundo MC102, o juros que ira sofrer o montante por mes e a movimentacao de cada mes.

valorinicial = float(input())
taxajurosmensal = float(input())
qtdmeses = int(input())
movimentacaomensal = 0
mes_atual = 0

valorinicial = valorinicial * (1.0 + taxajurosmensal) # Aplicacao de juros no montante para o primeiro mes

for mes_atual in range(0, qtdmeses): # Repete a ação dentro do for até o ultimes mes da qtd meses digitado pelo usuario

    movimentacaomensal = float(input())   # Pede a movimentacao (retirada ou deposito) para cada mes ( depende da qtd de meses que o usuario digitar)

    while (valorinicial + movimentacaomensal) < 0: # Caso a movimentacao mensal fazer o montante ficar negativo, pede um valor valido para a movimentacao mensal.
        print("Valor inválido no mês "+str(mes_atual)+". Tente novamente.")
        movimentacaomensal = float(input()) #Pede novamente um valor de movimentaçãomensal caso a primeira vez for invalida

    if mes_atual < qtdmeses-1: # Se o numero de meses for menor que o ultimo mes, a conta continuará sofrendo a ação do juros

        valorinicial = valorinicial + movimentacaomensal

        valorinicial = valorinicial * (1.0 + taxajurosmensal)# aplica o juros no montante todo mes

    else: # Nesse caso, se for o ultimo mês, ira entrar nesse else e o montante não irá sofrer mais a ação do juros.

        valorinicial = valorinicial + movimentacaomensal

print("O total após "+str(qtdmeses)+" meses é de R$ {:.2f}".format(valorinicial)+".") # Printa o total de meses que durou o deposito e o valor do montante final.


