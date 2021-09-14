#include <iostream>
using namespace std;

int main()
{
	int dollars, cents, quarters, dimes, nickels, pennies;

	cin>>quarters;
	cin>>dimes;
	cin>>nickels;
	cin>>pennies;

	dollars = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1))/100;
	cents = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1))%100;

	cout<<"The total is "<<dollars<<" dollars and "<<cents<<" cents"<<endl;

	return 0;
}