#pragma once
#include "FileShoppingBasket.h"
class CsvShoppingBasket :
    public FileShoppingBasket
{
public:
    CsvShoppingBasket(const std::string& filename) :FileShoppingBasket{ filename } {};
    void writeToFile() override;
    void displayShoppingBasket() override;
};

