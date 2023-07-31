#include "UndoRedo.h"
#include "productRepo.h"
#include <stdio.h>
#include <stdlib.h>


UndoRedo* createUndoRedo()
{
	UndoRedo* undoRedo = (UndoRedo*)malloc(sizeof(UndoRedo));
	if (undoRedo == NULL)
		return NULL;

	undoRedo->undoCapacity = 2;
	undoRedo->undoList = (DynamicArray**)malloc(undoRedo->undoCapacity * sizeof(DynamicArray*));
	if (undoRedo->undoList == NULL)
	{
		free(undoRedo);
		return NULL;
	}
	undoRedo->undoSize = 0;

	undoRedo->redoCapacity = 2;
	undoRedo->redoList = (DynamicArray**)malloc(undoRedo->redoCapacity * sizeof(DynamicArray*));
	if (undoRedo->redoList == NULL)
	{
		free(undoRedo->redoList);
		free(undoRedo);
		return NULL;
	}
	undoRedo->redoSize = 0;

	return undoRedo;
}

void destroyUndoRedo(UndoRedo* undoRedo)
{
	if (undoRedo == NULL)
		return;

	for (int i = 0; i < undoRedo->undoSize; i++)
	{
		destroyDynamicArray(undoRedo->undoList[i]);
	}
	free(undoRedo->undoList);

	for (int i = 0; i < undoRedo->redoSize; i++)
	{
		destroyDynamicArray(undoRedo->redoList[i]);
	}
	free(undoRedo->redoList);

	free(undoRedo);
}

void resizeUndo(UndoRedo* undoRedo)
{
	if (undoRedo == NULL)
		return;

	undoRedo->undoCapacity *= 2;
	DynamicArray** auxialiarArray = (DynamicArray**)realloc(undoRedo->undoList, undoRedo->undoCapacity * sizeof(DynamicArray*));
	if (auxialiarArray == NULL)
		return;

	undoRedo->undoList = auxialiarArray;
}

void resizeRedo(UndoRedo* undoRedo)
{
	if (undoRedo == NULL)
		return;

	undoRedo->redoCapacity *= 2;
	DynamicArray** auxialiarArray = (DynamicArray**)realloc(undoRedo->redoList, undoRedo->redoCapacity * sizeof(DynamicArray*));
	if (auxialiarArray == NULL)
		return;

	undoRedo->redoList = auxialiarArray;
}

void addUndoStage(UndoRedo* undoRedo, DynamicArray* previousStage)
{
	if (undoRedo == NULL || previousStage == NULL)
		return ;

	if (undoRedo->undoSize == undoRedo->undoCapacity)
		resizeUndo(undoRedo);

	undoRedo->undoList[undoRedo->undoSize] = previousStage;
	undoRedo->undoSize++;

}

void addRedoStage(UndoRedo* undoRedo, DynamicArray* previousStage)
{
	if (undoRedo == NULL || previousStage == NULL)
		return ;

	if (undoRedo->redoSize == undoRedo->redoCapacity)
		resizeRedo(undoRedo);

	undoRedo->redoList[undoRedo->redoSize] = previousStage;
	undoRedo->redoSize++;
}

void clearRedoList(UndoRedo* undoRedo)
{
	if (undoRedo->redoList == NULL)
		return;

	for (int i = 0; i < undoRedo->redoSize; i++)
	{
		destroyDynamicArray(undoRedo->redoList[i]);
		undoRedo->redoList[i] = NULL;
	}
	undoRedo->redoSize = 0;
}

int undoOperation(UndoRedo* undoRedo, ProductRepository* repository)
{
	if (undoRedo->undoList == NULL || undoRedo == NULL)
		return -1;

	if (undoRedo->undoSize == 0)
		return 1;

	DynamicArray* previousStage = undoRedo->undoList[undoRedo->undoSize - 1];
	undoRedo->undoList[undoRedo->undoSize - 1] = NULL;
	undoRedo->undoSize--;
	addRedoStage(undoRedo, copyDynamicArray(repository->dynamicArray));
	destroyDynamicArray(repository->dynamicArray);
	repository->dynamicArray = previousStage;

	return 0;
}

int redoOperation(UndoRedo* undoRedo, ProductRepository* repository)
{
	if (undoRedo->redoList == NULL || undoRedo == NULL)
		return -1;

	if (undoRedo->redoSize == 0)
		return 1;

	DynamicArray* previousStage = undoRedo->redoList[undoRedo->redoSize - 1];
	undoRedo->redoList[undoRedo->redoSize - 1] = NULL;
	undoRedo->redoSize--;
	addUndoStage(undoRedo, copyDynamicArray(repository->dynamicArray));
	destroyDynamicArray(repository->dynamicArray);
	repository->dynamicArray = previousStage;

	return 0;
}


void testUndoRedo()
{
	UndoRedo* undoRedo = createUndoRedo();
	destroyUndoRedo(undoRedo);
}

