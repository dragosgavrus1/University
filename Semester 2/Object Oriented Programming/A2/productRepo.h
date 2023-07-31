#pragma once
#include "product.h"
#include "dynamicArray.h"

typedef struct
{
	DynamicArray* dynamicArray;
}ProductRepository;

/// <summary>
/// Create a repository
/// </summary>
/// <returns></returns> the repository
ProductRepository* createRepository();

/// <summary>
/// Add a product to the repository
/// </summary>
/// <param name="repository"></param> the repository
/// <param name="product"></param> the product to be added
void addProduct(ProductRepository* repository, Product* product);

/// <summary>
/// Delete a product form the repo
/// </summary>
/// <param name="repository"></param> the repo
/// <param name="nameOfProductToDelete"></param> 
/// <param name="categoryOfProductToDelete"></param>
/// <returns></returns> an int based on if the operation is valid
int deleteProduct(ProductRepository* repository, char* nameOfProductToDelete, char* categoryOfProductToDelete);

/// <summary>
/// Update a product
/// </summary>
/// <param name="repository"></param> the repo
/// <param name="nameOfProductToUpdate"></param>
/// <param name="categoryOfProductToUpdate"></param>
/// <param name="newQuantity"></param>
/// <param name="newDate"></param>
/// <returns></returns>an int based on if the operation is valid
int updateProduct(ProductRepository* repository, char* nameOfProductToUpdate, char* categoryOfProductToUpdate, int newQuantity, date newDate);

/// <summary>
/// Frees the repository from memory
/// </summary>
/// <param name="repository"></param>the repo to be destroyed
void destroyRepository(ProductRepository* repository);
int positionOfElementInRepository(ProductRepository* repository, char* name, char* category);

/// <summary>
/// test function for the repo
/// </summary>
void testRepository();
