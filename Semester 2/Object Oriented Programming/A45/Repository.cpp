#include "Repository.h"

Repository::Repository(DynamicVector<TrenchCoat> initial_coats): coats{initial_coats}
{
}

DynamicVector<TrenchCoat> Repository::getCoats()
{
	return this->coats;
}

bool Repository::addToRepository(TrenchCoat coatToAdd)
{
	if(this->coats.findPositionOfElement(coatToAdd) != -1)
		return false;

	this->coats.addElement(coatToAdd);
	return true;
}

bool Repository::removeFromRepository(int indexOfCoatToRemove)
{
	if(indexOfCoatToRemove < 0 || indexOfCoatToRemove > this->coats.getSize())
		return false;

	this->coats.removeElement(indexOfCoatToRemove);
	return true;
}

bool Repository::updateToRepository(int indexOfElementToUpdate, TrenchCoat updatedCoat)
{
	if (indexOfElementToUpdate < 0 || indexOfElementToUpdate > this->coats.getSize())
		return false;

	this->coats.updateElement(indexOfElementToUpdate, updatedCoat);
	return true;
}

int Repository::coatPositionInRepository(TrenchCoat coat)
{
	return this->coats.findPositionOfElement(coat);
}

int Repository::getSize()
{
	return this->coats.getSize();
}
