#pragma once
#include <string>
#include "Repository.h"
#include "Coat.h"
#include <vector>

class AdminService
{
private:
	Repository* coatsRepository;

public:
	AdminService(Repository* initial_coatsRepository = {});
	bool addToService(std::string size, std::string colour, int price, int quantity, std::string link);
	bool updateToService(std::string size, std::string colour, std::string newSize, std::string newColour, int newPrice, int newQuantity, std::string newLink);
	bool removeFromService(std::string size, std::string colour);
	std::vector<TrenchCoat>& getAllCoats();
};

