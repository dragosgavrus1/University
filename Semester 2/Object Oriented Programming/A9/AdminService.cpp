#include "AdminService.h"
#include <iostream>



AdminService::AdminService(Repository* initial_coatsRepository) : coatsRepository{ initial_coatsRepository }
{
}

bool AdminService::addToService(std::string size, std::string colour, int price, int quantity, std::string link)
{
	TrenchCoat coatToAdd{ size, colour, price, quantity, link };

	bool result = this->coatsRepository->addToRepository(coatToAdd);
	if (result == true)
		return true;
	if (result == false)
		throw std::exception("Coat already exist");
}

bool AdminService::updateToService(std::string size, std::string colour, std::string newSize, std::string newColour, int newPrice, int newQuantity, std::string newLink)
{
	TrenchCoat coatToUpdate{ size, colour, 0, 0, "" };
	TrenchCoat updatedCoat{ newSize, newColour, newPrice, newQuantity, newLink };
	int index = this->coatsRepository->coatPositionInRepository(coatToUpdate);

	bool result = this->coatsRepository->updateToRepository(index, updatedCoat);
	if (result == true)
		return true;
	if (result == false)
		throw std::exception("Coat does not exist");
}

bool AdminService::removeFromService(std::string size, std::string colour)
{
	TrenchCoat coatToRemove{ size, colour, 0, 0, "" };
	int index = this->coatsRepository->coatPositionInRepository(coatToRemove);

	bool result = coatsRepository->removeFromRepository(index);
	if (result == true)
		return true;
	if (result == false)
		throw std::exception("Coat does not exist");
}

std::vector<TrenchCoat>& AdminService::getAllCoats()
{
	return this->coatsRepository->getCoats();
}




