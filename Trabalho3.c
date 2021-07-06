/* Nome: Vinicius Rodrigues da Costa Almeida RA: 254843    LAB03
   Descrição: Programa calcula quais ações comprar e vender em um intervalo de dias para obter o maior lucro possivel. Recebe o n de dias, todas as acoes da cada dia.
  e o intervalo limite de compra/venda. Retorna o melhor dia de compra e venda de ações, alem do lucro e a qtd de acoes compradas. */

#include <stdio.h>

int main()
{
	int menordia = 0, maiordia = 0, numdias, maxintervalodias,qtddeacoescompradas = 0,qtddeacoes = 0;
	
	scanf("%d",&numdias);
	
	double lucroatual, maxlucro = 0, maiorpreco = 0, menorpreco = 0,qtddinheiro,precoacoes[numdias];
	
	for(int x = 0; x < numdias;x++) /* Ler cada valor de ações da cada dia. O numero total de dias foi já dado pelo usuario. */
	{
		scanf("%lf",&precoacoes[x]);
	}
	
	scanf("%d",&maxintervalodias);
	scanf("%lf",&qtddinheiro);
	
	for( int x = 0; x < numdias; x++) /* Percorre todas as ações */
	{
			for(int y = x + 1; y < x + maxintervalodias + 1; y++) /* Percorre as ações posterioes ao dia de compra (desde que respeite o maxintervalodias)*/
			{	
				qtddeacoes = qtddinheiro/ precoacoes[x];
				lucroatual = (precoacoes[y] - precoacoes[x]) * qtddeacoes; /* Conta do lucro total */
				
				if((lucroatual > maxlucro) & (precoacoes[y] - precoacoes[x] > 0) & ( y < numdias) ) /*Se o lucro atual de comparação entre ações for maior do que anterior */
				{  															/* e que o intervalo de dias de comparação entre ação atual e as proximas ações não passe o total de dias posteriores. */
					maiorpreco = precoacoes[y];
					menorpreco = precoacoes[x];
					menordia = x;
					maiordia = y;
					maxlucro = lucroatual;
					qtddeacoescompradas = qtddeacoes;
				} 
			} 
	}
	
	if (maxlucro == 0)		/* Se o max lucro for igual a 0, entao houve a compra de acoes apenas da primeira posição e nao houve lucro. */	
	{
		menorpreco = precoacoes[0];
		menordia = 0;
		maiordia = 0;
		maiorpreco = precoacoes[0];
		qtddeacoescompradas = qtddinheiro/precoacoes[0];
	}

	printf("Dia da compra: %d",menordia + 1);
	printf("\nValor de compra: R$ %.2f",menorpreco);
	printf("\nDia da venda: %d",maiordia + 1);
	printf("\nValor de venda: R$ %.2f",maiorpreco); 
	printf("\nQuantidade de acoes compradas: %d",qtddeacoescompradas);
	printf("\nLucro: R$ %.2f\n",maxlucro); 
	
	return 0;
}
