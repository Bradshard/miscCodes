#include <iostream>
using namespace std;

bool isleapyear(int leapYear);


int main(int argc, char * year[]){


	int i;
	int leapYear;

	for (i = 1; i < argc; i++){

		leapYear = atoi(year[i]);

		cout<<isleapyear(leapYear)<<endl;
	}
		

	return 0;
}



bool isleapyear(int leapYear)
{
	bool isleapyear = false;

	if (((leapYear % 4 == 0) && (leapYear % 100 != 0)) || (leapYear % 400 == 0))
	{
		isleapyear = true;
	}
	else 
	{
		isleapyear = false;
	}
	return isleapyear;
}



    
