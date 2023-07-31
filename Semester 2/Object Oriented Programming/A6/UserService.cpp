#include "UserService.h"

UserService::UserService(Repository repository) :coatsRepository{ repository }, total_price{ 0 }
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


std::vector<TrenchCoat>& UserService::getShoppingBasket()
{
	return this->shoppingBasket;
}



void UserService::buyCoat(TrenchCoat coat)
{
	this->shoppingBasket.push_back(coat);
	this->total_price += coat.getPrice();
}

std::vector<TrenchCoat>& UserService::getAllCoats()
{
	return	this->coatsRepository.getCoats();
}

void UserService::updateUserRepo(std::vector<TrenchCoat> newCoats)
{
	this->coatsRepository.updateRepository(newCoats);
}

int UserService::getTotalPrice()
{
	return this->total_price;
}

