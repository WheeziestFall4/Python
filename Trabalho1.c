/* Nome: Vinicius Rodrigues da Costa Almeida
   RA: 254843
   DESCRICAO: Programa converte os dados dado em segundos para dias, horas e minutos. */

#include <stdio.h>

int main() {
	
	int D,H,M,S,N;
	
	scanf("%d",&N);
	
	D = N/86400;
	H = (N - D * 86400)/3600;
	M = (N - (D * 86400) - H*3600)/60;
	S = N - (D * 86400) - (H*3600) - (M * 60);
	
	printf("%d dia(s), %d hora(s), %d minuto(s) e %d segundo(s).\n",D,H,M,S);
	
	return 0;
}
