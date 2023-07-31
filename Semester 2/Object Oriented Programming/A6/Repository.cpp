#include "Repository.h"
#include <vector>

Repository::Repository(std::vector<TrenchCoat> initial_coats): coats{initial_coats}
{
}

std::vector<TrenchCoat>& Repository::getCoats()
{
	return coats;
}


bool Repository::addToRepository(TrenchCoat coatToAdd)
{
	if (std::find(coats.begin(), coats.end(), coatToAdd) != coats.end())
		return false;

	this->coats.push_back(coatToAdd);
	return true;
}

bool Repository::removeFromRepository(int indexOfCoatToRemove)
{
	if (indexOfCoatToRemove < 0 || indexOfCoatToRemove > this->coats.size())
		return false;

	this->coats.erase(coats.begin()+indexOfCoatToRemove);
	return true;
}

bool Repository::updateToRepository(int indexOfElementToUpdate, TrenchCoat updatedCoat)
{
	if (indexOfElementToUpdate < 0 || indexOfElementToUpdate > this->coats.size())
		return false;

	this->coats[indexOfElementToUpdate] = updatedCoat;
	return true;
}

int Repository::coatPositionInRepository(TrenchCoat coat)
{
	auto pointerToElement = std::find(coats.begin(), coats.end(), coat);
	if (pointerToElement == coats.end())
		return -1;
	int index = pointerToElement - coats.begin();
	return index;
}


int Repository::getSize()
{
	return this->coats.size();
}

void Repository::updateRepository(std::vector<TrenchCoat> newCoats)
{
	this->coats.swap(newCoats);
}

Repository::~Repository()
{
	coats.clear();
}
