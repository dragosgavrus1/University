#pragma once
#include "Subject.h"

#include "ItemsRepository.h"
#include "UserRepository.h"

#include <set>

using std::set;

class Service :
    public Subject
{
private:
    UserRepository& userRepository;
    ItemsRepository& itemsRepository;

public:
    Service(UserRepository& userRepository, ItemsRepository& itemsRepository);

    vector<Item>& getAllItems();
    vector<Item> getAllItemsFromCategory(string requiredCategory);

    set<string> getAllCategories();

    void addItem(string name, string category, int price);

    Item& getItemByName(string name);

    vector<Offer> getItemOffers(Item& item);

    void updateCurrentPriceForItem(string userName, string itemName, int newCurrentPrice);
};

