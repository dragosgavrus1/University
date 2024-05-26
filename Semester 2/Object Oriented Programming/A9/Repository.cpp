#include "Repository.h"
#include "Exception.h"
#include <vector>
#include <fstream>


Repository::Repository(std::string filename, std::vector<TrenchCoat> initial_coats) : coats{ initial_coats }, filename{ filename }
{
	this->readFromFile();
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
	this->writeToFile();
	return true;
}

bool Repository::removeFromRepository(int indexOfCoatToRemove)
{
	if (indexOfCoatToRemove < 0 || indexOfCoatToRemove > this->coats.size())
		return false;

	this->coats.erase(coats.begin() + indexOfCoatToRemove);
	this->writeToFile();
	return true;
}

bool Repository::updateToRepository(int indexOfElementToUpdate, TrenchCoat updatedCoat)
{
	if (indexOfElementToUpdate < 0 || indexOfElementToUpdate > this->coats.size())
		return false;

	this->coats[indexOfElementToUpdate] = updatedCoat;
	this->writeToFile();
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

void Repository::readFromFile()
{
	std::ifstream inputStream(this->filename);
	if (!inputStream.is_open())
	{
		throw FileException("The file could not be opened!");
	}
	TrenchCoat coatToRead;
	while (inputStream >> coatToRead)
		this->coats.push_back(coatToRead);
	inputStream.close();
}

void Repository::writeToFile()
{
	std::ofstream outputStream(this->filename);
	if (!outputStream.is_open())
		throw FileException("The file could not be opened!");
	for (auto currentCoat : this->coats)
	{
		outputStream << currentCoat;
	}
	outputStream.close();
}
