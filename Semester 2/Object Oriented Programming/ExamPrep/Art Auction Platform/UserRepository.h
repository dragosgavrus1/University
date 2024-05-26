#pragma once

#include <vector>

#include "User.h"

using std::vector;

class UserRepository
{
private:
	vector<User> users;
	string filePath;

public:
	UserRepository(string filePath);

	void readFile();

	int findUserPosition(int id);
	User& getUserById(int id);
	User& getUserByName(string name);

	void add(User userToAdd);

	vector<User>& getAll();
};

