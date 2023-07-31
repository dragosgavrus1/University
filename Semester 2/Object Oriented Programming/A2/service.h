#pragma once
#include "productRepo.h"
#include <stdbool.h>

typedef struct
{
	ProductRepository* repository;
}Service;

/// <summary>
/// Creates a service
/// </summary>
/// <param name="repository"></param> the repository for the service
/// <returns></returns> the service
Service* createService(ProductRepository* repository);

/// <summary>
/// Frees the service 
/// </summary>
/// <param name="service"></param>
void destroyService(Service* service);

/// <summary>
/// Checks if the category is valid
/// </summary>
/// <param name="category"></param>
/// <returns></returns> true or false is the category is valid or not
bool checkIfCategoryIsValid(char* category);

/// <summary>
/// Add a product to the service
/// </summary>
/// <param name="service"></param> the service
/// <param ></param> the values for the product
/// <returns></returns> the validity of the operation
int addProductToService(Service* service, char* name, char* category, int quantity, date expiration_date);

/// <summary>
/// Deletes a product from the service
/// </summary>
/// <param name="service"></param> the service
/// <param name="nameOfProductToDelete"></param>
/// <param name="categoryOfProductToDelete"></param>
/// <returns></returns> the validity of the operation
int deleteProductFromService(Service* service, char* nameOfProductToDelete, char* categoryOfProductToDelete);

/// <summary>
/// Updates a product from the service
/// </summary>
/// <param name="service"></param>
/// <param name="nameOfProductToUpdate"></param>
/// <param name="categoryOfProductToUpdate"></param>
/// <param name="newQuantity"></param>
/// <param name="newExpiration_date"></param>
/// <returns></returns>
int updateProductFromService(Service* service, char* nameOfProductToUpdate, char* categoryOfProductToUpdate, int newQuantity, date newExpiration_date);

/// <summary>
/// Searches for the products that contain a given string
/// </summary>
/// <param name="service"></param> 
/// <param name="filter"></param> the filter
/// <param name="filteredArray"></param> all valid products
/// <returns></returns>
int searchNameContainingString(Service* service, char* filter, DynamicArray* filteredArray);

/// <summary>
/// Filter all of the products from a given category which expire in the next X days
/// </summary>
/// <param name="service"></param>
/// <param name="filter"></param>
/// <param name="numberOfDaysTillExpiration"></param>
/// <param name="filteredArray"></param>
/// <returns></returns>
int filterAllProductsOfACategoryCloseToExpiration(Service* service, char* filter, int numberOfDaysTillExpiration, DynamicArray* filteredArray);

/// <summary>
/// Test function for service/// 
/// </summary>
void testService();