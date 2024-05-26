#include "UserRepository.h"
#include "StringOperations.h"

#include <fstream>

UserRepository::UserRepository(string filePath) :
	filePath{ filePath }
{
	this->readFile();
}

void UserRepository::readFile()
{
	std::ifstream inputFile{ filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open file to read!" };

	string currentUser;

	while (getline(inputFile, currentUser))
	{
		vector<string> fields = splitString(currentUser, '|');

		if (fields.size() != 3)
			continue;

		User userToAdd{ fields[0], fields[1], stoi(fields[2]) };
		this->add(userToAdd);
	}

	inputFile.close();
}

int UserRepository::findUserPosition(int id)
{
	auto position = find_if(users.begin(), users.end(),
		[&id](User currentUser)
		{
			return currentUser.getId() == id;
		});

	if (position == users.end())
		return -1;

	return position - users.begin();
}

User& UserRepository::getUserById(int id)
{
	int userIndex = this->findUserPosition(id);

	if (userIndex == -1)
		throw std::exception{ "User not in repository!" };

	return users[userIndex];
}

User& UserRepository::getUserByName(string name)
{
	auto position = find_if(users.begin(), users.end(),
		[&name](User currentUser)
		{
			return currentUser.getName() == name;
		});

	if (position == users.end())
		throw std::exception{ "User not found!" };

	return users[position - users.begin()];
}

void UserRepository::add(User userToAdd)
{
	if (this->findUserPosition(userToAdd.getId()) != -1)
		throw std::exception{ "User already in repository!" };

	users.push_back(userToAdd);
}

vector<User>& UserRepository::getAll()
{
	return users;
}
