#include <iostream>
#include <string>

using namespace std;

string remainingwords(string s);

int main(){

	string word;
	cout <<"Give me a sentence: ";
	getline(cin, word);

	cout <<remainingwords(word);

	return 0;
}

string remainingwords(string s){

	string remainingWords = s.substr(s.find(" ")+1);

	return remainingWords;
}