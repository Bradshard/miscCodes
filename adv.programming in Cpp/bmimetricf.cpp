#include <iostream>
#include<bits/stdc++.h>
using namespace std;


float bmimetricf(int weight, float height);

int main()
{
	int weight;
	float height;

	cout<<"Please enter weight in kilograms: ";
	cin>>weight;
	cout<<"Please enter height in meters: ";
	cin>>height;


	cout<<setprecision(4) <<"BMI is: "<<bmimetricf(weight, height)<<endl;

	return 0;
}


float bmimetricf(int weight, float height)
{
	float BMI;
	BMI = weight/(height*height);
	return BMI;
}