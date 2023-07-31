#pragma once
#include "service.h"
#include "UndoRedo.h"

typedef struct 
{
	Service* service;
}UI;

/// <summary>
/// Creates the ui
/// </summary>
/// <param name="service"></param>
/// <returns></returns> the ui
UI* createUI(Service* service);

/// <summary>
/// Frees the ui
/// </summary>
/// <param name="ui"></param>
void destroyUI(UI* ui);

/// <summary>
/// Prints the menu
/// </summary>
void printMenu();

/// <summary>
/// Add a product from the ui
/// </summary>
/// <param name="ui"></param>
/// <param name="undoRedo"></param> the undoRedo for the functions
/// <returns></returns>
int addUI(UI* ui, UndoRedo* undoRedo);

/// <summary>
/// Remove a product from the ui
/// </summary>
/// <param name="ui"></param>
/// <param name="undoRedo"></param> the undoRedo for the funtions
/// <returns></returns>
int removeUI(UI* ui, UndoRedo* undoRedo);

/// <summary>
/// Updates a product from the ui
/// </summary>
/// <param name="ui"></param>
/// <param name="undoRedo"></param> the undoRedo for the functions
/// <returns></returns>
int updateUI(UI* ui, UndoRedo* undoRedo);

/// <summary>
/// Functionality b
/// </summary>
/// <param name="ui"></param> the ui
/// <returns></returns>
int searhNameContainingStringUI(UI* ui);

/// <summary>
/// Functionality c
/// </summary>
/// <param name="ui"></param> the ui
/// <returns></returns>
int searchExpiredProductsFromCategory(UI* ui);

/// <summary>
/// Prints a dynamic array for funtionality b and c
/// </summary>
/// <param name="dynamicArray"></param>
void printDynamicArray(DynamicArray* dynamicArray);

/// <summary>
/// Reads a command only if it is an integer
/// </summary>
/// <returns></returns>
int readCommandOrPrintError();

/// <summary>
/// Starts the application
/// </summary>
/// <param name="ui"></param>
void startApplication(UI* ui);
