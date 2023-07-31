#include <iostream>
#include "DynamicVector.h"
#include "Repository.h"
#include "AdminService.h"
#include "Ui.h"
#include "Coat.h"
#include "Tests.h"

int main()
{
	Tests tests;
	tests.testAll();

	DynamicVector<TrenchCoat> coats;
	Repository repository{coats};

	AdminService adminService{ repository };
	adminService.initial_coats();
	
	UserService userService{ adminService.getRepository()};	
	Console console{ adminService , userService};
	console.startApplication();

	return 0;
}