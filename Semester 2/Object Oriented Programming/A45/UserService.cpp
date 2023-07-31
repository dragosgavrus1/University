#include "UserService.h"

UserService::UserService(Repository repository) :coatsRepository{ repository }, total_price{ 0 }
{
}

DynamicVector<TrenchCoat> UserService::getFilteredCoatList(const std::string& size_filter)
{
	DynamicVector<TrenchCoat> coatList;
	DynamicVector<TrenchCoat> all_coats = this->coatsRepository.getCoats();
	for (int i = 0; i < this->coatsRepository.getSize(); i++)
	{
		TrenchCoat current_coat = all_coats.getElement(i);
		if (size_filter.empty() || size_filter.compare(current_coat.getSize()) == 0)
			coatList.addElement(current_coat);
	}
	return coatList;
}

DynamicVector<TrenchCoat>& UserService::getShoppingBasket()
{
	// TODO: insert return statement here
	return this->shoppingBasket;
}

void UserService::buyCoat(TrenchCoat coat)
{
	this->shoppingBasket.addElement(coat);
	this->total_price += coat.getPrice();
}

int UserService::getTotalPrice()
{
	return this->total_price;
}

DynamicVector<TrenchCoat> UserService::getAllCoats()
{
	return	this->coatsRepository.getCoats();
}
