/*   Trabalho 6	
   Nome: Vinicius Rodrigues da Costa Almeida		RA: 254843
   Descricao: Programa le uma frase codificada e descodifica a mensagem baseado em um algorismo unico. */ 

#include <stdio.h>
#include <string.h>

int encontrasimbolomaisrecorrente(char frase[], int tamanho) /*Encontra qual letra se repetiu mais vezes e guarda ela */
{
	int vetor[123], numero;
	
	for(int x = 97; x < 123; x++)
	{
		vetor[x] = 0;
	}
	
	for (int x = 0; x < tamanho; x++)
	{
		numero = frase[x];
		vetor[numero]++;	
		numero = 0;
	}
	
	int maiorvalor = vetor[97];
	int simbolomaisrecorrente = 97;
	
	for(int x = 98; x < 123; x++) /* Pega um vetor que vai de 98 a 123 (igual as posicoes das letras na tabela) e verifica qual possui maior soma */
	{
		if (vetor[x] > maiorvalor)
		{
			maiorvalor = vetor[x];
			simbolomaisrecorrente = x;
		}
	}
	
	return simbolomaisrecorrente; /* retorna a posicao que tem mais recorrencia, o que tem o mesmo numero da letra mais recorrente */
}

void fazdescodificacaobilu (int simbolomaisrecorrente, char frase[], int tamanho) /* Faz a decodificação especial */
{
	int deslocamento = 0;
	
	for (int x = 0; x < tamanho; x++)
	{
		if((simbolomaisrecorrente != 'a') & (simbolomaisrecorrente != 'z')) /* Casos em que a letra mais recorrente nao é a e nem z*/
		{
			deslocamento = simbolomaisrecorrente -'a'; 
			
			if((frase[x] - deslocamento > simbolomaisrecorrente) & (simbolomaisrecorrente != frase[x]) & (frase[x] != ' '))
			{
				if (frase[x] - deslocamento >= 97)
				{
					frase[x] = frase[x] - deslocamento;
				}
				else
				{
					frase[x] = frase[x] - deslocamento - 97 + 122 ; /* Caso o deslocamento ultrapassar o alfabeto, fazer correção. */
				}
			}
			else if((frase[x] - deslocamento - 1 < simbolomaisrecorrente) & (simbolomaisrecorrente != frase[x]) & (frase[x] != ' '))
			{
				if (frase[x] - deslocamento - 1 >= 97)
				{
					frase[x] = frase[x] - deslocamento - 1;
				}
				else
				{
					frase[x] = frase[x] - deslocamento - 97 + 122 + 1; /* Caso o deslocamento ultrapassar o alfabeto, fazer correção. */
				} 
			} 
		}
		
		else if(simbolomaisrecorrente == 'a') /* Caso a letra mais recorrente for a A*/
		{
			deslocamento = 1; 
			
			if ((simbolomaisrecorrente != frase[x]) & (frase[x] != ' ') & (frase[x] != 'b'))
			{
				if (frase[x] - deslocamento >= 97)
				{
					frase[x] = frase[x] - deslocamento;	
				}
				else
				{
					frase[x] = frase[x] - deslocamento - 97 + 122 ; /* Caso o deslocamento ultrapassar o alfabeto, fazer correção. */
				}
			}
			
			else if((frase[x] - deslocamento - 1 < simbolomaisrecorrente) & (simbolomaisrecorrente != frase[x]) & (frase[x] != ' '))
			{
				if (frase[x] - deslocamento - 1>= 97)
				{
					frase[x] = frase[x] - deslocamento;
				}
				else
				{
					frase[x] = frase[x] - deslocamento - 97 + 122; /* Caso o deslocamento ultrapassar o alfabeto, fazer correção. */
				} 
			} 
		} 
		
		else /* Caso a letra mais recorrente for a z*/
		{
			deslocamento = 1; 
			
			if((simbolomaisrecorrente != frase[x]) & (frase[x] != ' '))
			{
				if (frase[x] - deslocamento >= 97)
				{
					frase[x] = frase[x] - deslocamento;	
				}
				else
				{
					frase[x] = frase[x] - deslocamento - 97 + 122 ; /* Caso o deslocamento ultrapassar o alfabeto, fazer correção. */
				}
			}
		}
	}
	
	printf("%s\n",frase);
}

int main()
{
	char frase[10001];
	int simbolomaisrecorrente;
	
	scanf(" %[^\n]",frase);
	
	simbolomaisrecorrente = encontrasimbolomaisrecorrente (frase, strlen(frase));
	fazdescodificacaobilu(simbolomaisrecorrente, frase, strlen(frase));
	
	return 0;
}
