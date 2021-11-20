#include<iostream>
#include<string>
#include <cctype>

using namespace std;


int main()
{
	char P;
	cout<<"Enter a character: ";
	cin>>P;

	if (islower(P)){
		cout<<P<<" "<<"is a lower case letter."<<endl;

	}
	if(isdigit(P)){
		cout<<P<<" "<<"is a digit."<<endl;

	}
	if(!isalnum(P)){
		cout<<P<<" "<<"is a non-alphanumeric character."<<endl;

	}
	if(isupper(P)){
		cout<<P<<" "<<"is an upper case letter."<<endl;

	}

}