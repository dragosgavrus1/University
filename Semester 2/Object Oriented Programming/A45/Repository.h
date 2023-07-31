#pragma once
#include "Coat.h"
#include "DynamicVector.h"

class Repository
{
private:
	DynamicVector<TrenchCoat> coats;

public:
	Repository(DynamicVector<TrenchCoat> initial_coats = NULL);
	DynamicVector<TrenchCoat> getCoats();
	bool addToRepository(TrenchCoat coatToAdd);
	bool removeFromRepository(int indexOfCoatToRemove);
	bool updateToRepository(int indexOfElementToUpdate, TrenchCoat updatedCoat);
	int coatPositionInRepository(TrenchCoat coat);
	int getSize();
};