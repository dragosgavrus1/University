#pragma once
#include "ShoppingBasket.h"

class FileShoppingBasket :
	public ShoppingBasket
{
protected:
	std::string filename;
public:
	FileShoppingBasket(const std::string& filename) : filename{ filename } {};
	virtual void writeToFile() = 0;
	virtual void displayShoppingBasket() = 0;
	virtual ~FileShoppingBasket() {}
};

