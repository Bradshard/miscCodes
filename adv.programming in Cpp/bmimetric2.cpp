#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

float bmimetricf(int weight, float height);
string Weight_status(float BMI);

int main()
{
	int weight;
	float height;
	float BMI_result;
	string status;

	cout<<"Please enter weight in kilograms: ";
	cin>>weight;
	cout<<"Please enter height in meters: ";
	cin>>height;

	BMI_result = bmimetricf(weight, height);
	status = Weight_status(BMI_result);
	cout<<setprecision(4) <<"BMI is: "<<BMI_result<<", "<<"Status is "<<status<<endl;

	return 0;
}


float bmimetricf(int weight, float height)
{
	float BMI;
	BMI = weight/(height*height);
	return BMI;
}
string Weight_status(float BMI)
{
	string answer;
	if(BMI < 18.5){
		return answer = "Underweight"; 
	}
	else if(BMI >= 18.5 && BMI <= 24.9){
		return answer = "Normal";
	}
	else if(BMI >= 25.0 && BMI <= 29.9){
		return answer = "Overweight";
	}
	else
	{
		return answer = "Obese";
	}
}