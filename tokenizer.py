# Daisy Aptovska
# CMPSC 470 - Basic Expression Tokenizer
# Due: 3/19/26

# Literals: int, float
# Operators: =, <, >, <=, >=, +, -, *, /, |
# Seperators: :, ;, (, ), [, ], {, }
# Variables: [a/A - z/Z]
# Reserved words: ["Solve", "Simplify", "Derive", "Derivative", "Integrate", "Integral"]
# Helper words: ["for", "in"]
# Data types: keyword, variable, int, float, operator

# Sample input test data
# Solve for y : x = y + 1
# Simplify the expression  : ( x + 1 ) ^ 2
# + $... solve ...$
# $... solve ...$ +
# solve $ solve

# References:
# Immo Landwerth - Video 1 in Building a Compiler playlist
# Google search AI Overview - syntax questions

import string
from collections import Counter

class Tokenizer:
    def __init__(self):
        self.keywords = ["solve", "simplify", "derive", "derivative", "integrate", "integral", "average", "mode", "max", "min"]
        self.helpers = ["for", "in", "the", 'expression', 'equation', 'of']
        self.variables = list(string.ascii_lowercase + string.ascii_uppercase)
        self.operators = ['=', '>', '<', '>=', '<=', '+', '-', '*', '/', '|', '^']
        self.comment = ['$', "$...", "...$"]
        self.sep = [':', ';']
        self.lines = 1

    def isKeyword(self, word):
        if word in self.keywords:
            return True
        else:
            return False

    def isInt(self, literal):
        if type(literal) == int:
            return True
        else:
            return False

    def isFloat(self, literal):
        if type(literal) == float:
            return True
        else:
            return False

    def tokenize(self, phrase):
        tokens = phrase.split()
        """ Tested, chose to split by spaces instead so that operators can be identified
        if ":" in phrase:
            tokens = phrase.split(":")
        else:
            return "Error: Invalid phrase format, lacking ':' seperator"
        if tokens[0].split()[0] in self.keywords:
            if '=' in tokens[1]:
                tokens[1] = tokens[1].split('=')
            elif '>' in tokens[1]:
                tokens[1] = tokens[1].split('>')
            elif '<' in tokens[1]:
                tokens[1] = tokens[1].split('<')
            elif '<=' in tokens[1]:
                tokens[1] = tokens[1].split('<=')
            elif '>=' in tokens[1]:
                tokens[1] = tokens[1].split('>=')
            else:
                return "Error: Invalid expression/equation, no operator"
        else:
            return "Error: Invalid keyword/keyphrase"
        """
        return tokens

    def identify(self, tokens):
        result = []
        for token in tokens:
            if (result.count("Comment") % 2) == 0:
                if token.lower() in self.helpers:
                    result.append("Helper")
                if token.lower() in self.keywords:
                    result.append("Keyword")
                if token.lower() in self.variables:
                    result.append("Variable")
                if token.lower() in self.operators:
                    result.append("Operator")
                if token.lower() in self.sep:
                    result.append("Separator")
                if token.isnumeric():
                    result.append("Number")
            if token in self.comment:
                if token == "$":
                    result.append("Comment")
                    break
                if token == "$..." or token == "...$":
                    result.append("Comment")
            if token == "\n":
                self.lines += 1
        counts = Counter(result)
        return counts, result

"""
def main():
    tokenizer = Tokenizer()
    testPhrase = "start"
    while testPhrase != "-1":
        testPhrase = input("Enter a phrase to test with MME (-1 to exit): ")
        if testPhrase != "-1":
            tokens = tokenizer.tokenize(testPhrase)
            print(tokens)
            result = tokenizer.identify(tokens)
            for var, count in result[0].items():
                print(f"{var}: {count}")
            print(result[1])
            print("Number of lines: ", tokenizer.lines)

if __name__ == "__main__":
    main()
"""