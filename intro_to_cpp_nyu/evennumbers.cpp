#include <iostream>
using namespace std;

int main()
{
	int integer;
	int x = 0;
	int i;

	cout<<"Please enter a positive integer: ";
	cin>>integer;

	for(i = 0; i < integer; i++)
	{
		x += 2;
		cout<<x<<endl;
	}

	return 0;
}