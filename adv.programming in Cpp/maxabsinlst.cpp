#include <iostream>
using namespace std;

int maxabsinlst(int lst[], int size);


int main()
{	
	int size;
	int lst[] = {-19,-3,20,-1,5,-25};
	printf("%i", maxabsinlst(lst,6));
	return 0;
}


int maxabsinlst(int lst[], int size)
{
	int max = 0;
	for(int i = 0; i<size; i++)
	{	
		if(i > 0)
		{
			if(lst[i] < 0)
			{
				if((-1*lst[i]) > max)
				{
					max = (-1*lst[i]);
				}
				else
				{
					continue;
				}
			}
			else
			{
				if(lst[i] > max)
				{
					max = lst[i];
				}
				else
				{
					continue;
				}
			}
		}
		else
		{
			if(lst[i] < 0)
			{
				max = -1*lst[i];
			}
			else
			{
				max = lst[i];
			}
		}
	}
	return max;
}

/* I thought it gives error due to package 
#include <cstdlib> use but probably 
not you can still change it to that one though. */