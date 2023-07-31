#include "Tests.h"
#include "Coat.h"
#include "DynamicVector.h"
#include "Repository.h"
#include "AdminService.h"
#include "UserService.h"
#include <assert.h>
#include <iostream>


Tests::Tests()
{
}

void Tests::testTrenchCoat()
{
	TrenchCoat testCoat{"S","Red",100,1,"https"};
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
}

void Tests::testDynamicVector()
{
	DynamicVector<int> testVector{1};
	assert(testVector.getSize() == 0);
	testVector.addElement(9);
	assert(testVector.getSize() == 1);
	testVector.updateElement(0, 11);
	assert(testVector.getElement(0) == 11);
	testVector.removeElement(0);
	assert(testVector.getSize() == 0);

}

void Tests::testRepository()
{
	DynamicVector<TrenchCoat> testVector;
	Repository testRepository{ testVector };
	assert(testRepository.getCoats().getSize() == 0);
	TrenchCoat testCoat{ "S","Red",100,1,"https" };
	assert(testRepository.addToRepository(testCoat) == true);
	assert(testRepository.getCoats().getSize() == 1);
	testCoat.setColour("Green");
	assert(testRepository.updateToRepository(0, testCoat) == true);
	assert(testRepository.getCoats().getElement(0).getColour() == "Green");
	assert(testRepository.removeFromRepository(0) == true);
	assert(testRepository.getCoats().getSize() == 0);
}

void Tests::testAdminService()
{
	DynamicVector<TrenchCoat> testVector;
	Repository testRepository{ testVector };
	AdminService testAdmin{ testRepository };
	assert(testAdmin.getAllCoats().getSize() == 0);
	assert(testAdmin.addToService("S", "Red", 100, 1, "https") == true);
	assert(testAdmin.getAllCoats().getSize() == 1);
	assert(testAdmin.updateToService("S", "Red", "L", "Black", 20, 1, "http") == true);
	assert(testAdmin.getAllCoats().getElement(0).getColour() == "Black");
	assert(testAdmin.removeFromService("S", "Red") == false);
	assert(testAdmin.removeFromService("L", "Black") == true);
	assert(testAdmin.getAllCoats().getSize() == 0);

}

void Tests::testUserService()
{
	DynamicVector<TrenchCoat> testVector;
	Repository testRepository{ testVector };
	TrenchCoat testCoat1{ "S","Red",100,3,"https" };
	TrenchCoat testCoat2{ "L","Blue",100,1,"https" };
	TrenchCoat testCoat3{ "S","Black",50,2,"https" };
	testRepository.addToRepository(testCoat1);
	testRepository.addToRepository(testCoat2);
	testRepository.addToRepository(testCoat3);
	UserService testUser{ testRepository };
	assert(testUser.getTotalPrice() == 0);
	assert(testUser.getShoppingBasket().getSize() == 0);
	assert(testUser.getFilteredCoatList("").getSize() == 3);
	assert(testUser.getFilteredCoatList("S").getSize() == 2);
	testUser.buyCoat(testCoat1);
	assert(testUser.getTotalPrice() == 100);
	testUser.buyCoat(testCoat3);
	assert(testUser.getTotalPrice() == 150);
	assert(testUser.getShoppingBasket().getSize() == 2);
}

void Tests::testAll()
{
	testTrenchCoat();
	testDynamicVector();
	testRepository();
	testAdminService();
	testUserService();
}
