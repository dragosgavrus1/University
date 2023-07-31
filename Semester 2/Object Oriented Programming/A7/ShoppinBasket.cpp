#include "ShoppinBasket.h"

std::vector<TrenchCoat> ShoppinBasket::getAllCoats()
{
    return this->coats;
}

bool ShoppinBasket::addCoatToBasket(TrenchCoat coatToAdd)
{
    auto iterator = std::find(this->coats.begin(), this->coats.end(), coatToAdd);
    if (iterator != this->coats.end())
        return false;
    this->coats.push_back(coatToAdd);
    return true;
}
