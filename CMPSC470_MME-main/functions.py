from symbolTable import SymbolTable
# https://www.geeksforgeeks.org/python/python-getting-started-with-sympy-module/
# Use the above link to build the functions for the translator
from sympy import symbols, diff, integrate, solve, simplify, Eq, sympify
from collections import Counter

class Functions:
    def __init__(self, table):
        # Unsure how to get symbol table type of token so it knows what function to call
        # Need to find a way in symbol table where tokens[0] is accessed,
        # value is returned, and thus the word ("Solve", or "Avg") is found as the token
        # and it knows to call which function from Functions class
        self.symbolTable = table

    # Need to make this work with tokenizer, possibly remerging into cohesive string, or change tokenizer to split by ":" to extract equation as 1 string
    def form(self, eq, sym=None):
        # Split equation string into left-hand side and right-hand side
        left, right = eq.split("=")

        # Remove any extra spaces
        left = left.strip()
        right = right.strip()

        lhs = symbols(left) # Convert left side into a symbolic variable
        rhs = sympify(right) # Convert right side string into a SymPy expression

        equation = Eq(lhs, rhs)
        if sym:
            sym_var = symbols(sym) # Convert string variable (e.g., "x") into a SymPy symbol
            return equation, sym_var
        else:
            # If no variable is specified, default to using the LHS variable
            return equation, lhs

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
        eq, _ = self.form(equation)
        return simplify(eq.rhs)

    def derive(self, equation, sym):
        eq, sym_var = self.form(equation, sym)
        return diff(eq.rhs, sym_var)

    def integrate(self, equation, sym):
        eq, sym_var = self.form(equation, sym)
        return integrate(eq.rhs, sym_var)

# Sample testing
# funcs = Functions()
# equationText = 'y = x + 1'
# symbolText = 'x'
#
# print(funcs.derive(equationText, symbolText))
# Unsure how to debug, how to replace string "x" with type symbol x