#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <stdio.h> 
#include <iterator>
using namespace std;

float cost(string date, int time_started, int duration);

int main()
{
	int time;
	int call_time;
	string day;


	cout<<"Enter the day the call started at: ";
	cin>>day;
	cout<<"Enter the time the call started at (hhmm): ";
	cin>>time;
	cout<<"Enter the duration of the call (in minutes): ";
	cin>>call_time;
	
	cout<<fixed<<setprecision(2)<<"This call will cost $"<<cost(day,time,call_time)<<endl;
	
}

float cost(string date, int time_started, int duration)
{
	float cost;

	if(date == "Mon" || date == "Tue" || date == "Wed" || date == "Thr" || date == "Fri" )
	{
		if(time_started >= 800 && time_started <= 1800)
		{
			cost = duration*0.40;
		}
		else{
			cost = duration*0.25;
		}
	}
	else
	{
		cost = duration*0.15;
	}
	return cost;
}