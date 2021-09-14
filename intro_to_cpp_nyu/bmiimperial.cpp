#include <iostream>
using namespace std;

int main()
{
	double weight;
	double height;
	float BMI;

	cout<<"Please enter weight in pounds: ";
	cin>>weight;
	cout<<"Please enter height in inches: ";
	cin>>height;

	weight = weight*0.453592;
	height = height*0.0254;
	

	BMI = weight/(height*height);
    printf("BMI is: %0.2f", BMI);

	return 0;
}