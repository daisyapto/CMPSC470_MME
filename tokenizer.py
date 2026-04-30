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

    def isFloat(self, token):
        try:
            float(token)
            return True
        except:
            return False

    def tokenize(self, phrase):
        # Protect multi-character operators
        phrase = phrase.replace(">=", " __GE__ ")
        phrase = phrase.replace("<=", " __LE__ ")

        # Single-char operators
        for op in ['=', '>', '<', '+', '-', '*', '/', '|', '^']:
            phrase = phrase.replace(op, f" {op} ")

        # Restore multi-character operators
        phrase = phrase.replace("__GE__", ">=")
        phrase = phrase.replace("__LE__", "<=")

        # Separators
        for s in self.sep:
            phrase = phrase.replace(s, f" {s} ")

        # Parentheses
        for p in ['(', ')', '{', '}', '[', ']']:
            phrase = phrase.replace(p, f" {p} ")

        phrase = " ".join(phrase.split())
        return phrase.split(" ")

    def identify(self, tokens):
        result = []

        for token in tokens:
            token_lower = token.lower()

            if token_lower in self.helpers:
                result.append("Helper")

            elif token_lower in self.keywords:
                result.append("Keyword")

            elif token in self.variables:
                result.append("Variable")

            elif token in self.operators:
                result.append("Operator")

            elif token in self.sep:
                result.append("Separator")

            elif token.isdigit():
                result.append("Number")

            elif self.isFloat(token):
                result.append("Float")

            else:
                result.append("Unknown")

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