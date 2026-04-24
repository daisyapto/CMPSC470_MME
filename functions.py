from symbolTable import SymbolTable
# https://www.geeksforgeeks.org/python/python-getting-started-with-sympy-module/
# Use the above link to build the functions for the translator
from sympy import symbols, diff, integrate, solve, simplify, Eq
from collections import Counter

class Functions:
    def __init__(self):
        # Unsure how to get symbol table type of token so it knows what function to call
        # Need to find a way in symbol table where tokens[0] is accessed,
        # value is returned, and thus the word ("Solve", or "Avg") is found as the token
        # and it knows to call which function from Functions class
        self.symbolTable = SymbolTable()

    # Need to make this work with tokenizer, possibly remerging into cohesive string, or change tokenizer to split by ":" to extract equation as 1 string
    def form(self, eq, sym=None): # This function is essential bc it can convert the string (i.e. 'x') to type symbols(x) and same for the equation string (i.e. 'y = x + 1') into type equation(eq)
        eqSplit = eq.split(" = ") # this will split "y = x + 1" into ["y", "x+1"] which is the type of input needed for Eq(input1, input2) --> input1 = input2
        if sym is None:
            sym = symbols(eqSplit[0])
        else:
            syms = symbols(f'{sym}, {eqSplit[0]}')

        equation = Eq(syms[1], eqSplit[1])

        return equation, symbols

    def average(self, vals): # vals must be past the : --> for example, access this list token "Avg: [3, 5, 7]"
        return sum(vals) / len(vals)

    def mode(self, vals):
        counts = Counter(vals)
        return counts.most_common(1)[0][0]

    def maximum(self, vals):
        return max(vals)

    def minimum(self, vals):
        return min(vals)

    def solve(self, equation, sym):
        equation, syms = self.form(equation, sym)
        return solve(equation, syms)

    def simplify(self, equation):
        equation, syms = self.form(equation)
        return simplify(equation)

    def derive(self, equation, sym):
        equation, syms = self.form(equation, sym)
        return diff(equation, syms)

    def integrate(self, equation, sym):
        equation, syms = self.form(equation, sym)
        return integrate(equation, syms)

# Sample testing
funcs = Functions()
equationText = 'y = x + 1'
symbolText = 'x'

print(funcs.derive(equationText, symbolText))
# Unsure how to debug, how to replace string "x" with type symbol x