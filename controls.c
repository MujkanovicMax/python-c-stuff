#include <stdio.h>
#include <termios.h>
#include <unistd.h>

int getch(void){

	struct termios natt, oatt;
	int ch;
	tcgetattr(STDIN_FILENO, &oatt);
	natt = oatt;
	natt.c_lflag &= ~( ICANON | ECHO );
	tcsetattr(STDIN_FILENO,TCSANOW,&natt);
	ch = getchar();
	tcsetattr(STDIN_FILENO,TCSANOW,&oatt);
	return ch;


}


int main(){

int boundary = 10;
char c=0x00;
int x = 5;
int y = 5;

printf("\033[?25l");
fflush(stdout);



printf("\033[2J");

for(int i = 0; i<=boundary;i++){
	for(int j=0;j<=boundary;j++){

		if(i==0||j==0||i==boundary||j==boundary){
		printf("\033[%d;%dH@",i,j);
		}
	}
}


while( x < boundary&& y < boundary && x > 0 && y > 0){
	printf("\033[%d;%dHx",x,y);
	
	c = getch();
	printf("");
	

	if(c==119){

		x--;
	}
	else if(c==97){

		y--;
	}
	else if(c==115){

		x++;
	}
	else if(c==100){

		y++;
	}
		

}

printf("\033[2J");
printf("\n");
printf("\033[?25h");
fflush(stdout) ;
return 0;
}

