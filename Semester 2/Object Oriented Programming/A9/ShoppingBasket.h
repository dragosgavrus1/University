#pragma once
#include "Coat.h"
#include <vector>

class ShoppingBasket
{
protected:
	std::vector<TrenchCoat> coats;
public:
	ShoppingBasket(std::vector<TrenchCoat> initialCoats = {}) {};
	std::vector<TrenchCoat> getAllCoats();
	bool addCoatToBasket(TrenchCoat coatToAdd);
	virtual ~ShoppingBasket() {};
};

