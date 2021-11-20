#include <iostream>
using namespace std;

float avgoflst(int lst[], int size);

int main()
{	
	int size;
	int lst[] = {19,2,20,1,0,18};
	printf("%3.0f", avgoflst(lst,6));
	return 0;
}


float avgoflst(int lst[], int size)
{
	float count = 0;
	float sum = 0;
	for(int i = 0; i < size; i++)
	{
		sum = sum + lst[i];
		count++;
	}
	return float(sum/count);
}