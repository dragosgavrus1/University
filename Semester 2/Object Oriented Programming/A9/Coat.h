#pragma once
#include <string>

class TrenchCoat
{
private:
	std::string size;
	std::string colour;
	int price, quantity;
	std::string link;

public:
	TrenchCoat(std::string size = std::string(""), std::string colour = std::string(""), int price = 0, int quantity = 0, std::string link = std::string(""));
	std::string getSize();
	std::string getColour();
	int getPrice();
	int getQuantity();
	std::string getLink();
	void setSize(std::string newSize);
	void setColour(std::string newColour);
	void setLink(std::string newLink);
	void setPrice(int newPrice);
	void setQuantity(int newQuantity);
	bool operator==(const TrenchCoat& coatToCompare);
	void operator=(const TrenchCoat& coatToCompare);

	friend std::istream& operator>>(std::istream& inputStream, TrenchCoat& coat);
	friend std::ostream& operator<<(std::ostream& outputStream, const TrenchCoat& coat);

};