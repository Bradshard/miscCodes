#include <iostream>
#include <stdio.h>      /* printf */
#include <math.h>       /* sqrt */
using namespace std;

bool isPrime(int num);

int main()
{
	int num;
	

	cout<<"please give me a number to check if it's prime or not as true or false. : "<<endl;
	cin>>num;
	
	if(isPrime(num) == true)
	{
		printf("the %d is a prime number. ", num);
	}
	else
	{
		printf("the %d is not a prime number. ", num);
	}
	return 0;
}



bool isPrime(int num){
	int countDivs;
	countDivs = 0;
	for(int i = 1; i <= sqrt(num); i++){
		if(num % i ==0){
			countDivs++;
		}
	}
	if(countDivs == 1)
	{
		return true;
	}
	else
		return false;
}

/* (O(n) = 6sqrt(n) + 4) * n is the size of the input (n = num)  - runtime analysis fast */