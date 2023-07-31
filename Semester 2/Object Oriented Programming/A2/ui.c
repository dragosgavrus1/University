#include "ui.h"
#include "service.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "UndoRedo.h"

UI* createUI(Service* service)
{
    UI* ui = malloc(sizeof(UI));
    if (ui == NULL)
        return NULL;
    ui->service = service;
    return ui;
}

void destroyUI(UI* ui)
{
    if (ui == NULL)
        return;
    destroyService(ui->service);
    free(ui);
}

void printMenu()
{
    printf("\n");
    printf("1. Add Product\n");
    printf("2. Remove Product\n");
    printf("3. Update Product\n");
    printf("4. Display Products that contain a string in the name\n");
    printf("5. Display Products of a certain category which expire in X days\n");
    printf("6. Undo\n");
    printf("7. Redo\n");
    printf("0. Exit\n");
    printf("\n");
}

int addUI(UI* ui, UndoRedo* undoRedo)
{
    char name[50], category[20];
    int quantity, day, month, year;
    date expiration_date;

    printf("Name: ");
    scanf("%s", &name);
    printf("Category: ");
    scanf("%s", &category);
    printf("Quantity: ");
    scanf("%d", &quantity);
    printf("Enter the expiration date (day month year): ");
    scanf("%d %d %d", &day, &month, &year);
    expiration_date.day = day;
    expiration_date.month = month;
    expiration_date.year = year;

    DynamicArray* copy = copyDynamicArray(ui->service->repository->dynamicArray);
    int result = addProductToService(ui->service, name, category, quantity, expiration_date);
    //if (result == 0)
    if (result == -1)
    {
        printf("Invalid operation");
        destroyDynamicArray(copy);
    }
    if (result == 1)
    {
        printf("Invalid category");
        destroyDynamicArray(copy);
    }
    if (result == 0)
    {
        addUndoStage(undoRedo, copy);
        clearRedoList(undoRedo);
    }


    return result;
}

int removeUI(UI* ui, UndoRedo* undoRedo)
{
    char name[50], category[20];
    printf("Name of product to delete: ");
    scanf("%s", &name);
    printf("Category of product to delete: ");
    scanf("%s", &category);

    DynamicArray* copy = copyDynamicArray(ui->service->repository->dynamicArray);
    int result = deleteProductFromService(ui->service, name, category);
    
    if (result == -1)
    {
        printf("Invalid operation");
        destroyDynamicArray(copy);
    }
    if (result == 0)
    {
        addUndoStage(undoRedo, copy);
        clearRedoList(undoRedo);
    }
    return result;
}

int updateUI(UI* ui, UndoRedo* undoRedo)
{
    char name[50], category[20];
    int newQuantity, year, month, day;
    date newExpirationDay;
    printf("Name of product to update: ");
    scanf("%s", &name);
    printf("Category of product to update: ");
    scanf("%s", &category);
    printf("New quantity: ");
    scanf("%d", &newQuantity);
    printf("Enter the new expiration date (day month year): ");
    scanf("%d %d %d", &day, &month, &year);
    newExpirationDay.day = day;
    newExpirationDay.month = month;
    newExpirationDay.year = year;

    DynamicArray* copy = copyDynamicArray(ui->service->repository->dynamicArray);
    int result = updateProductFromService(ui->service, name, category, newQuantity, newExpirationDay);
    if (result == -1)
    {
        printf("Invalid operation");
        destroyDynamicArray(copy);
    }
    if (result == 0)
    {
        addUndoStage(undoRedo, copy);
        clearRedoList(undoRedo);
    }
    return result;
}

void printDynamicArray(DynamicArray* dynamicArray)
{
    for (int i = 0; i < dynamicArray->size; i++)
    {
        printf("Name:%s, Category:%s, Quantity:%d, Expiration Date:%d-%d-%d\n", dynamicArray->elements[i]->name, dynamicArray->elements[i]->category, dynamicArray->elements[i]->quantity, dynamicArray->elements[i]->expiration_date.day, dynamicArray->elements[i]->expiration_date.month, dynamicArray->elements[i]->expiration_date.year);

    }
}




int searhNameContainingStringUI(UI* ui)
{
    char search_string[50];
    printf("Search string: ");
    fgets(search_string, sizeof(search_string), stdin);
    fgets(search_string, sizeof(search_string), stdin);
    search_string[strlen(search_string) - 1] = '\0';

    DynamicArray* result_array= createDynamicArray(1);
    int result = searchNameContainingString(ui->service, search_string, result_array);

    if (result_array->size == 0 )
        return 1;

    if (result == -1) 
    {
        printf("Invalid operation");
        return -1;
    }
    printDynamicArray(result_array);

    destroyDynamicArray(result_array);

    return result;
}

int searchExpiredProductsFromCategory(UI* ui)
{
    char search_string[50];
    int number_of_days_until_expiration;
    printf("Search string: ");
    fgets(search_string, sizeof(search_string), stdin);
    fgets(search_string, sizeof(search_string), stdin);
    search_string[strlen(search_string) - 1] = '\0';

    printf("Days until expiration: ");
    scanf("%d", &number_of_days_until_expiration);

    DynamicArray* result_array = createDynamicArray(1);
    int result = filterAllProductsOfACategoryCloseToExpiration(ui->service, search_string, number_of_days_until_expiration, result_array);

    if (result_array->size == 0)
        return 1;

    if (result == -1)
    {
        printf("Invalid operation");
        return -1;
    }
    printDynamicArray(result_array);

    destroyDynamicArray(result_array);

    return result;
}

int readCommandOrPrintError()
{
    char string[10];
    int integer_number;
    int is_number = 0;

    while (is_number == 0)
    {
        printf("Command: ");
        scanf("%s", &string);
        is_number = sscanf(string, "%d", &integer_number);
        if (is_number == 0)
            printf("Not an integer number\n");
    }

    return integer_number;
}

void startApplication(UI* ui)
{
    int command, result;
    UndoRedo* undoRedo = createUndoRedo();

    while (true)
    {
        printMenu();
        command = readCommandOrPrintError();
        while (command < 0 || command > 7)
        {
            printf("Incorrect command\n");
            command = readCommandOrPrintError();
        }

        if (command == 0)
        {
            destroyUndoRedo(undoRedo);
            return;
        }
        else if (command == 1)
        {
            result = addUI(ui, undoRedo);
            if (result == 0)
                printf("Add succsessful\n");
        }
        else if (command == 2)
        {
            result = removeUI(ui, undoRedo);
            if (result == 0)
                printf("Removed succsessful\n");
        }
        else if (command == 3)
        {
            result = updateUI(ui, undoRedo);
            if (result == 0)
                printf("Update succsessful\n");
        }
        else if (command == 4)
        {
            result = searhNameContainingStringUI(ui);
            if (result == 1)
                printf("Repository is empty\n");
        }
        else if (command == 5)
        {
            result = searchExpiredProductsFromCategory(ui);
            if (result == 1)
                printf("No elements\n");
        }
        else if (command == 6)
        {
            result = undoOperation(undoRedo, ui->service->repository);
            if (result == 1)
                printf("No more undos\n");
            if (result == -1)
                printf("Invalid operation\n");
            if (result == 0)
                printf("Succsessful undo\n");
        }
        else if (command == 7)
        {
            result = redoOperation(undoRedo, ui->service->repository);
            if (result == 1)
                printf("No more redos\n");
            if (result == -1)
                printf("Invalid operation\n");
            if (result == 0)
                printf("Succsessful redo\n");
        }
    }
}

