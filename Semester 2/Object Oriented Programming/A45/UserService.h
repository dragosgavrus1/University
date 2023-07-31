#pragma once
#include <string>
#include "Repository.h"
#include "Coat.h"
#include "DynamicVector.h"

class UserService
{
private:
	Repository coatsRepository;
	DynamicVector<TrenchCoat> shoppingBasket;
	int total_price;

public:
	UserService(Repository repository);
	DynamicVector<TrenchCoat> getFilteredCoatList(const std::string& size);
	DynamicVector<TrenchCoat>& getShoppingBasket();
	int getTotalPrice();
	void buyCoat(TrenchCoat coat);
	DynamicVector<TrenchCoat> getAllCoats();
};