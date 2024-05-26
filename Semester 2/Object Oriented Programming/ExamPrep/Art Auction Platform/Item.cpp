#include "Item.h"

Item::Item(string name, string category, int currentPrice) :
	name{ name }, category{ category }, currentPrice{ currentPrice }
{
}

Item::Item(string name, string category, int currentPrice, vector<Offer> offers) :
	name{ name }, category{ category }, currentPrice{ currentPrice }, offers{ offers }
{
}

string Item::getName()
{
	return this->name;
}

string Item::getCategory()
{
	return this->category;
}

int Item::getCurrentPrice()
{
	return this->currentPrice;
}

vector<Offer>& Item::getOffers()
{
	return this->offers;
}

void Item::setCurrentPrice(int newCurrentPrice)
{
	this->currentPrice = newCurrentPrice;
}

void Item::addOffer(Offer newOffer)
{
	this->offers.push_back(newOffer);
}

string Item::toString()
{
	return this->name + " | " + this->category + " | " + std::to_string(this->currentPrice);
}

string Item::toStringForFile()
{
	string result = this->name + "|" + 
		this->category + "|" +
		std::to_string(this->currentPrice) + "|";

	for (auto offer : offers)
		result = result + offer.toStringForFile() + "#";

	result.erase(result.end() - 1);

	return result;
}
