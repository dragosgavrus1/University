#include "productRepo.h"
#include <stdlib.h>
#include <string.h>
#include <assert.h>


ProductRepository* createRepository()
{
	DynamicArray* dynamicArray = createDynamicArray(1);
	ProductRepository* repository = (ProductRepository*)malloc(sizeof(ProductRepository));

	if (repository == NULL)
		return NULL;

	repository->dynamicArray = dynamicArray;

	return repository;
}

int positionOfElementInRepository(ProductRepository* repository, char* name, char* category)
{
	if (repository == NULL || name == NULL || category == NULL)
		return -1;

	for (int i = 0; i < repository->dynamicArray->size; i++)
	{
		if (strcmp(repository->dynamicArray->elements[i]->name, name) == 0 && strcmp(repository->dynamicArray->elements[i]->category, category) == 0)
			return i;
	}

	return -1;
}


void addProduct(ProductRepository* repository, Product* product)
{	
	int positionInArray = positionOfElementInRepository(repository, product->name, product->category);
	if (positionInArray == -1)
	{
		addElementToArray(repository->dynamicArray, product);
	}
	else
	{
		repository->dynamicArray->elements[positionInArray]->quantity += product->quantity;
	}
}

int deleteProduct(ProductRepository* repository, char* nameOfProductToDelete, char* categoryOfProductToDelete)
{
	int positionInArray;
	positionInArray = positionOfElementInRepository(repository, nameOfProductToDelete, categoryOfProductToDelete);
	if (positionInArray == -1)
		return -1;
	else
	{
		removeElementFromArray(repository->dynamicArray, positionInArray);
		return 0;
	}
}

int updateProduct(ProductRepository* repository, char* nameOfProductToUpdate, char* categoryOfProductToUpdate, int newQuantity, date newDate)
{
	int positionInArray;
	positionInArray = positionOfElementInRepository(repository, nameOfProductToUpdate, categoryOfProductToUpdate);
	if (positionInArray == -1)
		return -1;
	else 
	{
		setQuantity(repository->dynamicArray->elements[positionInArray], newQuantity);
		setDate(repository->dynamicArray->elements[positionInArray], newDate);
		//Product* updatedProduct = createProduct(nameOfProductToUpdate, categoryOfProductToUpdate, newQuantity, newDate);
		//updateElementInArray(repository->dynamicArray, updatedProduct, positionInArray);
		return 0;
	}

}

void destroyRepository(ProductRepository* repository)
{
	if (repository == NULL)
		return;

	destroyDynamicArray(repository->dynamicArray);
	free(repository);
}


void testRepository()
{
	ProductRepository* repository = createRepository();
	Product* testProduct = createProduct("apple", "fruit", 4, (date) { 25, 3, 2023 });
	assert(repository->dynamicArray->size == 0);
	addProduct(repository, testProduct);
	assert(repository->dynamicArray->size == 1);
	updateProduct(repository, "apple", "fruit", 20, (date) { 25, 5, 2024 });
	assert(repository->dynamicArray->elements[0]->quantity == 20);
	assert(repository->dynamicArray->elements[0]->expiration_date.month == 5);
	assert(repository->dynamicArray->elements[0]->expiration_date.year == 2024);
	deleteProduct(repository, "apple", "fruit");
	assert(repository->dynamicArray->size == 0);

	destroyRepository(repository);
}




