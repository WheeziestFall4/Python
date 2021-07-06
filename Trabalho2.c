/* Nome: Vinicius Rodrigues da Costa Almeida
   RA: 254843
   DESCRICAO: programa recebe qtd de tuplas e as tuplas com numero, frequencia e caractere. Constroi um grafico
   de frequencia. */

#include <stdio.h>

int main()
{
	int n;
	
	scanf("%d",&n);
	
	int i = 0,num[1000], frequencia[1000],k = 0,y = 0;
	char c[1000];
	
	for (i = 0; i < n; i++)
	{	
		if (i < n-1)
		{		
			scanf(" (%d,%d,%c) ",&num[i],&frequencia[i],&c[i]);
		}
		else 
		{
			scanf(" (%d,%d,%c)",&num[i],&frequencia[i],&c[i]);
		}
	}
	
	for(y = 0; y < n; y++)
	{
		printf("%4d |",num[y]);
		
		for(k = 0; k < frequencia[y]; k++)
		{
			printf("%c",c[y]);
		}
		
		printf(" %d\n",frequencia[y]);
	}
	
	return 0;
}
	
