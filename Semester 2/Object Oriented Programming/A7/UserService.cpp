#include "UserService.h"



UserService::UserService(Repository repository, FileShoppingBasket* initialShoppingBasket): coatsRepository{repository}, shoppingBasket{initialShoppingBasket}, total_price{0}
{
}

std::vector<TrenchCoat> UserService::getFilteredCoatList(const std::string& size_filter)
{
	std::vector<TrenchCoat> coatList;
	std::vector<TrenchCoat>& all_coats = this->coatsRepository.getCoats();
	for (int i = 0; i < this->coatsRepository.getSize(); i++)
	{
		TrenchCoat current_coat = all_coats[i];
		if (size_filter.empty() || size_filter.compare(current_coat.getSize()) == 0)
			coatList.push_back(current_coat);
	}
	return coatList;
}



void UserService::buyCoat(TrenchCoat coat)
{
	this->shoppingBasket->addCoatToBasket(coat);
	this->total_price += coat.getPrice();
}

std::vector<TrenchCoat>& UserService::getAllCoats()
{
	return	this->coatsRepository.getCoats();
}


FileShoppingBasket* UserService::getShoppingBasket()
{
	return this->shoppingBasket;
}

void UserService::saveShoppingBasket()
{
	this->shoppingBasket->writeToFile();
}

void UserService::openShoppingBasket()
{
	this->shoppingBasket->displayShoppingBasket();
}

int UserService::getTotalPrice()
{
	return this->total_price;
}

