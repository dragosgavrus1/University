#include "Tests.h"
#include "Coat.h"
#include "Repository.h"
#include "AdminService.h"
#include "UserService.h"
#include "FakeRepository.h"
#include <assert.h>
#include <iostream>
#include <vector>

Tests::Tests()
{
}

//void Tests::testTrenchCoat()
//{
//	TrenchCoat testCoat{ "S","Red",100,1,"https" };
//	assert(testCoat.getSize() == "S");
//	assert(testCoat.getColour() == "Red");
//	assert(testCoat.getPrice() == 100);
//	assert(testCoat.getQuantity() == 1);
//	assert(testCoat.getLink() == "https");
//	testCoat.setSize("M");
//	testCoat.setColour("Blue");
//	assert(testCoat.getSize() == "M");
//	assert(testCoat.getColour() == "Blue");
//	TrenchCoat testCoat2{ "M","Blue",100,1,"https" };
//	assert(testCoat == testCoat2);
//	testCoat2.setLink("http");
//	testCoat2.setPrice(10);
//	testCoat2.setQuantity(2);
//	assert(testCoat2.getPrice() == 10);
//}
//
//
//void Tests::testRepository()
//{
//	std::vector<TrenchCoat> testVector;
//	Repository testRepository{ "Coats.txt", testVector };
//	assert(testRepository.getCoats().size() == 0);
//	TrenchCoat testCoat{ "S","Red",100,1,"https" };
//	assert(testRepository.addToRepository(testCoat) == true);
//	assert(testRepository.getCoats().size() == 1);
//	testCoat.setColour("Green");
//	assert(testRepository.updateToRepository(0, testCoat) == true);
//	assert(testRepository.getCoats()[0].getColour() == "Green");
//	assert(testRepository.removeFromRepository(0) == true);
//	assert(testRepository.getCoats().size() == 0);
//}
//
//
//void Tests::testAdminService()
//{
//	std::vector<TrenchCoat> testVector;
//	Repository testRepository{ "Coats.txt", testVector };
//	AdminService testAdmin{ testRepository };
//	assert(testAdmin.getAllCoats().size() == 0);
//	assert(testAdmin.addToService("S", "Red", 100, 1, "https") == true);
//	assert(testAdmin.getAllCoats().size() == 1);
//	assert(testAdmin.updateToService("S", "Red", "L", "Black", 20, 1, "http") == true);
//	assert(testAdmin.getAllCoats()[0].getColour() == "Black");
//	assert(testAdmin.removeFromService("S", "Red") == false);
//	assert(testAdmin.removeFromService("L", "Black") == true);
//	assert(testAdmin.getAllCoats().size() == 0);
//}
//
//void Tests::testUserService()
//{
//	std::vector<TrenchCoat> testVector;
//	Repository testRepository{ "Coats.txt", testVector };
//	TrenchCoat testCoat1{ "S","Red",100,3,"https" };
//	TrenchCoat testCoat2{ "L","Blue",100,1,"https" };
//	TrenchCoat testCoat3{ "S","Black",50,2,"https" };
//	testRepository.addToRepository(testCoat1);
//	testRepository.addToRepository(testCoat2);
//	testRepository.addToRepository(testCoat3);
//	UserService testUser{ testRepository };
//	assert(testUser.getTotalPrice() == 0);
//	assert(testUser.getShoppingBasket()->getAllCoats().size() == 0);
//	assert(testUser.getFilteredCoatList("").size() == 3);
//	assert(testUser.getFilteredCoatList("S").size() == 2);
//	testUser.buyCoat(testCoat1);
//	assert(testUser.getTotalPrice() == 100);
//	testUser.buyCoat(testCoat3);
//	assert(testUser.getTotalPrice() == 150);
//	assert(testUser.getShoppingBasket()->getAllCoats().size() == 2);
//}


void Tests::testAll()
{
	TestService_Add_Valid();
	TestService_Add_Invalid();
	TestService_Remove_Valid();
	TestService_Remove_Invalid();
	TestService_Update_Invalid();
	TestService_Update_Valid();
}

void Tests::TestService_Add_Valid()
{
	FakeRepository* fakeRepository = new FakeRepository{};
	AdminService testService{ fakeRepository };
	fakeRepository->boolValueToReturn = true;
	assert(testService.addToService("S", "Red", 100, 1, "https") == true);
}

void Tests::TestService_Add_Invalid()
{
	FakeRepository* fakeRepository = new FakeRepository{};
	AdminService testService{ fakeRepository };
	fakeRepository->boolValueToReturn = false;
	try {
		testService.addToService("S", "Red", 100, 1, "https");
		assert(false);
	}
	catch (std::exception)
	{
		assert(true);
	}
}

void Tests::TestService_Remove_Valid()
{
	FakeRepository* fakeRepository = new FakeRepository{};
	AdminService testService{ fakeRepository };
	fakeRepository->boolValueToReturn = true;
	assert(testService.removeFromService("S", "Red") == true);
}

void Tests::TestService_Remove_Invalid()
{
	FakeRepository* fakeRepository = new FakeRepository{};
	AdminService testService{ fakeRepository };
	fakeRepository->boolValueToReturn = false;
	try {
		testService.removeFromService("S", "Red");
		assert(false);
	}
	catch (std::exception)
	{
		assert(true);
	}
}

void Tests::TestService_Update_Valid()
{
	FakeRepository* fakeRepository = new FakeRepository{};
	AdminService testService{ fakeRepository };
	fakeRepository->boolValueToReturn = true;
	assert(testService.updateToService("L", "Black", "S", "Red", 100, 1, "https") == true);
}

void Tests::TestService_Update_Invalid()
{
	FakeRepository* fakeRepository = new FakeRepository{};
	AdminService testService{ fakeRepository };
	fakeRepository->boolValueToReturn = false;
	try {
		testService.updateToService("L", "Black", "S", "Red", 100, 1, "https");
		assert(false);
	}
	catch (std::exception)
	{
		assert(true);
	}
}




