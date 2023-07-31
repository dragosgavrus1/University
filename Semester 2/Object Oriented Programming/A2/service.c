#include "service.h"
#include "productRepo.h"
#include "product.h"
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <assert.h>


Service* createService(ProductRepository* repository)
{
	Service* service = (Service*)malloc(sizeof(Service));
	if (service == NULL)
		return NULL;
	service->repository = repository;
	return service;
}

void destroyService(Service* service)
{
	if (service == NULL)
		return NULL;
	destroyRepository(service->repository);
	free(service);
}

bool checkIfCategoryIsValid(char* category)
{
	if (strcmp(category, "meat") == 0 || strcmp(category, "dairy") == 0 || strcmp(category, "fruit") == 0 || strcmp(category, "sweets") == 0)
		return true;
	return false;
}

int addProductToService(Service* service, char* name, char* category, int quantity, date expiration_date)
{
	if (service == NULL)
		return -1;
	if (name == NULL || category == NULL)
		return -1;
	if (checkIfCategoryIsValid(category) == false)
	{
		return 1;
	}

	Product* product = createProduct(name, category, quantity, expiration_date);
	if (product == NULL)
		return -1;

	
	addProduct(service->repository, product);
	return 0;

}

int deleteProductFromService(Service* service, char* nameOfProductToDelete, char* categoryOfProductToDelete)
{
	int result = deleteProduct(service->repository, nameOfProductToDelete, categoryOfProductToDelete);
	return result;
}

int updateProductFromService(Service* service, char* nameOfProductToUpdate, char* categoryOfProductToUpdate, int newQuantity, date newExpiration_date)
{
	int result = updateProduct(service->repository, nameOfProductToUpdate, categoryOfProductToUpdate, newQuantity, newExpiration_date);
	return result;
}

int searchNameContainingString(Service* service, char* filter, DynamicArray* filteredArray)
{
	if (service == NULL)
		return -1;

	if (filter[0] == '\0')
	{
		for (int i = 0; i < service->repository->dynamicArray->size; i++)
		{
			Product* product = createProduct(service->repository->dynamicArray->elements[i]->name, service->repository->dynamicArray->elements[i]->category, service->repository->dynamicArray->elements[i]->quantity, service->repository->dynamicArray->elements[i]->expiration_date);
			addElementToArray(filteredArray, product);
		}
	}

	else
	{
		for (int i = 0; i < service->repository->dynamicArray->size; i++)
		{
			char* match;
			match = strstr(service->repository->dynamicArray->elements[i]->name, filter);
			if (match != NULL)
			{
				Product* product = createProduct(service->repository->dynamicArray->elements[i]->name, service->repository->dynamicArray->elements[i]->category, service->repository->dynamicArray->elements[i]->quantity, service->repository->dynamicArray->elements[i]->expiration_date);
				addElementToArray(filteredArray, product);
			}
		}
	}

	for (int i = 0; i < filteredArray->size; i++)
	{
		for (int j = i + 1; j < filteredArray->size; j++)
		{
			if (filteredArray->elements[i]->quantity > filteredArray->elements[j]->quantity)
			{
				Product* auxiliary = filteredArray->elements[i];
				filteredArray->elements[i] = filteredArray->elements[j];
				filteredArray->elements[j] = auxiliary;
			}
		}
	}

	return 0;
}


int filterAllProductsOfACategoryCloseToExpiration(Service* service, char* filter, int numberOfDaysTillExpiration, DynamicArray* filteredArray)
{
	if (service == NULL)
		return -1;

	if (filter[0] == '\0')
	{
		for (int i = 0; i < service->repository->dynamicArray->size; i++)
		{
			
			time_t currentDate = time(NULL);
			struct tm* time = localtime(&currentDate);
			int current_day = time->tm_mday;
			int current_month = time->tm_mon + 1; // Month is 0-based, so add 1
			int current_year = time->tm_year + 1900; // Years since 1900

			current_day += numberOfDaysTillExpiration;
			if (current_day > 30)
			{
				current_day -= 30;
				current_month++;
			}
			if (current_month > 12)
			{
				current_month -= 12;
				current_year++;
			}
			if (service->repository->dynamicArray->elements[i]->expiration_date.year < current_year || service->repository->dynamicArray->elements[i]->expiration_date.year == current_year && service->repository->dynamicArray->elements[i]->expiration_date.month < current_month || service->repository->dynamicArray->elements[i]->expiration_date.year == current_year && service->repository->dynamicArray->elements[i]->expiration_date.month == current_month && service->repository->dynamicArray->elements[i]->expiration_date.day < current_day)
			{
				Product* product = createProduct(service->repository->dynamicArray->elements[i]->name, service->repository->dynamicArray->elements[i]->category, service->repository->dynamicArray->elements[i]->quantity, service->repository->dynamicArray->elements[i]->expiration_date);
				addElementToArray(filteredArray, product);
			}
			
		}
	}

	else
	{
		if (checkIfCategoryIsValid(filter) == false)
			return 1;
		for (int i = 0; i < service->repository->dynamicArray->size; i++)
		{
			if (strcmp(service->repository->dynamicArray->elements[i]->category, filter) == 0)
			{
				time_t currentDate = time(NULL);
				struct tm* time = localtime(&currentDate);
				int current_day = time->tm_mday;
				int current_month = time->tm_mon + 1; // Month is 0-based, so add 1
				int current_year = time->tm_year + 1900; // Years since 1900

				current_day += numberOfDaysTillExpiration;
				if (current_day > 30)
				{
					current_day -= 30;
					current_month++;
				}
				if (current_month > 12)
				{
					current_month -= 12;
					current_year++;
				}
				if (service->repository->dynamicArray->elements[i]->expiration_date.year < current_year || service->repository->dynamicArray->elements[i]->expiration_date.year == current_year && service->repository->dynamicArray->elements[i]->expiration_date.month < current_month || service->repository->dynamicArray->elements[i]->expiration_date.year == current_year && service->repository->dynamicArray->elements[i]->expiration_date.month == current_month && service->repository->dynamicArray->elements[i]->expiration_date.day < current_day)
				{
					Product* product = createProduct(service->repository->dynamicArray->elements[i]->name, service->repository->dynamicArray->elements[i]->category, service->repository->dynamicArray->elements[i]->quantity, service->repository->dynamicArray->elements[i]->expiration_date);
					addElementToArray(filteredArray, product);
				}
			}
		}
	}
	return 0;
}



void testService()
{
	ProductRepository* repository = createRepository();
	Service* service = createService(repository);

	assert(service->repository->dynamicArray->size == 0);
	assert(addProductToService(service, "beef", "meat", 5, (date) { 25, 3, 2023 }) == 0);
	assert(service->repository->dynamicArray->size == 1);
	assert(updateProductFromService(service, "beef", "meat", 1, (date) { 10, 6, 2024 }) == 0);
	assert(deleteProductFromService(service, "beef", "meat") == 0);
	assert(service->repository->dynamicArray->size == 0);

	destroyService(service);

}


