# Daisy Aptovska
# Symbol Table Assignment - MME
# Due: 4/3/26

import string

class SymbolTable:
    def __init__(self):
        self.symbolTable = dict()
        # From tokenizer.py submission
        self.keywords = ["solve", "simplify", "derive", "derivative", "integrate", "integral", "average", "mode", "max", "min"]
        self.helpers = ["for", "in", "the", 'expression', 'equation', 'of']
        self.variables = list(string.ascii_lowercase + string.ascii_uppercase)
        self.operators = ['=', '>', '<', '>=', '<=', '+', '-', '*', '/', '|', '^']
        self.comment = ['$', "$...", "...$"]
        self.sep = [':', ';']
        self.para = ['(', '{', '[', ')', '}', ']']
        self.tokenTypes = ['Helper', 'Keyword', 'Operator', 'Comment', 'Variable', 'Number', 'Seperator']

    # Google search AI Overview suggestion & function - create isfloat() function to check for isfloat since not built-in Python func
    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def enterEntry(self, name, entryType, category, value):
        # Entry format entry = {name : x, type : x, category : x, value (if applicable) : x}
        self.symbolTable[name] = {"Name" : name, "Type" : entryType, "Category" : category, "Value" : value}

    def getEntry(self, name):
        try:
            return self.symbolTable[name]
        except KeyError:
            return f"Error: attempted to obtain an invalid entry '{name}'"

    def editEntry(self, name, newName, newEntryType, newCategory, newValue):
        try:
            self.symbolTable[name] = {"Name" : newName, "Type" : newEntryType, "Category" : newCategory, "Value" : newValue}
        except KeyError:
            return f"Error: attempted to edit an invalid entry '{name}'"

    def deleteEntry(self, entry):
        try:
            del self.symbolTable[entry]
        except KeyError:
            return f"Error: attempted to delete an invalid entry '{entry}'"

    def testSymbolTable(self, testPrograms):
        # Entry tests
        for test in testPrograms:
            test = test.split()
            for item in test:
                name = item
                entryType = type(item)
                category = None
                value = None
                if item.lower() in self.keywords:
                    category = "Keyword"
                elif item.lower() in self.helpers:
                    category = "Helper"
                elif item in self.variables:
                    category = "Variable"
                elif item.lower() in self.operators:
                    category = "Operator"
                elif item.lower() in self.comment:
                    category = "Comment"
                elif item.lower() in self.sep:
                    category = "Separator"
                elif item.isdigit():
                    name = int(item)
                    entryType = int
                    category = "Integer"
                    value = item
                elif self.isfloat(item):
                    name = float(item)
                    entryType = float
                    category = "Float"
                    value = item
                elif item in self.para:
                    name = item
                    entryType = str
                    category = "Parentheses/Bracket/Brace"

                if category is not None:
                    self.enterEntry(name, entryType, category, value)
                else:
                    print("Error: improper syntax, must be of type: ", self.tokenTypes)

        print("Current Symbol Table: ", self.symbolTable)
        print("All entries successfully added to symbol table!")
        print()
        # Get tests
        for test in testPrograms:
            test = test.split()
            for item in test:
                if item.isdigit() or self.isfloat(item):
                    print(self.getEntry(float(item)))
                else:
                    print(self.getEntry(item))

        print("Current Symbol Table: ", self.symbolTable)
        print("All entries successfully obtained from symbol table!")
        print()
        # Edit tests
        count = 0
        for test in testPrograms:
            test = test.split()
            for item in test:
                count += 1
                self.editEntry(item, f"new_Name_Test_{count}", f"new_Entry_Type_Test_{count}", f"new_Category_Test_{count}", f"new_Value_Test_{count}")
                print(self.getEntry(item))
                
        print("Current Symbol Table: ", self.symbolTable)
        print("All entries successfully edited from symbol table!")
        print()
        # Delete tests
        for test in testPrograms:
            test = test.split()
            for item in test:
                if item in self.symbolTable:
                    self.deleteEntry(item)
                if self.isfloat(item):
                    self.deleteEntry(float(item))
        print("Current Symbol Table: ", self.symbolTable)
        print("All entries successfully deleted from symbol table!")
        print()

def main():
    symbolTable = SymbolTable()

    testProgram1 = "Solve for abcde : y = x + 1"
    testProgram2 = "Solve : 5 + 10.5"
    testProgram3 = "Simplify : ( x + 3 ) ^ 2"

    tests = [testProgram1, testProgram2, testProgram3]
    symbolTable.testSymbolTable(tests)

if __name__ == "__main__":
    main()

# References
# Google search AI Overview - syntax questions and symbol table design in compilers
# https://www.geeksforgeeks.org/compiler-design/symbol-table-compiler/
# https://en.wikipedia.org/wiki/Symbol_table
# https://docs.python.org/3/library/symtable.html
# https://github.com/daisyapto/CMPSC470_MME