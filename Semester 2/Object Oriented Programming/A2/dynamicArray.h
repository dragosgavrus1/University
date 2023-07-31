#pragma once
#include "product.h"

typedef Product TElem;

typedef struct
{
	TElem** elements;
	int size, capacity;
}DynamicArray;

/// <summary>
/// Creates a dynamic array
/// </summary>
/// <param name="capacity"></param> The capacity of the dynamic array
/// <returns></returns>
DynamicArray* createDynamicArray(int capacity);

/// <summary>
/// Frees the dynamic array from the memory	
/// </summary>
/// <param name="dynamicArrayToDestroy"></param> The array to be destroyed
void destroyDynamicArray(DynamicArray* dynamicArrayToDestroy);

/// <summary>
/// Resize the array for adding if size == capacity
/// </summary>
/// <param name="dynamicArray"></param>
void resize(DynamicArray* dynamicArray);

/// <summary>
/// Add an element to the array
/// </summary>
/// <param name="dynamicArray"></param> the array
/// <param name="element"></param>	the new element
void addElementToArray(DynamicArray* dynamicArray, TElem* element);

/// <summary>
/// Remove an element from an array
/// </summary>
/// <param name="dynamicArray"></param> The array
/// <param name="position"></param>
void removeElementFromArray(DynamicArray* dynamicArray, int position);

/// <summary>
/// Copy an array for the undo and redo
/// </summary>
/// <param name="dynamicArray"></param> the array to be copied
/// <returns></returns> the copied array
DynamicArray* copyDynamicArray(DynamicArray* dynamicArray);

/// <summary>
/// Getters
/// </summary>
/// <param name="dynamicArray"></param>
/// <returns></returns>
int getSize(DynamicArray* dynamicArray);
int getCapacity(DynamicArray* dynamicArray);

/// <summary>/// Test function for the array/// </summary>
void testDynamicArray();