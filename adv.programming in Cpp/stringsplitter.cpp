#include<iostream>
#include<string>
#include<algorithm>

using namespace std;


int main(){

	string odd_string;
	string left_of_middle;
	string right_of_middle;
	string middle_middle;
	int length;

	cout<<"Enter an odd length string: ";

	getline(cin,odd_string);

	length = (odd_string.length()-1)/2;
	left_of_middle = odd_string.substr(0, length);
	middle_middle = odd_string.substr(length, 1);
	right_of_middle = odd_string.substr(length+1);



	cout<<"Middle character: "<<middle_middle<<endl;
	cout<<"First half: "<<left_of_middle<<endl;
	cout<<"Second half: "<<right_of_middle<<endl;


	return 0;

}
