#include <iostream>
using namespace std;

int factorial(int num);
int kCombinations(int n , int k);

int main()
{
	int n, k, k_comb;
	cout<<"Please enter n and k (n => k): "<<endl;
	cin>>n>>k;

	cout<<n<<" choose "<<k<<" is ";
	cout<<k_comb<<endl;
	return 0;
}

int kCombinations(int n , int k)
{
	int n_Fact, k_Fact, n_kFact;

	n_Fact = factorial(n);
	k_Fact = factorial(k);
	n_kFact = factorial(n-k);

	return (n_Fact / (k_Fact + n_kFact));

}

int factorial(int num)
{
	int factRes, i;
	factRes = 1;

	for (i = 1; i<= num; i++)
		factRes *= i;
	return factRes;
}