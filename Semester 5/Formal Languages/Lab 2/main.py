from hashtable import HashTable
from symboltables import IdentifierSymbolTable, ConstantSymbolTable

def main():
    identifiers = IdentifierSymbolTable()
    identifiers.add_identifier("x", 5)
    print(identifiers.get_identifier_value("x"))

    constants = ConstantSymbolTable()
    constants.add_constant(10, 15)
    print(constants.get_constant(10))

    table = HashTable()
    table.insert("m", 7)
    print(table.get("m"))


    
if __name__ == "__main__":
    main()