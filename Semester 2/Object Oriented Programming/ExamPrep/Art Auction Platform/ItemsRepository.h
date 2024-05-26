#pragma once

#include <vector>

#include "Item.h"

using std::vector;

class ItemsRepository
{
private:
	vector<Item> items;
	string filePath;

public:
	ItemsRepository(string filePath);

	void readFile();
	void saveFile();

	int findItemPosition(string name);
	Item& getItemByName(string name);

	void add(Item itemToAdd);

	vector<Item>& getAll();

	~ItemsRepository();
};

