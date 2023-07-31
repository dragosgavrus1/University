#include "AdminService.h"
#include <iostream>

AdminService::AdminService(Repository initial_coatsRepository) : coatsRepository{ initial_coatsRepository }
{
}

bool AdminService::addToService(std::string size, std::string colour, int price, int quantity, std::string link)
{
	TrenchCoat coatToAdd{ size, colour, price, quantity, link };
	return this->coatsRepository.addToRepository(coatToAdd);
}

bool AdminService::updateToService(std::string size, std::string colour, std::string newSize, std::string newColour, int newPrice, int newQuantity, std::string newLink)
{
	TrenchCoat coatToUpdate{ size, colour, 0, 0, "" };
	TrenchCoat updatedCoat{ newSize, newColour, newPrice, newQuantity, newLink };
	int index = this->coatsRepository.coatPositionInRepository(coatToUpdate);

	return this->coatsRepository.updateToRepository(index, updatedCoat);
}

bool AdminService::removeFromService(std::string size, std::string colour)
{
	TrenchCoat coatToRemove{ size, colour, 0, 0, "" };
	int index = this->coatsRepository.coatPositionInRepository(coatToRemove);

	return this->coatsRepository.removeFromRepository(index);
}

std::vector<TrenchCoat>& AdminService::getAllCoats()
{
	return this->coatsRepository.getCoats();
}


void AdminService::initial_coats()
{
	this->coatsRepository.addToRepository(TrenchCoat{ "S","Beige",1700,112,"https://ro.burberry.com/c/the-trench-coat/" });
	this->coatsRepository.addToRepository(TrenchCoat{ "M", "Black", 200, 280, "https://www.farfetch.com/" });
	this->coatsRepository.addToRepository(TrenchCoat{ "L", "Red", 175, 300, "https://www.amazon.com/mens-trench-coat/s?k=mens+trench+coat" });
	this->coatsRepository.addToRepository(TrenchCoat{ "XL", "Gray", 56, 1000, "https://www.amazon.com/mens-trench-coat/s?k=mens+trench+coat" });
	this->coatsRepository.addToRepository(TrenchCoat{ "M", "White", 75, 2500, "https://www.amazon.com/mens-trench-coat/s?k=mens+trench+coat" });
	this->coatsRepository.addToRepository(TrenchCoat{ "L", "Brown", 120, 3100, "https://www.amazon.com/mens-trench-coat/s?k=mens+trench+coat" });
	this->coatsRepository.addToRepository(TrenchCoat{ "S", "Green", 1359, 300, "https://www.farfetch.com/" });
	this->coatsRepository.addToRepository(TrenchCoat{ "L", "Blue", 84, 5000, "https://www.asos.com/men/jackets-coats/trench-coats/cat/?cid=11902" });
	this->coatsRepository.addToRepository(TrenchCoat{ "S", "Yellow", 164, 4250, "https://www.asos.com/men/jackets-coats/trench-coats/cat/?cid=11902" });
	this->coatsRepository.addToRepository(TrenchCoat{ "L", "Cactus", 1800, 500, "https://www.goat.com/" });
}

