#include <stdio.h>

int digits(int num){

	int a = 0;

	while(num!=0){
		num = num/10;
		a++;
	}
	return a-1;

}

int conc(int x, int y){

	int pow =10;
	while(y>=pow){
		pow *= 10;
	}
	return x*pow +y;

}
int power(num,p){


}
void add1(int *num){

	int a = *num;
	int d = digits(a);
	int arr[d-1];
	for(int i=0;i<d;i++){

		arr[i] = 
	}
	

}
