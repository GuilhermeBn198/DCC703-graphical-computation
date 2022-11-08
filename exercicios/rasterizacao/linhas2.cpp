#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <stdlib.h>
#include <cstdlib>

void InitVGA(void);
void retal(int, int, int, int, int);

void InitVGA(){
	int Gd, Gm;
	char GrErr;
	Gd=DETECT;
	Gm=2;
	initgraph(&Gd, &Gm, "C:/msys64/mingw64/lib/" );
	GrErr = graphresult();
	if (GrErr != grOk) {
		printf("Erro grafico %s\n", grapherrormsg(GrErr));
		exit(1);
	}
}

//função algoritmo analitico

void p1(int x1, int x2, int y1, int y2, int cor) {
	int x = x1;
	int y = y1;

	float m;
	int b;

	m = (y2 - y1) / ( x2 - x1);

	b = y2 - m * x2;

	if (x1 == x2) {
		for (y = y1; y <= y2; y++) {
			putpixel(x1, y, cor);
		}
	} else {
		for (x = x1; x <= x2; x++){
			putpixel(x, y, cor);
		}
	}
}

int main() {
	int x1, x2, y1, y2, cor;

	InitVGA();

	x1 = 0;
	y1 = 0;
	x2 = 800;
	for (y2 = 0; y2 < 600; y2++) {
		cor = rand();

		p1(x1, y1, x2, y2, cor);
	}
	getch();
	closegraph();
	return(0);
}
