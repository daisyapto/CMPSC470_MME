from functions import *
from tokenizer import Tokenizer
from translator import Translator

def main():
    tokenizer = Tokenizer()
    table = SymbolTable()
    functions = Functions(table)
    translator = Translator(table)

    exit_flag = False
    while not exit_flag:
        expression = input(">>> ")

        if expression == "exit":
            exit_flag = True
            continue

        tokens = tokenizer.tokenize(expression)

        result = translator.translate(tokens)
        print(result)


        if expression == "exit":
            exit_flag = True

if __name__ == "__main__":
    main()