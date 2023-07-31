#pragma once
#include "FileShoppingBasket.h"
#include <iostream>
#include <fstream>

class HtmlShoppingBasket :
	public FileShoppingBasket
{
public:
	HtmlShoppingBasket(const std::string& filename) : FileShoppingBasket{ filename } {};
	void writeToFile() override;
	void displayShoppingBasket() override;
};

