#include <iostream>
using namespace std;

int main()
{
	int num1, num2, num3, num4;
	int countOdd = 0;
	int countEven = 0;

	cout<<"Please enter 4 positive integers, separated by a space: "<<endl;

	cin>>num1>>num2>>num3>>num4;

	if(num1 % 2 == 0)
	{
		countEven = countEven + 1;
	}
	else
		countOdd = countOdd + 1;

	if(num2 % 2 == 0){
		countEven = countEven + 1;
	}
	else
	{
		countOdd = countOdd + 1;
	}
	if(num3 % 2 == 0){
		countEven = countEven + 1;
	}
	else
	{
		countOdd = countOdd + 1;
	}
	if(num4 % 2 == 0){
		countEven = countEven + 1;
	}
	else
	{
		countOdd = countOdd + 1;
	}

	if(countEven > countOdd)
	{
		cout<<"more evens"<<endl;
	}
	else if(countOdd > countEven)
	{
		cout<<"more odds"<<endl;
	}
	else
		cout<<"same number of evens and odds"<<endl;


	return 0;
}