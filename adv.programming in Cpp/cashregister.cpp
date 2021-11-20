#include <iostream>
#include <bits/stdc++.h>
#include <string>
#include <stdio.h> 
using namespace std;

float discount(string y_n, float first_item, float second_item);

int main(){

	float price_of_first_item;
	float price_of_second_item;
	string club_card_y_n;
	float tax_rate;
	float Base_price;
	float discounted_price;
	float total_price;

	cout<<"Enter price of the first item:";
	cin>>price_of_first_item;
	cout<<"Enter price of the second item:";
	cin>>price_of_second_item;
	cout<<"Does customer have a club card? (Y/N):";
	cin>>club_card_y_n;
	cout<<"Enter tax rate, e.g 5.5 for 5.5(%) tax:";
	cin>>tax_rate;

	Base_price = price_of_first_item + price_of_second_item;

	discounted_price = discount(club_card_y_n,price_of_first_item,price_of_second_item);

	total_price = discounted_price + discounted_price*tax_rate*0.01;

	cout<<fixed<<setprecision(2)<<"Base price = "<<Base_price<<endl;
	cout<<fixed<<setprecision(2)<<"Price after discounts = "<<discounted_price<<endl;
	cout<<fixed<<setprecision(2)<<"Total price = "<<total_price;

	return 0;
}

float discount(string y_n, float first_item, float second_item){

	float pricetag;

	if(y_n == "y" || y_n == "Y")
	{
		if(first_item < second_item)
		{
			pricetag = 0.9*((first_item/2) + second_item);
		}
		else
		{
			pricetag = 0.9*(first_item + (second_item/2));
		}
		
	}
	else if(y_n == "N" || y_n == "n")
	{
		if(first_item < second_item)
		{
			pricetag = (first_item/2) + second_item;
		}
		else
		{
			pricetag = first_item + (second_item/2);
		}
	}
	else
	{
		pricetag = 0;
	}
	return pricetag;
}