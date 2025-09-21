from domain.item import Item
from domain.state import State
import copy

from domain.table import Table, addSpaces

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.addAugmentedProduction()
        self.items = []
        self.computeInitialLr0Items()
        self.canonicalCollection = []
        self.table = Table(self.grammar.N + self.grammar.E)

    def addAugmentedProduction(self):
        productions = {'S`': [(self.grammar.S, -1)]}
        productions.update(self.grammar.P)
        self.grammar.P = productions

    def computeInitialLr0Items(self):
        for lhs in self.grammar.P:
            for rhs in self.grammar.P[lhs]:
                self.items.append(Item(lhs, rhs[0], self.grammar.N + self.grammar.E))

    def closure(self, itemList):
        items = itemList.copy()
        while True:
            itemsAtIterationStart = items.copy()
            for item in itemsAtIterationStart:
                if item.isDotAtTheEnd():
                    # dot position is at the end
                    continue
                if item.getSymbolAfterDot() in self.grammar.N:
                    # non-terminal follows dot
                    for otherItem in self.items:
                        if otherItem.lhs == item.getSymbolAfterDot() and otherItem not in items:
                            items.append(otherItem)
            if itemsAtIterationStart == items:
                break
        if items[0].lhs == 'S`':
            return State(items, len(self.canonicalCollection))
        for state in self.canonicalCollection:
            # if an identical state already exists, don't create a new one
            if state.items == items:
                return state
        return State(items, len(self.canonicalCollection))

    def isInCanonicalCollection(self, state):
        for other in self.canonicalCollection:
            if state.items == other.items:
                return True
        return False

    def computeCanonicalCollection(self):
        # add initial state - closure of augmented production
        self.canonicalCollection.append(self.closure([self.items[0]]))
        while True:
            canonicalCollectionAtIterationStart = self.canonicalCollection.copy()
            for state in canonicalCollectionAtIterationStart:
                for symbol in self.grammar.N + self.grammar.E:
                    gotoResult = self.goTo(state, symbol)
                    if gotoResult != [] and not self.isInCanonicalCollection(gotoResult):
                        self.canonicalCollection.append(gotoResult)
            if canonicalCollectionAtIterationStart == self.canonicalCollection:
                break
        self.printCanonicalCollection()

    def goTo(self, state, symbol):
        items = []
        for item in state.items:
            # dot position is at the end
            if item.isDotAtTheEnd():
                continue
            if item.getSymbolAfterDot() == symbol:
                newItem = copy.deepcopy(item)
                newItem.moveDot()
                items.append(newItem)
        if items:
            gotoResult = self.closure(items)
            if gotoResult:
                self.table.addSymbolToState(state, symbol, gotoResult)
            return gotoResult
        else:
            return []

    def computeTableActions(self):
        for state in self.canonicalCollection:
            item = state.items[0]
            if item.lhs == 'S`' and item.isDotAtTheEnd():
                self.table.addActionToState(state, 'acc')
            elif item.isDotAtTheEnd():
                reduceValue = -1
                for rhs in self.grammar.P[item.lhs]:
                    if item.rhs == rhs[0]:
                        reduceValue = rhs[1]
                if self.table.isActionToStateDefined(state):
                    raise RuntimeError
                self.table.addActionToState(state, 'reduce' + str(reduceValue))
            else:
                if self.table.isActionToStateDefined(state):
                    raise RuntimeError
                self.table.addActionToState(state, 'shift')

    def buildInputStack(self, sequence):
        inputStack = []
        index = 0
        while index != len(sequence):
            nextPossibleSymbol = sequence[index:]
            while nextPossibleSymbol not in self.grammar.E + self.grammar.N:
                nextPossibleSymbol = nextPossibleSymbol[:-1]
            index += len(nextPossibleSymbol)
            inputStack.append(nextPossibleSymbol)
        return inputStack

    def getStateHavingIndex(self, index):
        for state in self.canonicalCollection:
            if state.index == index:
                return state

    def parseSequence(self, sequence):
        global topOfInputStack
        workingStack = [0]
        inputStack = self.buildInputStack(sequence)
        outputStack = []

        while True:
            print(str(workingStack) + addSpaces(30 - len(str(workingStack))) + ' | ' + str(inputStack) + addSpaces(
                30 - len(str(inputStack))) + ' | ' + str(outputStack))
            if len(inputStack):
                topOfInputStack = inputStack.pop(0)
            else:
                topOfInputStack = None
            topOfWorkingStack = workingStack[-1]
            currentState = self.getStateHavingIndex(topOfWorkingStack)
            currentAction = self.table.actionsForStates[currentState]
            if currentAction == 'shift' and topOfInputStack is not None:
                workingStack.append(topOfInputStack)
                workingStack.append(self.table.stateToStateMap[currentState][topOfInputStack])
            elif 'reduce' in currentAction:
                if topOfInputStack is not None:
                    inputStack.insert(0, topOfInputStack)
                production = self.grammar.getProductionAsPair(int(currentAction[len('reduce'):]))
                reduceTo, reduceFrom = production
                outputStack.insert(0, currentAction[6:])
                for symbol in reduceFrom[::-1]:
                    while workingStack[-1] != symbol:
                        workingStack.pop()
                    workingStack.pop()
                topOfWorkingStack = workingStack[-1]
                workingStack.append(reduceTo)
                currentState = self.getStateHavingIndex(topOfWorkingStack)
                workingStack.append(self.table.stateToStateMap[currentState][reduceTo])
            elif currentAction == 'acc' and topOfInputStack is None:
                break
            else:
                raise RuntimeError('The sequence in not accepted')

        print('\nFinal output: ' + str(outputStack))

    def printCanonicalCollection(self):
        result = ''
        for state in self.canonicalCollection:
            result += repr(state)
            result += '\n'
        print(result[:-1])