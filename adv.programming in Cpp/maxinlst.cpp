#include <iostream>
using namespace std;

int maxinlst(int lst[], int size);

int main()
{	
	int size;
	int lst[] = {-19,-3,20,-1,5,-25};
	printf("%i", maxinlst(lst,6));
	return 0;
}


int maxinlst(int lst[], int size)
{
	int max = 0;
	for(int i = 0; i<size; i++)
	{	
		if(i > 0)
		{
			if(lst[i] > max)
			{
				max = lst[i];
			}
			else
				continue;
		}
		else
			max = lst[i];
	}
	return max;
}
