#include <iostream>
using namespace std;

int fibonacci(int integer)
{
	if (integer <= 1)
	{
		return integer;
	}
	return fibonacci(integer - 1) + fibonacci(integer - 2);
}

int main()
{
	int integer;
	int i;
	cout<<"Please enter a positive integer greater than 1: ";
	cin>>integer;

	for(i = 1; i <= integer; i++)
	{
		cout<<fibonacci(i)<<endl;
	}
		

	return 0;
}