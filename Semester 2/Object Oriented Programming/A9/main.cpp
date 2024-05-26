#include "A9.h"
#include <QtWidgets/QApplication>
#include <iostream>
#include <crtdbg.h>
#include <vector>
#include "Repository.h"
#include "AdminService.h"
#include "UserService.h"
#include "Gui.h"
#include "Coat.h"
#include "Tests.h"
#include "Exception.h"
#include "CsvShoppingBasket.h"
#include "HtmlShoppingBasket.h"
using namespace std;

int main(int argc, char* argv[])
{
	try
	{
		Tests tests;
		tests.testAll();

		Repository* repository = new Repository{};
		FileShoppingBasket* filePointer = nullptr;
		filePointer = new CsvShoppingBasket{ "shoppingBasket.csv" };
		AdminService adminService{ repository };

		UserService userService{ repository , filePointer };
		GUI gui{ adminService , userService };
		gui.startScreen();
		delete filePointer;

	}
	catch (FileException&)
	{
		std::cout << "Repository file could not be opened! The application will terminate." << endl;
		return 1;
	}
	//_CrtDumpMemoryLeaks();
	return 0;
}