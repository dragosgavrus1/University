#include "Coat.h"
#include "Utilis.h"
#include <iostream>
#include <vector>

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



std::istream& operator>>(std::istream& inputStream, TrenchCoat& coat)
{
    std::string line;
    getline(inputStream, line);

    std::vector<std::string> tokens = tokenize(line, ',');
    if (tokens.size() != 5)
        return inputStream;

    coat.size = tokens[0];
    coat.colour = tokens[1];
    coat.price = std::stoi(tokens[2]);
    coat.quantity = std::stoi(tokens[3]);
    coat.link = tokens[4];
    return inputStream;
}

std::ostream& operator<<(std::ostream& outputStream, const TrenchCoat& coat)
{
    outputStream << coat.size << "," << coat.colour << "," << coat.price << "," << coat.quantity << "," << coat.link << "\n";
    return outputStream;
}
