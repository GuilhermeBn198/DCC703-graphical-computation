#include <stdio.h>
#include <math.h>

#define BORDA 1
#define TAM_MATRIX 30

void metodoAnalitico(int matrix[TAM_MATRIX][TAM_MATRIX], int x1, int y1, int x2, int y2){
    int y;
    if(x1==x2){
        for(y=y1 ; y<=y2; y++)
            matrix[x1][y] = BORDA;
    }else{
        double m = (double) (y2-y1) / (x2-x1);
        double b = (double) y2-m*x2;
        int x;
        for(x=x1 ; x<=x2 ; x++){
            double k = (double) m*x+b;
            y = round(k);
            matrix[x][y] = BORDA;
        }
    }
}



void pause(){
    getchar();
    getchar();
}

void imprimeMatrix(int matrix[TAM_MATRIX][TAM_MATRIX]){
    int i,j;
    for(i=0;i<TAM_MATRIX;i++){
        for(j=0;j<TAM_MATRIX;j++){
        	if(matrix[i][j]==1){
				printf(" O");
			}else{
				printf(" .");
			}            
        }
        printf("\n");
    }    
}

int main(){

	while(1){
	    printf("\tAlgoritmo Analitico\n\nOBS: Matriz tamanho maximo %dx%d\n\n",TAM_MATRIX,TAM_MATRIX);
	
	    int x1,y1,x2,y2;
	    int matrix[TAM_MATRIX][TAM_MATRIX]={0};
	
	    printf("Informe as coordenadas de x1 e y1.\n>> ");
	    scanf("%d %d",&x1,&y1);
	    printf("Informe as coordenadas de x2 e y2.\n>> ");
	    scanf("%d %d",&x2,&y2);
	    printf("\n");
	
	    metodoAnalitico(matrix, x1,y1,x2,y2);
	    imprimeMatrix(matrix);
	    
	    pause();
	}
	return 0;
}