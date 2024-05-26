#pragma once
#include <string>
#include "Repository.h"
#include "Coat.h"
#include "FileShoppingBasket.h"
#include "CsvShoppingBasket.h"
#include "HtmlShoppingBasket.h"
#include <vector>

class UserService
{
private:
	Repository* coatsRepository;
	FileShoppingBasket* shoppingBasket;
	int total_price;

public:
	UserService(Repository* repository = {}, FileShoppingBasket* initialShoppingBasket = nullptr);
	std::vector<TrenchCoat> getFilteredCoatList(const std::string& size_filter);
	int getTotalPrice();
	void buyCoat(TrenchCoat coat);
	std::vector<TrenchCoat>& getAllCoats();
	FileShoppingBasket* getShoppingBasket();
	void saveShoppingBasket();
	void openShoppingBasket();
	void setShoppingBasketType(std::string shoppingBasketType);
};