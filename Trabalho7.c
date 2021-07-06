
# include <stdio.h>
# include <stdlib.h>
# include <string.h>


struct Contatos{
	
	char nome[51];
	char endereco[101];
	char telefone[13];
	char data[10];	
};

void insercao (struct Contatos *listas[], int tamanho, int qtddeinsercao)
{
	scanf(" [^\n]",listas[qtddeinsercao] -> nome);
	scanf(" [^\n]",listas[qtddeinsercao] -> endereco);
	scanf(" [^\n]",listas[qtddeinsercao] -> telefone);
	scanf(" [^\n]",listas[qtddeinsercao] -> data);
}

void impressao (struct Contatos listas[], int tamanho, int qtddeinsercao)
{
	printf("Listagem:");
	printf("\n\n%d\n\n",qtddeinsercao);
	for(int x = 0; x <= qtddeinsercao; x++)
	{
		printf("\n%d %s     %s     %s     %s",qtddeinsercao+1,listas[x].nome,listas[x].endereco,listas[x].telefone,listas[x].data);
	}
}


int main(void)
{
	char opcao = 'a';
	int qtddeinsercao = 0;
	struct Contatos contato[1001];
	struct Contatos *listas = &contato[1001];
	
	while (opcao != 'f')
	{
		scanf("%c",&opcao);
		printf("\n\n%c",opcao);
		printf("\n\nCONSEGUIU\n");
		
		if (opcao == 'i')
		{
			insercao(listas, 1001, qtddeinsercao);
			qtddeinsercao++;
			printf("\n\n%d\n\n",qtddeinsercao);
		}
		else if(opcao == 'r')
		{
		/*	remocao();*/
		}
		else if (opcao == 'b')
		{
		/*	busca(); */
		}
		else if (opcao == 'p')
		{
			impressao(contato, 1001,qtddeinsercao); 
		}
		
	}	
	
	return 0;
}
