#include <stdio.h>
#include <math.h>


double maxv(double *arr, int size){

	double temp =0;

	for(int i = 0; i<size-1;i++){

		if(arr[i]>=arr[i+1])
			temp = arr[i];
		
	}
	return temp;

}
double minv(double *arr, int size){

	double temp =0;

	for(int i = 0; i<size-1;i++){

		if(arr[i]<=arr[i+1])
			temp = arr[i];
		
	}
	return temp;

}

void swap(double *a,double *b){

	double temp = *a;
	*a = *b;
	*b = temp;


}

void printarray(double *array,int size){

	for(int i=0;i<size;i++)
		printf("%f ", array[i]);
	printf("\n");

}

void heapify(double *a, int i,int size){
if(i<size){
	int max = i;
	if(a[max] <  a[2*i+1]){

		max = 2*i +1;
		
	}
	if(a[max] < a[2*i+2]){

		max = 2*i +2;
	}
	if(max != i){

		swap(&a[max],&a[i]);
		heapify(a,max,size);
	}
	
}
}

int getparent(double *a, int i){

	int j;
	if(i%2==0){

		j =( i- 2)/2;

	}
	else{

		j = (i-1)/2;
	}
	return j;

}
void buildheap(double *a, int size){

	for(int i = 0; i<size;i++){
	
		heapify(a,i,size);
	}

}

void merge(double *arr, int low,int mid, int high){

	double tarr[high-low+1];

	int i = low;
	int j = mid+1;
	int k = 0;
	while(i <= mid && j<=high){

		if(arr[i] <= arr[j]){

			tarr[k] = arr[i];
			i++;
		}
		else{


		tarr[k] = arr[j];
			j++;
		}
		k++;

	}
	while(i<=mid){
	
		tarr[k] = arr[i];
		i++;
		k++;
	}
	while(j<=high){

		tarr[k] = arr[j];
		j++;
		k++;
	}
	int n =0;
	for(int f = low; f<=high; f++){


		arr[f] = tarr[n];
		n++;

	}
//printarray(arr,7);

}



int partition(double *arr, int low, int high){

	double pivot = arr[high];
	int i = (low-1);

	for(int j=low;j<high;j++){

		if(arr[j] <= pivot){

			i++;
			swap(&arr[j],&arr[i]);

		}

	

	}
	
	swap(&arr[i+1],&arr[high]);

	return i+1;



}


int partition2(double *arr,int low, int high){


	double pivot = arr[high];
	int i=0;
	int j=high-low;
	int l = 0;
	double tarr[high-low+1];

	for(int k =low;k<=high;k++){

		if(arr[k]<=pivot){

			tarr[i]=arr[k];
			i++;

		
		}
		else{

		
			
			tarr[j]=arr[k];
			j--;
			


		}
	}

	for(int k=low;k<=high;k++){

		arr[k] = tarr[l];
		l++;

	}
		
	
	return i-1;

}

void qwsort(double *arr,int low, int high){


	if(high-low==1){

		partition2(arr,low,high);
		return;
	}

	else if(high-low<=0){

		return;
	}
	else{

		int ipiv = partition2(arr,low,high);
	
	
		qwsort(arr,low,ipiv-1);
		
		qwsort(arr,ipiv+1,high);
		return;
	}

}

void mergesort(double *arr,int low, int high){

//	printf("%d-%d\n",high,low);
	if(high-low==1){

		partition2(arr,low,high);
		return;
	}
	else if(high-low<=0)
		return;
	else{

		
	//	printf("a\n");
		mergesort(arr,low,(low+high)/2.);
	//	printf("b\n");
		mergesort(arr,(low+high)/2.+1,high);

	//	printarray(arr,7);
		merge(arr,low,(low+high)/2,high);

	}


}
int main(){

	double a[] = {1.1,8.9,6.44,8,0,120,2.3,3.12,5,12,6};

	double b[] = {7,8.1,9,1,1,0.4,2,9,10};
	double c[] = {3,7,5,5,0,1,2,7,3,14};

	printarray(c,10);
	buildheap(c,10);
	printarray(c,10);

	
}
