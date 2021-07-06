/* Nome: Vinicius Rodrigues da Costa Almeida RA:254843   Lab04
   Descrição: Programa pede uma matriz nxm e a ordem de uma submatriz rxs. Baseado nisso, calcula qual é o maior soma dos valores de uma submatriz dentro
   da matriz nxm. Entrada: Ordem da matriz nxm, orden da submatriz rxs, a matriz nxm. Retorna: a maior dentre as soma dos valores de cada submatriz possivel dentro da 
   matriz maior*/

#include <stdio.h>

int main()
{
	int n,m,r,s,soma,maxvalor = 0;
	int matriz[100][100];
	
	for(int x = 0; x < 100; x++) /* Inicia os valores da matriz nxm com 0 */
	{
		for(int y = 0; y < 100; y++)
		{
			matriz[x][y] = 0;
		}
	}
	
	scanf("%d %d %d %d",&n,&m,&r,&s);
	
	for(int x = 0; x < n; x++) /* Le os valores da matriz nxm */
	{
		for(int y = 0; y < m; y++)
		{
			scanf("%d",&matriz[x][y]);
		}
	}
	
	for (int x = 0; x < n; x++) /* For percorrem a matriz nxm e as submatrizes rxs, baseado nisso, somam os valores da submatriz e compara com a soma anterior */
	{
		for(int y = 0; y < m  ;y++)
		{
			if((r + x <= n) & (s + y <= m))
			{
				for(int z = x; z < r + x; z++)                          /* Linha r da submatriz */
				{								
					for(int w = y; w < s + y; w++)						/* Coluna s da submatriz */
					{
						soma = soma + matriz[z][w];
					}
				}
				
				if (soma > maxvalor) /* Se a soma atual for maior, entao o maxvalor se torna a soma atual */
				{
					maxvalor = soma;
				}
			}
				soma = 0; 
					
		}
	}
	
	printf("%d\n",maxvalor);
	
	return 0;
}
