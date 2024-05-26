#pragma once

#include <string>
#include <vector>

using std::string;
using std::vector;

struct Offer {
	int userId;
	string date;
	int offeredSum;

	Offer(int userId, string date, int offeredSum) : userId{ userId }, date{ date }, offeredSum{ offeredSum } {}

	string toString()
	{
		return std::to_string(userId) + " | " + date + " | " + std::to_string(offeredSum);
	}

	string toStringForFile()
	{
		return std::to_string(userId) + "," + date + "," + std::to_string(offeredSum);
	}
};

class Item
{
private:
	string name, category;
	int currentPrice;
	vector<Offer> offers;

public:
	Item(string name, string category, int currentPrice);
	Item(string name, string category, int currentPrice, vector<Offer> offers);

	string getName();
	string getCategory();
	int getCurrentPrice();
	vector<Offer>& getOffers();

	void setCurrentPrice(int newCurrentPrice);
	void addOffer(Offer newOffer);

	string toString();
	string toStringForFile();
};

