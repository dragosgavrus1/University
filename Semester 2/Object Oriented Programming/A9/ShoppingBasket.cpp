#include "ShoppingBasket.h"

std::vector<TrenchCoat> ShoppingBasket::getAllCoats()
{
    return this->coats;
}

bool ShoppingBasket::addCoatToBasket(TrenchCoat coatToAdd)
{
    auto iterator = std::find(this->coats.begin(), this->coats.end(), coatToAdd);
    if (iterator != this->coats.end())
        return false;
    this->coats.push_back(coatToAdd);
    return true;
}
