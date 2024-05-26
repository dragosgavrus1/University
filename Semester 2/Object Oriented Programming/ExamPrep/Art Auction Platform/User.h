#pragma once

#include <string>

using std::string;

class User
{
private:
	string name, type;
	int id;

public:
	User(string name, string type, int id);

	string getName();
	string getType();
	int getId();
};

