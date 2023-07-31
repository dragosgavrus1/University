#include "Coat.h"

TrenchCoat::TrenchCoat(std::string size, std::string colour, int price, int quantity, std::string link)
{
    this->size = size;
    this->colour = colour;
    this->price = price;
    this->quantity = quantity;
    this->link = link;
}

std::string TrenchCoat::getSize()
{
    return this->size;
}

std::string TrenchCoat::getColour()
{
    return this->colour;
}

int TrenchCoat::getPrice()
{
    return this->price;
}

int TrenchCoat::getQuantity()
{
    return this->quantity;
}

std::string TrenchCoat::getLink()
{
    return this->link;
}

void TrenchCoat::setSize(std::string newSize)
{
    this->size = newSize;
}

void TrenchCoat::setColour(std::string newColour)
{
    this->colour = newColour;
}

void TrenchCoat::setLink(std::string newLink)
{
    this->link = newLink;
}

void TrenchCoat::setPrice(int newPrice)
{
    this->price = newPrice;
}

void TrenchCoat::setQuantity(int newQuantity)
{
    this->quantity = newQuantity;
}

bool TrenchCoat::operator==(const TrenchCoat& coatToCompare)
{
    if (this->size == coatToCompare.size && this->colour == coatToCompare.colour)
        return true;
    return false;
}

void TrenchCoat::operator=(const TrenchCoat& coatToCopy)
{
    this->size = coatToCopy.size;
    this->colour = coatToCopy.colour;
    this->price = coatToCopy.price;
    this->quantity = coatToCopy.quantity;
    this->link = coatToCopy.link;
}
