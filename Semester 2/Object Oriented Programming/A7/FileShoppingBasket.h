#pragma once
#include "ShoppinBasket.h"

class FileShoppingBasket :
	public ShoppinBasket
{
protected:
	std::string filename;
public:
	FileShoppingBasket(const std::string& filename) : filename{ filename } {};
	virtual void writeToFile() = 0;
	virtual void displayShoppingBasket() = 0;
	virtual ~FileShoppingBasket() {}
};

