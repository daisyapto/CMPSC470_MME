from symbolTable import SymbolTable
# https://www.geeksforgeeks.org/python/python-getting-started-with-sympy-module/
# Use the above link to build the functions for the translator

class Functions:
    def __init__(self, expression):
        self.expression = expression
        self.symbolTable = SymbolTable()

    def getFunction(self):
        return self.symbolTable.getEntry(self.expression)


