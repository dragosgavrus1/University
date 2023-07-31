#include "product.h"
#include <stdlib.h>
#include <string.h>
#include <assert.h>


Product* createProduct(char* name, char* category, int quantity, date expiration_date)
{
    Product* product = malloc(sizeof(Product));
    if (product == NULL)
        return NULL;

    product->name = (char*)malloc(sizeof(char) * (strlen(name)+1)  );
    if (product->name == NULL)
    {
        return product;
    }
    strcpy(product->name, name);

    product->category = (char*)malloc(sizeof(char)* (strlen(category)+1)  );
    if (product->category == NULL)
    {
        free(product->name);
        return product;
    }
    strcpy(product->category, category);

    product->quantity = quantity;

    product->expiration_date = expiration_date;

    return product;
}

void removeProduct(Product* product)
{
    if (product == NULL)
        return;

    free(product->name);
    free(product->category);
    free(product);
}

char* getName(Product* product)
{
    if (product->name == NULL)
        return NULL;
    return product->name;
}

char* getCategory(Product* product)
{
    if (product->category == NULL)
        return NULL;
    return product->category;
}

int getQuantity(Product* product)
{
    if (product == NULL)
        return -1;
    return product->quantity;
}

date getExpirationDate(Product* product)
{
    if (product == NULL)
        return (date){0,0,0};
    return product->expiration_date;
}

void setName(Product* product, char* newName)
{
    free(product->name);
    product->name = (char*)malloc((strlen(newName) + 1) * sizeof(char));
    strcpy(product->name, newName);
}

void setCategory(Product* product, char* newCategory)
{
    free(product->category);
    product->category = (char*)malloc((strlen(newCategory) + 1) * sizeof(char));
    strcpy(product->category, newCategory);
}

void setQuantity(Product* product, int newQuantity)
{
    product->quantity = newQuantity;
}

void setDate(Product* product, date newExpirationDate)
{
    product->expiration_date = newExpirationDate;
}

void testProduct()
{
    date testDate = {1,4,2020};
    Product* testProduct = createProduct("apple", "fruit", 3, testDate);
    assert(strcmp(testProduct->name, "apple") == 0);
    assert(strcmp(testProduct->category, "fruit") == 0);
    assert(testProduct->quantity == 3);
    assert(testProduct->expiration_date.day == 1);
    assert(testProduct->expiration_date.month == 4);
    assert(testProduct->expiration_date.year == 2020);
    setName(testProduct, "tomato");
    assert(strcmp(getName(testProduct), "tomato") == 0);
    setCategory(testProduct, "vegetable");
    assert(strcmp(getCategory(testProduct), "vegetable") == 0);
    setQuantity(testProduct, 4);
    assert(getQuantity(testProduct) == 4);
    setDate(testProduct, (date){ 3,4,2021 });
    testDate = getExpirationDate(testProduct);
    assert(testDate.day == 3);
    assert(testDate.month == 4);
    assert(testDate.year == 2021);

    removeProduct(testProduct);
}

