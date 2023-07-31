#include <iostream>
#include <crtdbg.h>
#include <vector>
#include "Repository.h"
#include "AdminService.h"
#include "UserService.h"
#include "Ui.h"
#include "Coat.h"
#include "Tests.h"
#include "Exception.h"
#include "CsvShoppingBasket.h"
#include "HtmlShoppingBasket.h"
using namespace std;

int main()
{
	try
	{
		Tests tests;
		//tests.testAll();

		Repository repository{ "Coats.txt"};
		FileShoppingBasket* filePointer = nullptr;
		std::cout << "What type of file would you like to use to store the shopping basket?(CSV/HTML)\n";
		string filetype{};
		cin >> filetype;
		if (filetype == "CSV")
			filePointer = new CsvShoppingBasket{ "shoppingBasket.csv" };
		else
			filePointer = new HtmlShoppingBasket{ "shoppingBasket.html" };

		AdminService adminService{ repository };

		UserService userService{ repository , filePointer};
		Console console{ adminService , userService };
		console.startApplication();
		delete filePointer;
	}
	catch (FileException&)
	{
		std::cout << "Repository file could not be opened! The application will terminate." << endl;
		return 1;
	}
	_CrtDumpMemoryLeaks();
	return 0;
}