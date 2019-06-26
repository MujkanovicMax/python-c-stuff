#include <stdio.h>
#include <stdlib.h>

int digits(int num){

	int a = 0;

	while(num!=0){
		num = num/10;
		a++;
	}
	return a;

}

int conc(int x, int y){

	int pow =10;
	while(y>=pow){
		pow *= 10;
	}
	return x*pow +y;

}

unsigned int power10(int p){
    int pow = 1;
    
    if(p == 0){
        
        return pow;
        
    }
    
    
    for(int i = 0;i<p;i++){
        
     pow *=10;   
    }
    return pow;
}


void reverse(int *arr,int len){
 
    int tmp = 0;
    for(int i = 0;i<len/2;i++){
        
        tmp = arr[i];
        arr[i] = arr[len-1-i];
        arr[len-1-i] = tmp;
        
        
    }
    
    
}

void add1(int *num){
    
	unsigned int a = *num;
        
	unsigned int d = digits(a);
	unsigned int arr[d];
        unsigned int fin = 0;
	for(int i=d-1;i>=0;i--){
                
                unsigned int pow = power10(i);
		arr[i] = a/pow;
                arr[i]++;
                a = a%pow;
	}
	
	reverse(arr,d);
	
	fin = conc(arr[0],arr[1]);
	for(int i = 2; i<d;i++){
         
                fin = conc(fin,arr[i]);
            
        }
	
        *num = fin;
}



int main(){
 
    
    
    unsigned int num = 32340333789;
    printf("%d\n",num);
    
    add1(&num);
    printf("%d\n",num);
    
    
    
    
    
    return 0;
    
}
