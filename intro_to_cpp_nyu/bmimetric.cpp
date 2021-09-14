#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	int weight;
	double height;
	float BMI;

	cout<<"Please enter weight in kilograms: ";
	cin>>weight;
	cout<<"Please enter height in meters: ";
	cin>>height;

	BMI = weight/(height*height);
	cout<<setprecision(4) <<"BMI is: "<<BMI<<endl;

	return 0;
}