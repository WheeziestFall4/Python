
nome = input()
numerohoraextra = int(input())
valorporhoraanterior = float(input())
valortotal = 0

if numerohoraextra >= 8 and numerohoraextra <=14:
    if numerohoraextra >= 8 and numerohoraextra <= 12:
        valortotal = (valorporhoraanterior * 8 * 22 + valorporhoraanterior*(numerohoraextra - 8)*1.25*22)
        print ("O salário do(a) funcionário(a) "+nome+" será de R${:.2f}".format(valortotal)+" para esse mês")
    else:
        valortotal = (valorporhoraanterior * 8 * 22 + valorporhoraanterior*(numerohoraextra - 8)*1.5*22)
        print("O salário do(a) funcionário(a) "+nome+" será de R${:.2f}".format(valortotal)+" para esse mês")
else:
    print("Número de horas diárias não admitido")
