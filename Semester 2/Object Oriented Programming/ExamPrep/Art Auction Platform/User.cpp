#include "User.h"

User::User(string name, string type, int id) :
	name{ name }, type{ type }, id{ id }
{
}

string User::getName()
{
	return this->name;
}

string User::getType()
{
	return this->type;
}

int User::getId()
{
	return this->id;
}
