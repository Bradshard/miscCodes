#include <iostream>
using namespace std;

int main()
{
	int dollars, cents, quarters, dimes, nickels, pennies;

	cout<<"Please enter the amount of money to convert:"<<endl;

	cin>>dollars;
	cin>>cents;

	cents = cents + dollars*100;
	quarters = cents/25;
	cents = (cents - quarters*25);
	dimes = cents/10;
	cents = (cents - dimes*10);
	nickels = (cents)/5;
	cents = (cents - nickels*5);
	pennies = cents/1;
	cents = (cents - pennies*1);

	cout<<"The coins are "<<quarters<<" quarters, "<<dimes<<" dimes, "<<nickels<<" nickels and "<<pennies<<" pennies"<<endl;

	return 0;
}