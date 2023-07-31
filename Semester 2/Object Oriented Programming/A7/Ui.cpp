
#include "Ui.h"
#include "Coat.h"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define Exit 0
#define Next 1
#define Buy 2
#define ShoppingBasket 3
#define SaveShoppingBasket 4
#define OpenShoppingBasket 5

#define Add 1
#define Remove 2
#define Update 3
#define Print 4


Console::Console(AdminService initial_adminService, UserService initial_userService) : adminService{ initial_adminService }, userService{ initial_userService }
{
}

void Console::printAdminMenu()
{
	cout << "\n";
	cout << "1. Add Coat\n";
	cout << "2. Remove Coat\n";
	cout << "3. Update Coat\n";
	cout << "4. Print Coats\n";
	cout << "0. Exit\n";
}

void Console::addToUI()
{
	string size, colour, link;
	int price, quantity;
	cout << "Coat size: ";
	cin >> size;
	cout << "Coat colour: ";
	cin >> colour;
	cout << "Coat price: ";
	cin >> price;
	cout << "Coat quantity: ";
	cin >> quantity;
	cout << "Coat link: ";
	cin >> link;
	try
	{
		bool result = this->adminService.addToService(size, colour, price, quantity, link);
		cout << "Succsessful add\n";
	}	
	catch(const std::exception& message)
	{
		std::cout << message.what() << "\n";
	}

}

void Console::removeFromUi()
{
	string size, colour;
	cout << "Coat to remove size: ";
	cin >> size;
	cout << "Coat to remove colour: ";
	cin >> colour;

	try
	{
		bool result = this->adminService.removeFromService(size, colour);
		cout << "Remove succsessful\n";
	}
	catch (const std::exception& message)
	{
		std::cout << message.what() << "\n";
	}
	
}

void Console::updateToUi()
{
	string size, colour;
	cout << "Coat to update size: ";
	cin >> size;
	cout << "Coat to update colour: ";
	cin >> colour;

	string newSize, newColour, newLink;
	int newPrice, newQuantity;
	cout << "New coat size: ";
	cin >> newSize;
	cout << "New coat colour: ";
	cin >> newColour;
	cout << "New coat price: ";
	cin >> newPrice;
	cout << "New coat quantity: ";
	cin >> newQuantity;
	cout << "New coat link: ";
	cin >> newLink;

	try
	{
		bool result = this->adminService.updateToService(size, colour, newSize, newColour, newPrice, newQuantity, newLink);
		cout << "Update succsessful\n";
	}
	catch (const std::exception& message)
	{
		std::cout << message.what() << "\n";
	}
}

void Console::printAllCoats()
{
	vector<TrenchCoat> all_coats = this->adminService.getAllCoats();
	for (int i = 0; i < all_coats.size(); i++)
	{
		TrenchCoat current_coat = all_coats[i];
		cout << "Size: " << current_coat.getSize() << " Colour: " << current_coat.getColour() << " Price: " << current_coat.getPrice() << " Quantity: " << current_coat.getQuantity() << " Link: " << current_coat.getLink() << "\n";

	}
}

void Console::startApplication()
{
	cout << "Choose the mode ( administrator/user ) \n";
	string mode;
	while (true)
	{
		cout << "Mode (exit to close program): ";
		cin >> mode;
		if (mode.compare("administrator") == 0)
			administratorMode();
		else if (mode.compare("user") == 0)
		{

			runUser();
		}
		else if (mode.compare("exit") == 0)
			return;
		else
		{
			cout << "No such mode\n";
		}
	}
}

void Console::administratorMode()
{
	while (true)
	{
		printAdminMenu();
		cout << "Option: ";
		int option;
		cin >> option;
		switch (option)
		{
		case Add:
			addToUI();
			break;
		case Remove:
			removeFromUi();
			break;
		case Update:
			updateToUi();
			break;
		case Print:
			printAllCoats();
			break;
		case Exit:
			return;
		default:
			cout << "Invalid option\n";
			break;
		}
	}
}

void Console::userMenu()
{
	cout << "\n0. Exit\n";
	cout << "1. Next\n";
	cout << "2. Buy\n";
	cout << "3. See shopping basket\n";
	cout << "4. Save shopping basket to file\n";
	cout << "5. Open shopping basket\n";

}


void Console::seeShoppingBasket()
{
	vector<TrenchCoat> shoppingBasket = this->userService.getShoppingBasket()->getAllCoats();
	cout << "\nShopping Basket: \n";
	for (int i = 0; i < shoppingBasket.size(); i++)
	{
		TrenchCoat current_coat = shoppingBasket[i];
		cout << "Size: " << current_coat.getSize() << " Colour: " << current_coat.getColour() << " Price: " << current_coat.getPrice() << " Quantity: " << current_coat.getQuantity() << " Link: " << current_coat.getLink() << "\n";

	}
}


void Console::runUser()
{
	string filter;
	cout << "Filter size: ";
	getline(cin, filter);
	getline(cin, filter);
	vector<TrenchCoat> filteredCoats = userService.getFilteredCoatList(filter);
	int size = filteredCoats.size();
	if (size == 0)
	{
		cout << "No coats of this size\n";
		return;
	}
	else
	{
		int index = 0;
		while (true)
		{
			TrenchCoat current_coat = filteredCoats[index];
			cout << "\nSize: " << current_coat.getSize() << " \nColour: " << current_coat.getColour() << "\nPrice: " << current_coat.getPrice() << "\nQuantity: " << current_coat.getQuantity() << "\nLink: " << current_coat.getLink() << "\n";

			userMenu();
			cout << "Option: ";
			int option;
			cin >> option;
			switch (option)
			{
			case Exit:
				return;
			case Next:
				if (index >= size - 1 && index > 0)
					index = 0;
				else if (index < size - 1)
					index++;
				break;
			case Buy:
				userService.buyCoat(current_coat);
				cout << "Total price: " << this->userService.getTotalPrice() << "\n";
				break;
			case ShoppingBasket:
				seeShoppingBasket();
				break;
			case SaveShoppingBasket:
				saveShoppingBasketToFile();
				break;
			case OpenShoppingBasket:
				openShoppingBasket();
				break;
			default:
				cout << "Invalid option\n";
				break;
			}

		}
	}

}

void Console::saveShoppingBasketToFile()
{
	this->userService.saveShoppingBasket();
}

void Console::openShoppingBasket()
{
	this->userService.openShoppingBasket();
}
