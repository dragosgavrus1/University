#include "dynamicArray.h"
#include "product.h"
#include <stdlib.h>
#include <assert.h>

DynamicArray* createDynamicArray(int capacity)
{
	DynamicArray* dynamicArray = (DynamicArray*)malloc(sizeof(DynamicArray));
	if (dynamicArray == NULL)
		return NULL;

	dynamicArray->capacity = capacity;
	dynamicArray->size = 0;

	dynamicArray->elements = (TElem**) malloc(capacity * sizeof(TElem*));
	if (dynamicArray->elements == NULL)
	{
		free(dynamicArray);
		return NULL;

	}
	return dynamicArray;
}

void destroyDynamicArray(DynamicArray* dynamicArrayToDestroy)
{
	if (dynamicArrayToDestroy == NULL)
		return;

	if (dynamicArrayToDestroy->elements == NULL)
	{
		free(dynamicArrayToDestroy);
		return;
	}

	for (int i = 0; i < dynamicArrayToDestroy->size; i++)
	{
		removeProduct(dynamicArrayToDestroy->elements[i]);
		
	}
	free(dynamicArrayToDestroy->elements);
	free(dynamicArrayToDestroy);
}

void resize(DynamicArray* dynamicArray)
{
	if (dynamicArray == NULL)
		return;

	dynamicArray->capacity *= 2;
	TElem** elements = (TElem**)realloc(dynamicArray->elements, dynamicArray->capacity * sizeof(TElem*));
	if (elements == NULL)
		return; 
	dynamicArray->elements = elements;
}

void addElementToArray(DynamicArray* dynamicArray, TElem* element)
{
	if (dynamicArray == NULL)
		return;
	if (dynamicArray->elements == NULL)
		return;

	if (dynamicArray->capacity == dynamicArray->size)
		resize(dynamicArray);

	dynamicArray->elements[dynamicArray->size] = element;
	dynamicArray->size++;
}

void removeElementFromArray(DynamicArray* dynamicArray, int position)
{
	removeProduct(dynamicArray->elements[position]);
	for (int i = position; i < dynamicArray->size; i++)
	{
		dynamicArray->elements[i] = dynamicArray->elements[i + 1];
	}
	
	dynamicArray->size--;
}


DynamicArray* copyDynamicArray(DynamicArray* dynamicArray)
{
	DynamicArray* dynamicArrayCopy = createDynamicArray(dynamicArray->capacity);
	if (dynamicArrayCopy == NULL)
		return NULL;

	for (int i = 0; i < dynamicArray->size; i++)
	{
		Product* productCopy = createProduct(dynamicArray->elements[i]->name, dynamicArray->elements[i]->category, dynamicArray->elements[i]->quantity, dynamicArray->elements[i]->expiration_date);
		if (productCopy == NULL)
		{
			destroyDynamicArray(dynamicArrayCopy);
			return NULL;
		}

		addElementToArray(dynamicArrayCopy, productCopy);
	}

	return dynamicArrayCopy;
}

int getSize(DynamicArray* dynamicArray)
{
	if (dynamicArray == NULL)
		return 0;
	return dynamicArray->size;
}

int getCapacity(DynamicArray* dynamicArray)
{
	if (dynamicArray == NULL)
		return 0;
	return dynamicArray->capacity;
}

void testDynamicArray()
{
	DynamicArray* dynamicArray = createDynamicArray(10);

	assert(dynamicArray->size == 0);

	Product* product = createProduct("beef", "meat", 1, (date){25, 3, 2023});
	addElementToArray(dynamicArray, product);

	assert(dynamicArray->size == 1);


	DynamicArray* arrayCopy = copyDynamicArray(dynamicArray);
	assert(arrayCopy->size == 1);

	removeElementFromArray(dynamicArray, 0);

	assert(dynamicArray->size == 0);
	assert(arrayCopy->size == 1);

	destroyDynamicArray(dynamicArray);
	destroyDynamicArray(arrayCopy);

}


