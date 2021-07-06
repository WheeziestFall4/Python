from decimal import Decimal

numero = Decimal(input())

quartodigito = (numero*100)%10
terceirodigito = ((numero-(quartodigito/100))*10)%10
segundodigito = (numero - (terceirodigito/10)-(quartodigito/100))%10
primeirodigito = (numero -(terceirodigito/10)-(quartodigito/100)-segundodigito)/10

novoprimeirodigito = int(quartodigito)
novosegundodigito = int(terceirodigito)
novoterceirodigito = int(segundodigito)/10
novoquartodigito = int(primeirodigito)

soma = (novosegundodigito + novoterceirodigito)
print("R$ "+str(novoprimeirodigito)+str(soma)+str(novoquartodigito))


