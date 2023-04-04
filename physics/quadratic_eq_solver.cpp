#include <iostream>
#include <cmath>
using namespace std;

//Constants to represent type of solutions to an equation.

const int No_Solution = 0;
const int One_Real_Solution = 1;
const int Two_Real_Solution = 2;
const int All_Real = 3;
const int No_Real_Solution = 4;

//Quadratic: Solves the quadratic equation: ax^2 + bx + c = 0
//Input: a, b, c - coefficients of equation
/*Output: 1.Type of solution (return value)
		  2.outX1, outX2 - solutions to equation (output parameters)

  Assumptions: 1. If equation has one solution it will be returned in outX1
			   2. If equation has no real solutions the values in outX1 and outX2 are not defined.
*/

int quadratic(double a, double b, double c, double& outX1, double& outX2);

//linear: Solves a linear equation: ax+b = 0
//Input: a,b - coefficients of equation
/* Output: 1. Type of solution(return value)
 		   2. outX - solution to equation (output parameter)
Assumptions: If equation has no solutions the value returned at outX is not defined
*/

int linear(double a, double b, double& outX);

// This program solves a quadratic equation.
// Input from user: 3 real numbers, representing coefficients of a quadratic equation.
// Output to user: The solutions of the equation, if there are any, or an appropriate message.

int main()
{
	double a, b, c, x1, x2;

	cout<<"Please enter coefficients of quadratic equation: \n";
	cin>>a>>b>>c;
	cout<<"The equation: "<<a<<"x^2 + "<<b<<"x + "<<c<<" = 0"<<endl;
	switch (quadratic(a,b,c,x1,x2))
	{
		case Two_Real_Solution:
			cout<<"Solutions: "<<x1<<" "<<x2<<endl;
			break;
		case One_Real_Solution:
			cout<<"One solution: "<<x1<<endl;
			break;
		case No_Real_Solution:
			cout<<"No real solution"<<endl;
			break;
		case No_Solution:
			cout<<"No solutions"<<endl;
			break;
		case All_Real:
			cout<<"All real numbers are solutions"<<endl;
			break;
		default:
			cout<<"Error"<<endl; 
			break;
	}
	return 0;
}

int quadratic(double a, double b, double c, double& outX1, double& outX2)
{
	double delta;
	if (a != 0.0)
	{
		delta = b*b - 4*a*c;
		if (delta > 0)
		{
			x1 = (-b + sqrt(delta))/(2*a);
			x2 = (-b + sqrt(delta))/(2*a);
			outX1 = x1;
			outX2 = x2;
			return Two_Real_Solution;
		}
		else if (delta == 0)
		{
			x1 = -b/(2*a);
			outX1 = x1;
			return One_Real_Solution;
		}
		else
			return No_Real_Solution;
	}
	else
		return linear(b, c, outX1);
}

int linear(double a, double b, double& outX)
{
	double x;
	if (a != 0)
	{
		x = -b/a;
		outX = x;
		return One_Real_Solution;
	}
	else if ((a == 0) && (b == 0))
	{
		x = 0;
		outX = x;
		return All_Real;
	}
	else // in this case a == 0 && b != 0
		return No_Solution;
}