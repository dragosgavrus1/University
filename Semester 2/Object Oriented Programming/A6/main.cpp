#include <iostream>
#include <crtdbg.h>
#include <vector>
#include "Repository.h"
#include "AdminService.h"
#include "UserService.h"
#include "Ui.h"
#include "Coat.h"
#include "Tests.h"

int main()
{
	{
		Tests tests;
		tests.testAll();

		//Repository repository{  };
		//AdminService adminService{ repository };
		//adminService.initial_coats();
		//UserService userService{ repository};
		//Console console{ adminService , userService };
		//console.startApplication();
	}
	//_CrtDumpMemoryLeaks();
	return 0;
}