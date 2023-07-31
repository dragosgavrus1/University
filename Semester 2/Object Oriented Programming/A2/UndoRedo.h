#pragma once
#include "dynamicArray.h"
#include "productRepo.h"

typedef struct
{
	DynamicArray** undoList;
	int undoSize, undoCapacity;
	DynamicArray** redoList;
	int redoSize, redoCapacity;
}UndoRedo;

UndoRedo* createUndoRedo();
void destroyUndoRedo(UndoRedo* undoRedo);
void addUndoStage(UndoRedo* undoRedo, DynamicArray* previousStage);
void addRedoStage(UndoRedo* undoRedo, DynamicArray* previousStage);
void clearRedoList(UndoRedo* undoRedo);
int undoOperation(UndoRedo* undoRedo, ProductRepository* repository);
int redoOperation(UndoRedo* undoRedo, ProductRepository* repository);

void testUndoRedo();