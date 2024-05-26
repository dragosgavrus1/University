#include "ItemsRepository.h"
#include "StringOperations.h"

#include <fstream>
#include <algorithm>

ItemsRepository::ItemsRepository(string filePath) :
	filePath{ filePath }
{
	this->readFile();
}

void ItemsRepository::readFile()
{
	std::ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open file for reading!" };

	string currentItem;

	while (getline(inputFile, currentItem))
	{
		vector<string> fields = splitString(currentItem, '|');

		if (fields.size() == 3)
		{
			Item currentItem{ fields[0], fields[1], stoi(fields[2]) };
			this->add(currentItem);
			
			continue;
		}

		vector<string> offersList = splitString(fields[3], '#');
		vector<Offer> offers;

		for (auto offer : offersList)
		{
			vector<string> offerFields = splitString(offer, ',');
			Offer currentOffer{ stoi(offerFields[0]), offerFields[1], stoi(offerFields[2]) };
			offers.push_back(currentOffer);
		}

		Item currentItem{ fields[0], fields[1], stoi(fields[2]), offers };

		this->add(currentItem);
	}
}

void ItemsRepository::saveFile()
{
	std::ofstream outputFile{ this->filePath };

	if (!outputFile.is_open())
		throw std::exception{ "Cannot open file for write!" };

	for (auto& item : items)
	{
		outputFile << item.toStringForFile() << "\n";
	}

	outputFile.close();

	/*
	pen|write|27|2,2023.05.12,25#1,2023.05.14,27
banana|fruit|5|2,2023.05.12,5
	*/
}

int ItemsRepository::findItemPosition(string name)
{
	auto position = find_if(items.begin(), items.end(),
		[&name](Item currentItem)
		{
			return currentItem.getName() == name;
		});

	if (position == items.end())
		return -1;

	return position - items.begin();
}

Item& ItemsRepository::getItemByName(string name)
{
	int position = this->findItemPosition(name);

	if (position == -1)
		throw std::exception{ "Item not in repository!" };

	return items[position];
}

void ItemsRepository::add(Item itemToAdd)
{
	if (this->findItemPosition(itemToAdd.getName()) != -1)
		throw std::exception{ "Item already in repository!" };

	items.push_back(itemToAdd);

	sort(items.begin(), items.end(),
		[](Item firstItem, Item secondItem)
		{
			return firstItem.getCurrentPrice() < secondItem.getCurrentPrice();
		});
}

vector<Item>& ItemsRepository::getAll()
{
	return this->items;
}

ItemsRepository::~ItemsRepository()
{
	this->saveFile();
}
