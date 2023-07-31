#pragma once
#include "Coat.h"
#include <vector>

class ShoppinBasket
{
protected:
	std::vector<TrenchCoat> coats;
public:
	ShoppinBasket(std::vector<TrenchCoat> initialCoats = {}) {};
	std::vector<TrenchCoat> getAllCoats();
	bool addCoatToBasket(TrenchCoat coatToAdd);
	virtual ~ShoppinBasket() {};
};

