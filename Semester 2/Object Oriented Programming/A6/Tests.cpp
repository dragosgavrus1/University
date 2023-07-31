#include "Tests.h"
#include "Coat.h"
#include "Repository.h"
#include "AdminService.h"
#include "UserService.h"
#include <assert.h>
#include <iostream>
#include <vector>

Tests::Tests()
{
}

void Tests::testTrenchCoat()
{
	TrenchCoat testCoat{ "S","Red",100,1,"https" };
	assert(testCoat.getSize() == "S");
	assert(testCoat.getColour() == "Red");
	assert(testCoat.getPrice() == 100);
	assert(testCoat.getQuantity() == 1);
	assert(testCoat.getLink() == "https");
	testCoat.setSize("M");
	testCoat.setColour("Blue");
	assert(testCoat.getSize() == "M");
	assert(testCoat.getColour() == "Blue");
	TrenchCoat testCoat2{ "M","Blue",100,1,"https" };
	assert(testCoat == testCoat2);
	testCoat2.setLink("http");
	testCoat2.setPrice(10);
	testCoat2.setQuantity(2);
	assert(testCoat2.getPrice() == 10);
}


void Tests::testRepository()
{
	std::vector<TrenchCoat> testVector;
	Repository testRepository{ testVector };
	assert(testRepository.getCoats().size() == 0);
	TrenchCoat testCoat{ "S","Red",100,1,"https" };
	assert(testRepository.addToRepository(testCoat) == true);
	assert(testRepository.addToRepository(testCoat) == false);
	assert(testRepository.getCoats().size() == 1);
	testCoat.setColour("Green");
	assert(testRepository.updateToRepository(0, testCoat) == true);
	assert(testRepository.getCoats()[0].getColour() == "Green");
	assert(testRepository.removeFromRepository(0) == true);
	assert(testRepository.updateToRepository(-2, testCoat) == false);
	assert(testRepository.getCoats().size() == 0);
	std::vector<TrenchCoat> testVector2 = {};
	testRepository.updateRepository(testVector2);
	assert(testRepository.getCoats().size() == 0);
}


void Tests::testAdminService()
{
	std::vector<TrenchCoat> testVector;
	Repository testRepository{ testVector };
	AdminService testAdmin{ testRepository };
	assert(testAdmin.getAllCoats().size() == 0);
	assert(testAdmin.addToService("S", "Red", 100, 1, "https") == true);
	assert(testAdmin.getAllCoats().size() == 1);
	assert(testAdmin.updateToService("S", "Red", "L", "Black", 20, 1, "http") == true);
	assert(testAdmin.getAllCoats()[0].getColour() == "Black");
	assert(testAdmin.removeFromService("S", "Red") == false);
	assert(testAdmin.removeFromService("L", "Black") == true);
	assert(testAdmin.getAllCoats().size() == 0);
	testAdmin.initial_coats();
	assert(testAdmin.getAllCoats().size() == 10);
}

void Tests::testUserService()
{
	std::vector<TrenchCoat> testVector;
	Repository testRepository{ testVector };
	TrenchCoat testCoat1{ "S","Red",100,3,"https" };
	TrenchCoat testCoat2{ "L","Blue",100,1,"https" };
	TrenchCoat testCoat3{ "S","Black",50,2,"https" };
	testRepository.addToRepository(testCoat1);
	testRepository.addToRepository(testCoat2);
	testRepository.addToRepository(testCoat3);
	UserService testUser{ testRepository };
	assert(testUser.getTotalPrice() == 0);
	assert(testUser.getAllCoats().size() == 3);
	assert(testUser.getShoppingBasket().size() == 0);
	assert(testUser.getFilteredCoatList("").size() == 3);
	assert(testUser.getFilteredCoatList("S").size() == 2);
	testUser.buyCoat(testCoat1);
	assert(testUser.getTotalPrice() == 100);
	testUser.buyCoat(testCoat3);
	assert(testUser.getTotalPrice() == 150);
	assert(testUser.getShoppingBasket().size() == 2);
	std::vector<TrenchCoat> testVector2 = {};
	testUser.updateUserRepo(testVector2);
	assert(testUser.getAllCoats().size() == 0);

}


void Tests::testAll()
{
	testTrenchCoat();
	testRepository();
	testAdminService();
	testUserService();
}
