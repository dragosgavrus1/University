from hashtable import HashTable


class ConstantSymbolTable:
    def __init__(self):
        self.table = HashTable()

    def add_constant(self, name, value):
        self.table.insert(name, value)

    def get_constant(self, name):
        return self.table.get(name)
    
    def get_position(self, identifier):
        return self.table.get_position(identifier)


class IdentifierSymbolTable:
    def __init__(self):
        self.table = HashTable()

    def add_identifier(self, name, value):
        self.table.insert(name, value)

    def get_identifier_value(self, name):
        return self.table.get(name)

    def get_position(self, identifier):
        return self.table.get_position(identifier)