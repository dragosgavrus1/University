#pragma once

typedef struct
{
	int day;
	int month;
	int year;
}date;

typedef struct
{
	char* name;
	char* category;
	int quantity;
	date expiration_date; // time_t

}Product;

/// <summary>
/// This is a function for creating a product
/// </summary>
/// <param name="name"></param> The name of the product
/// <param name="category"></param> The category of the product
/// <param name="quantity"></param> The quantity of the product
/// <param name="expiration_date"></param> The expiration date of the product
/// <returns></returns> The created product
Product* createProduct(char* name, char* category, int quantity, date expiration_date);

/// <summary>
/// Frees a product from memory
/// </summary>
/// <param name="product"></param> The product to free
void removeProduct(Product* product);

/// <summary>
/// Getters
/// </summary>
/// <returns></returns> The value of each field 
char* getName(Product* product);
char* getCategory(Product* product);
int getQuantity(Product* product);
date getExpirationDate(Product* product);

/// <summary>
/// Setters
/// </summary>
/// <param name="product"></param> The product
/// <param _ ></param> The new value of the field
void setName(Product* product, char* newName);
void setCategory(Product* product, char* newCategory);
void setQuantity(Product* product, int newQuantity);
void setDate(Product* product, date newExpirationDate);

/// <summary>
/// Test function for the domain/// 
/// </summary>
void testProduct();