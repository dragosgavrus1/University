#pragma once
#include <string>
#include "Repository.h"
#include "Coat.h"
#include <vector>

class UserService
{
private:
	Repository coatsRepository;
	std::vector<TrenchCoat> shoppingBasket;
	int total_price;

public:
	UserService(Repository repository);
	std::vector<TrenchCoat> getFilteredCoatList(const std::string& size_filter);
	std::vector<TrenchCoat>& getShoppingBasket();
	int getTotalPrice();
	void buyCoat(TrenchCoat coat);
	std::vector<TrenchCoat>& getAllCoats();
	void updateUserRepo(std::vector<TrenchCoat> newCoats);
};