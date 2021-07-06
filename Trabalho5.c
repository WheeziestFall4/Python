# include <stdio.h>
# include <stdlib.h>
# include <string.h>

void mudarsituacao(char resultadosenhas[][21], int senhaespecifica)
{
	strcpy(resultadosenhas[senhaespecifica], " inaceitavel.");	
}

void pelomenos8caracteres(char senha[][21],int tamanho1 , char resultadosenhas[][21], int tamanho2)
{
	for(int x = 0; x < tamanho1; x++)
	{
		if((strlen(senha[x]) < 8 ) & (strcmp(senha[x],"") != 0))
		{
			mudarsituacao(resultadosenhas,x); 
		/*	printf("\nERRO FOI AQUI: 1"); */
		}
	} 
}

void pelomenosumavogal(char senha[][21], int tamanho1, char resultadosenhas[][21], int tamanho2)
{
	int soma = 0;
	
	for(int x = 0; x < tamanho1; x++)
	{
		if(strcmp(senha[x],"") != 0)
		{
			for(int y = 0; y <= strlen(senha[x]); y++)
			{
				if ((senha[x][y] == 'a') || (senha[x][y] == 'A'))
				{
					soma++;
				}	
				if ((senha[x][y] == 'e')|| (senha[x][y] == 'E'))
				{
					soma++;
				}	
				
				if ((senha[x][y] == 'i')|| (senha[x][y] == 'I'))
				{
					soma++;
				}	
				if ((senha[x][y] == 'o')|| (senha[x][y] == 'O'))
				{
					soma++;
				}
				if ((senha[x][y] == 'u')|| (senha[x][y] == 'U'))
				{
					soma++;
				}
			}
		
			if( soma == 0)
			{
				mudarsituacao(resultadosenhas,x);
			/*	printf("\nERRO FOI AQUI: 2"); */
			}
		
			soma = 0; 
		}
	} 	
} 

int verificaposicaodigito (char senha[][21],int x,int y)
{
	if(strcmp(senha[x],"") != 0)
	{
		if ((senha[x][y] == '0') || (senha[x][y] == '1')||(senha[x][y] == '2'))
		{
			return 1;
		}	
		if ((senha[x][y] == '3')|| (senha[x][y] == '4'))
		{
			return 1;
		}	
		if ((senha[x][y] == '5') || (senha[x][y] == '6'))
		{
			return 1;
		}	
		if ((senha[x][y] == '7' || senha[x][y] == '8'))
		{
			return 1;
		}
		if ((senha[x][y] == '8' || senha[x][y] == '9'))
		{
			return 1;
		}
	}
			
	return 0;
} 

void pelomenosumdigito(char senha[][21], int tamanho1, char resultadosenhas[][21], int tamanho2)
{
	int soma = 0;
	
	for(int x = 0; x < tamanho1; x++)
	{
		if(strcmp(senha[x],"") != 0)
		{
			for(int y = 0; y <= strlen(senha[x]); y++)
			{
				if ((senha[x][y] == '0' )|| (senha[x][y] == '1' )|| (senha[x][y] == '2'))
				{
					soma++;
				}	
				if ((senha[x][y] == '3')|| (senha[x][y] == '4'))
				{
					soma++;
				}	
				if ((senha[x][y] == '5') || (senha[x][y] == '6'))
				{
					soma++;
				}	
				if ((senha[x][y] == '7')|| (senha[x][y] == '8'))
				{
					soma++;
				}
				if ((senha[x][y] == '8')|| (senha[x][y] == '9'))
				{
					soma++;
				}
			}
		
			if( soma == 0)
			{
				mudarsituacao(resultadosenhas,x);
			/*	printf("\nERRO FOI AQUI: 3"); */
			}
		
			soma = 0; 
		}
	} 			
}

int verificaposicaovogal (char senha[][21],int x,int y)
{
	if(strcmp(senha[x],"") != 0)
	{
		if ((senha[x][y] == 'a')|| (senha[x][y] == 'e'))
		{
			return 1;
		}	
		if ((senha[x][y] == 'i')|| (senha[x][y] == 'o'))
		{
			return 1;
		}	
		if (senha[x][y] == 'u')
		{
			return 1;
		}	
	}
			
	return 0;
} 

void colocaremmaiuscula(char nome[], int tamanho)
{
	for (int x = 0; x < tamanho; x++)
	{
		if(((nome[x] - 32) >= 65) & (nome[x] >= 65) & (nome[x] <= 90))
		{
			nome[x] = nome[x] - 32;
		}
	}	
}

void colocaremminuscula(char nome[], int tamanho)
{
	for (int x = 0; x < tamanho; x++)
	{
		if(((nome[x] + 32) <= 122) & (nome[x] >= 65) & (nome[x] <= 90))
		{
			nome[x] = nome[x] + 32;
		}
		
	}	
}

