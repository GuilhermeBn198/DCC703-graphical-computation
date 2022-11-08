#include <stdio.h>
#include <math.h>

#define BORDA 1
#define TAM_MATRIX 30

///////////////////////////////
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
////////////////////////////////

void metodoAnalitico(int matrix[TAM_MATRIX][TAM_MATRIX], int x1, int y1, int x2, int y2){
    int y;
    if(x1==x2){
        for(y=y1 ; y<y2; y++)
            matrix[x1][y] = BORDA;
    }else{
        double m = (double) (y2-y1) / (x2-x1);
        double b = (double) y2-m*x2;
        int x;
        for(x=x1 ; x<x2 ; x++){
            double k = (double) m*x+b;
            y = round(k);
            matrix[x][y] = BORDA;
        }
    }
}

void algoritmo_dda(int matrix[TAM_MATRIX][TAM_MATRIX], int x1, int y1, int x2, int y2){
	
	int abs_x = x2-x1;
	abs_x = abs(abs_x); //pega o valor abs do delta x

	int abs_y = y2-y1;
	abs_y = abs(abs_y); //pega o valor abs do delta y

	double incremento=0, totalIncrementos=0;

	int x , y;

	if(abs_x > abs_y){
		incremento = (double) (y2-y1) / (x2-x1);
		y = y1;

		printf("INCREMETO = %f\n", incremento);

		for(x=x1 ; x<=x2 ; x++){
			matrix[x][y] = BORDA;
			totalIncrementos = totalIncrementos + incremento;
			y = round(totalIncrementos);
		}
	}else{

		incremento = (double) (x2-x1) / (y2-y1);
		x = x1;
		//printf("INCREMETO = %f\n", incremento);

		for(y=y1 ; y<=y2 ; y++){
			matrix[x][y] = BORDA;
			totalIncrementos = totalIncrementos + incremento;
			x = round(totalIncrementos);
		}
	}

}

void bresenham_line(int matrix[TAM_MATRIX][TAM_MATRIX], int x0,int y0, int x1, int y1){
	int delta_x = abs(x0-x1);
	int delta_y = abs(y0-y1);
	int parametro = 2*delta_y-delta_x;
	int parametro2 = 2*delta_y;
	int xy2 = 2*(delta_y-delta_x);
	int xf,x,y;
	if(x0 > x1){
		x = x1;
		y = y1;
		xf = x0;
		matrix[x][y] = BORDA;
	}else{
		x = x0;
		y = y0;
		xf = x1;
		matrix[x][y] = BORDA;
	}
	while(x < xf){
		x = x+1;
		if(parametro < 0){
			parametro = parametro + parametro2;
		}else{
			y = y+1;
			parametro = parametro + xy2;
        }
		matrix[x][y] = BORDA;			
	}
}

/////////////////////////////////////////////
int main(){
    int reset = 0;
    int selector;
	do{
	    int x1,y1,x2,y2;
	    int matrix[TAM_MATRIX][TAM_MATRIX]={0};
        printf("\n");
        printf("\n");

        
        printf("bem vindo ao aplicativo de rasterizacao de linhas, por favor selecione o algoritmo o qual o aplicativo ira utilizar para fazer a rasterizacao:\n");
        printf("digite 1 para utilizar o algoritmo analitico;\n");
        printf("digite 2 para utilizar o algoritmo DDA;\n");
        printf("digite 3 para utilizar o algoritmo de Bresenham;\n");

        printf("       "); scanf("%d",&selector);
        
        switch (selector){
        case 1:
            printf("\n");
            printf("\tAlgoritmo Analitico Selecionado!\n\nOBS: Matriz tamanho maximo %dx%d\n\n",TAM_MATRIX,TAM_MATRIX);

        
            printf("Informe as coordenadas de x1 e y1.\n>> ");
            scanf("%d %d",&x1,&y1);
            printf("Informe as coordenadas de x2 e y2.\n>> ");
            scanf("%d %d",&x2,&y2);
            printf("\n");
        
            metodoAnalitico(matrix, x1,y1,x2,y2);
            imprimeMatrix(matrix);
            
            pause();
            printf("\n");
            printf("deseja continuar testando os algoritmos? digite '1' para fechar a aplicacao e '0' para continuar: "); scanf("%d",&reset);
            break;
        
        case 2:
            printf("\n");
            printf("\tAlgoritmo DDA Selecionado!\n\nOBS: tamanho da matrix %dx%d\n\n",TAM_MATRIX,TAM_MATRIX);
	
            printf("Informe o valor de x1 e y1.\n>> ");
            scanf("%d %d",&x1,&y1);
            printf("Informe o valor de x2 e y2.\n>> ");
            scanf("%d %d",&x2,&y2);
            printf("\n");
        
            algoritmo_dda(matrix,x1,y1,x2,y2);
            imprimeMatrix(matrix);

            pause();
            printf("\n");
            printf("deseja continuar testando os algoritmos? digite '1' para fechar a aplicacao e '0' para continuar: "); scanf("%d",&reset);
            break;

        case 3:
	
            printf("\t\tAlgoritmo Bresenham de semirretas selecionado!\n\nOBS: tamanho da matrix %dx%d\n\n",TAM_MATRIX,TAM_MATRIX);
            printf("Informe o valor de x1 e y1:\n>> ");
            scanf("%d %d", &x1,&y1);
            printf("Informe o valor de x2 e y2:\n>> ");
            scanf("%d %d", &x2,&y2);
        
            bresenham_line(matrix, x1,y1,x2,y2);
            imprimeMatrix (matrix);
            
            pause();
            printf("\n");
            printf("deseja continuar testando os algoritmos? digite '1' para fechar a aplicacao e '0' para continuar: "); scanf("%d",&reset);
            break;
        default:
            break;
        }
	}while(reset == 0);
    printf("algoritmo Finalizado!");
    pause();
	return 0;
}