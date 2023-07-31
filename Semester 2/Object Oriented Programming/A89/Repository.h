#pragma once
#include "Coat.h"
#include <vector>

class Repository
{
private:
	std::vector<TrenchCoat> coats;
	std::string filename;

public:
	Repository(std::string filename = {"coats.txt"}, std::vector<TrenchCoat> initial_coats = {});
	std::vector<TrenchCoat>& getCoats();
	bool addToRepository(TrenchCoat coatToAdd);
	bool removeFromRepository(int indexOfCoatToRemove);
	bool updateToRepository(int indexOfElementToUpdate, TrenchCoat updatedCoat);
	int coatPositionInRepository(TrenchCoat coat);
	int getSize();
	void updateRepository(std::vector<TrenchCoat> newCoats);
	~Repository();
	void readFromFile();
	void writeToFile();
};