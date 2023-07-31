#pragma once
#include "AdminService.h"
#include "UserService.h"
#include <vector>

class Console
{
private:
	AdminService adminService;
	UserService userService;

public:
	Console(AdminService initial_adminService, UserService initial_userService);
	void printAdminMenu();
	void addToUI();
	void removeFromUi();
	void updateToUi();
	void printAllCoats();
	void startApplication();
	void administratorMode();
	void userMenu();
	void seeShoppingBasket();
	void runUser();
};