import copy

totalTableColumnSize = 18


def addSpaces(number):
    result = ''
    for _ in range(number):
        result += ' '
    return result


class Table:

    def __init__(self, symbols):
        self.actionsForStates = {}
        self.stateToStateMap = {}
        self.symbolsToStateDefault = {}
        for symbol in symbols:
            self.symbolsToStateDefault[symbol] = -1

    def addSymbolToState(self, fromState, symbol, toState):
        if fromState not in self.stateToStateMap.keys():
            symbolsToState = copy.deepcopy(self.symbolsToStateDefault)
            self.stateToStateMap[fromState] = symbolsToState
            if self.stateToStateMap[fromState][symbol] == -1:
                self.stateToStateMap[fromState][symbol] = toState.index
        else:
            if self.stateToStateMap[fromState][symbol] == -1:
                self.stateToStateMap[fromState][symbol] = toState.index

    def addActionToState(self, fromState, action):
        self.actionsForStates[fromState] = action

    def isActionToStateDefined(self, fromState):
        return fromState in self.actionsForStates.keys()