void pelomenosmaiuscula(char senha[][21], int tamanho1, char resultadosenhas[][21], int tamanho2)
{
	int soma = 0;
	int h = 0;
	
	for(int x = 0; x < tamanho1; x++)
	{
		if(strcmp(senha[x],"") != 0)
		{
			char nome[strlen(senha[x])];
			
			strcpy(nome,senha[x]);
		    colocaremmaiuscula(nome,strlen(senha[x]));
			
			for(int y = 0; y < strlen(senha[x]); y++)
			{	
				h = verificaposicaodigito(senha,x,y);
				
				if((senha[x][y] == nome[y]) & (h != 1))
				{
					soma++;	
				}
				
				h = 0;
			}

			if( soma == 0)
			{
				mudarsituacao(resultadosenhas,x);
		/*		printf("\nERRO FOI AQUI: %4"); */
			}
		
			soma = 0;
		}
	} 			
}

void pelomenosminuscula(char senha[][21], int tamanho1, char resultadosenhas[][21], int tamanho2)
{
	int soma = 0;
	int h = 0;
	
	for(int x = 0; x < tamanho1; x++)
	{
		if(strcmp(senha[x],"") != 0)
		{
			char nome[strlen(senha[x])];
			
			strcpy(nome,senha[x]);
			colocaremminuscula(nome,strlen(senha[x])); 
			
			for(int y = 0; y < strlen(senha[x]); y++)
			{	
				h = verificaposicaodigito(senha,x,y);
				
				if((senha[x][y] == nome[y]) & (h != 1))
				{
					soma++;	
				}
				
				h = 0;
			}

			if( soma == 0)
			{
				mudarsituacao(resultadosenhas,x);
			/*	printf("\nERRO FOI AQUI: 5"); */
			}
		
			soma = 0;
		}
	} 			
}

void naopossuimais3vogaisconsecutivas(char senha[][21], int tamanho1, char resultadosenhas[][21], int tamanho2)
{
	int soma = 0;
	int h = 0;
	
	for(int x = 0; x < tamanho1; x++)
	{
		if(strcmp(senha[x],"") != 0)
		{
			char novasenha[strlen(senha[x])][21];
			
			strcpy(novasenha[x],senha[x]);
			colocaremminuscula(novasenha[x],strlen(novasenha[x]));
			
			for(int y = 0; y < strlen(senha[x]); y++)
			{	
				h = verificaposicaovogal(novasenha[x], x, y);
				
				if(h == 1)
				{
					soma++;	
				}
				else
				{
					soma = 0;
				}
				
				if(soma >= 3)
				{
					mudarsituacao(resultadosenhas,x);
			/*		printf("\nERRO FOI AQUI: 6"); */
					break;
				}
			}
			soma = 0;
		}
	} 				
}

void pelomenos3consoantesconsecutivas(char senha[][21], int tamanho1, char resultadosenhas[][21], int tamanho2)
{
	int soma = 0;
	int h = 0;
	
	for(int x = 0; x < tamanho1; x++)
	{
		if(strcmp(senha[x],"") != 0)
		{
			char novasenha[strlen(senha[x])][21];
			
			strcpy(novasenha[x],senha[x]);
		    colocaremminuscula(novasenha[x],strlen(senha[x]));
			
			for(int y = 0; y < strlen(senha[x]); y++)
			{	
				h = verificaposicaovogal(novasenha, x, y);
				
				if((h == 0) & (verificaposicaodigito(novasenha,x,y) != 1))
				{
					soma++;	
					
					if(soma >= 3)
					{
						break;
					}
				}
				else
				{
					soma = 0;
				}
			}
			
			if(soma < 3)
			{
				mudarsituacao(resultadosenhas,x);
		/*		printf("\nERRO FOI AQUI: 7\n"); */
			}
			
			soma = 0;
		}
	} 				
}


int main()
{
	int x = 0, verificar = 0;
	char nome[21], senha[100][21],resultadosenhas[100][21];
	
	for(int x = 0; x < 100; x++)
	{
		strcpy(senha[x],"");
		strcpy(resultadosenhas[x],"");
	}
		
	while (verificar == 0)
	{	
		scanf("%s",&nome);
		
		if((strcmp(nome,"fim")) == 0)
		{
			verificar = 1;
	
		}
		else
		{
			strcpy(senha[x],nome);
			strcpy(resultadosenhas[x]," aceitavel.");
		}
		
		x++;	
	}
	
	pelomenos8caracteres(senha,100, resultadosenhas, 100); 
	pelomenosumavogal(senha,100, resultadosenhas, 100); 
	pelomenosumdigito(senha,100, resultadosenhas, 100);
	pelomenosmaiuscula(senha,100, resultadosenhas, 100);
	pelomenosminuscula(senha,100, resultadosenhas, 100);
	naopossuimais3vogaisconsecutivas(senha,100, resultadosenhas, 100);
	pelomenos3consoantesconsecutivas(senha,100, resultadosenhas, 100);
	
	for(int x = 0; x < 100; x++)
	{
		if((strcmp(senha[x],"") != 0) & (strcmp(resultadosenhas[x], "") != 0))
		{ 
			printf("[%s] e'",senha[x]);
			printf("%s\n",resultadosenhas[x]);
		} 
	} 
	
/*	printf("ERRO FOI AQUI: %d",num); */
	
	return 0;		
}
