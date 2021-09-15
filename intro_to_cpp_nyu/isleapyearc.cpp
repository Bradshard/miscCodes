#include <iostream>
using namespace std;

int main(int argc, char * year[])
{
	int i;
	int leapYear; 

	for (i = 1; i < argc; i++)
	{
		leapYear = atoi(year[i]);
		if (((leapYear % 4 == 0) && (leapYear % 100 != 0)) || (leapYear % 400 == 0))
		{
			cout<<year[i]<<" was a leap year"<<endl;
		}
		else
		{
			cout<<year[i]<<" was not a leap year"<<endl;
		}


	}

	return 0;
}