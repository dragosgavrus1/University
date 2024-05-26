#include "Service.h"

#include <iterator>
#include <algorithm>

Service::Service(UserRepository& userRepository, ItemsRepository& itemsRepository) :
	userRepository{ userRepository }, itemsRepository{ itemsRepository }
{
}

vector<Item>& Service::getAllItems()
{
	return this->itemsRepository.getAll();
}

vector<Item> Service::getAllItemsFromCategory(string requiredCategory)
{
	vector<Item> allItems = this->itemsRepository.getAll();

	if (requiredCategory == "All")
		return allItems;

	vector<Item> requiredItems;

	copy_if(allItems.begin(), allItems.end(), back_inserter(requiredItems),
		[&requiredCategory](Item currentItem)
		{
			return currentItem.getCategory() == requiredCategory;
		});

	return requiredItems;
}

set<string> Service::getAllCategories()
{
	set<string> allCategories;

	for (auto& item : this->itemsRepository.getAll())
		allCategories.insert(item.getCategory());

	return allCategories;
}

void Service::addItem(string name, string category, int price)
{
	if (name == "")
		throw std::exception{ "Name cannot be empty!" };

	if (price <= 0)
		throw std::exception{ "Price must be positive!" };


	Item itemToAdd{ name, category, price };
	this->itemsRepository.add(itemToAdd);

	this->notify();
}

Item& Service::getItemByName(string name)
{
	return this->itemsRepository.getItemByName(name);
}

vector<Offer> Service::getItemOffers(Item& item)
{
	vector<Offer> offers = item.getOffers();

	sort(offers.begin(), offers.end(),
		[](Offer firstOffer, Offer secondOffer)
		{
			return firstOffer.date > secondOffer.date;
		});

	return offers;
}

void Service::updateCurrentPriceForItem(string userName, string itemName, int newCurrentPrice)
{
	Item& requiredItem = this->getItemByName(itemName);

	if (requiredItem.getCurrentPrice() > newCurrentPrice)
		throw std::exception{ "Bid must be greater than current price!" };

	requiredItem.setCurrentPrice(newCurrentPrice);

	User& currentUser = userRepository.getUserByName(userName);
	Offer newOffer{ currentUser.getId(), "2023.06.13", newCurrentPrice };

	requiredItem.addOffer(newOffer);

	this->notify();
}
