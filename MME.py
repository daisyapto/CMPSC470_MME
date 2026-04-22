from tokenizer import *
from symbolTable import SymbolTable
from functions import *
from tokenizer.tokenizer import Tokenizer
from translator import *

def main():
    tokenizer = Tokenizer()
    table = SymbolTable()
    functions = Functions(table)
    #translator = Translator()

    exit_flag = False
    while not exit_flag:
        expression = input(">>> ")
        tokens = tokenizer.tokenize(expression)
        table.enterEntry(expression, tokens, type(expression), type(expression))
        table_entry = table.getEntry(expression)


        if expression == "exit":
            exit_flag = True

if __name__ == "__main__":
    main()