#include <iostream>
#include <string>

using namespace std;

string firstword(string s);


int main(){

	string word;
	cout <<"Give me a sentence: ";
	getline(cin, word);

	cout <<firstword(word);

	return 0;
}

string firstword(string s){

	string firstWord = s.substr(0, s.find(" "));

	return firstWord;
}