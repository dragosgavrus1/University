#include "product.h"
#include "productRepo.h"
#include "service.h"
#include "ui.h"
#include <stdlib.h>
#include <stdio.h>

int main()
{
	
	testProduct();
	testDynamicArray();
	testRepository();
	testService();
	testUndoRedo();
	ProductRepository* repository = createRepository();
	Service* service = createService(repository);
	UI* ui = createUI(service);

	addProductToService(service, "beef", "meat", 2, (date) { 25, 3, 2023 });
	addProductToService(service, "apple", "fruit", 20, (date) { 28, 10, 2023 });
	addProductToService(service, "chicken", "meat", 5, (date) { 10, 4, 2023 });
	addProductToService(service, "yoghurt", "dairy", 10, (date) { 25, 5, 2023 });
	addProductToService(service, "cheese", "dairy", 4, (date) { 25, 2, 2023 });
	addProductToService(service, "milk", "dairy", 3, (date) { 29, 3, 2023 });
	addProductToService(service, "pork", "meat", 15, (date) { 11, 5, 2023 });
	addProductToService(service, "chocolate", "sweets", 5, (date) { 25, 3, 2024 });
	addProductToService(service, "jelly", "sweets", 7, (date) { 11, 9, 2025 });
	addProductToService(service, "banana", "fruit", 12, (date) { 1, 8, 2023 });

	startApplication(ui);
	destroyUI(ui);
	

	return 0;
}