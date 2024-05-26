#pragma once
#include "Repository.h"
class FakeRepository :
    public Repository
{
public:
    bool boolValueToReturn;
    FakeRepository() : boolValueToReturn{ true } {};
    bool addToRepository(TrenchCoat coatToAdd) override;
    bool removeFromRepository(int indexOfCoatToRemove) override;
    bool updateToRepository(int indexOfElementToUpdate, TrenchCoat updatedCoat) override;
};

