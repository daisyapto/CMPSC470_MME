from functions import Functions
from tokenizer import Tokenizer


class Translator:
    def __init__(self, table):
        self.table = table
        self.functions = Functions(table)
        self.tokenizer = Tokenizer()


    def translate(self, tokens):
        # Empty - no tokens
        if not tokens:
            return "Error: No input"

        command = tokens[0].lower()

        # Handler for different keywords
        if command == "solve":
            return self._handle_solve(tokens)

        elif command == "simplify":
            return self._handle_simplify(tokens)

        elif command in ["derive", "derivative"]:
            return self._handle_derive(tokens)

        elif command in ["integrate", "integral"]:
            return self._handle_integrate(tokens)

        elif command == "average":
            return self._handle_average(tokens)

        elif command == "mode":
            return self._handle_mode(tokens)

        elif command == "max":
            return self._handle_max(tokens)

        elif command == "min":
            return self._handle_min(tokens)

        else:
            return "Error: Unknown command"

    # Get equation from line
    def _extract_equation(self, tokens):
        if ":" in tokens:
            idx = tokens.index(":")
            return " ".join(tokens[idx + 1:])
        return None

    # Get numbers from line
    def _extract_numbers(self, tokens):
        nums = []
        for t in tokens:
            try:
                if "." in t:
                    nums.append(float(t))
                else:
                    nums.append(int(t))
            except:
                continue
        return nums

    # Get symbols from line
    def _extract_symbol(self, tokens):
        if "for" in tokens:
            idx = tokens.index("for")
            return tokens[idx + 1]
        return None

    # If equation and symbols are valid, then run solve function
    def _handle_solve(self, tokens):
        equation = self._extract_equation(tokens)
        symbol = self._extract_symbol(tokens)
        if equation and symbol:
            return self.functions.solve(equation, symbol)
        return "Error: Invalid solve format"

    # If equation, simplify it
    def _handle_simplify(self, tokens):
        equation = self._extract_equation(tokens)
        if equation:
            return self.functions.simplify(equation)
        return "Error: Invalid simplify format"

    # If equation, derive it
    def _handle_derive(self, tokens):
        equation = self._extract_equation(tokens)
        symbol = self._extract_symbol(tokens)
        if equation and symbol:
            return self.functions.derive(equation, symbol)
        return "Error: Invalid derive format"

    # If equation, integrate it
    def _handle_integrate(self, tokens):
        equation = self._extract_equation(tokens)
        symbol = self._extract_symbol(tokens)
        if equation and symbol:
            return self.functions.integrate(equation, symbol)
        return "Error: Invalid integrate format"

    # If numbers, get average
    def _handle_average(self, tokens):
        nums = self._extract_numbers(tokens)
        if nums:
            return self.functions.average(nums)
        return "Error: No numbers found"

    # If numbers, get mode
    def _handle_mode(self, tokens):
        nums = self._extract_numbers(tokens)
        if nums:
            return self.functions.mode(nums)
        return "Error: No numbers found"

    # If numbers, get max
    def _handle_max(self, tokens):
        nums = self._extract_numbers(tokens)
        if nums:
            return self.functions.maximum(nums)
        return "Error: No numbers found"

    # If numbers, get min
    def _handle_min(self, tokens):
        nums = self._extract_numbers(tokens)
        if nums:
            return self.functions.minimum(nums)
        return "Error: No numbers found"

    def test(self): # Crucial function for testing; simply run the "MME.py" and type "test mode" to test every function with a sample code statement in MME
        # Provides syntax guidance on how to use all the functions
        TEST_CODE = [
            "Solve for x : y = x + 1",
            "Simplify : y = x + 1 + 2",
            "Derive for x : y = x^2 + 1",
            "Integrate for x : y = x^2 + 1",
            "Average : [3, 5, 7]",
            "Mode : [3, 5, 5, 7]",
            "Max : [3, 5, 7]",
            "Min : [3, 5, 7]",
        ]
        for statement in TEST_CODE:
            tokens = self.tokenizer.tokenize(statement)
            print("Testing the following statement: ", statement)
            print("Tokens: ", tokens)
            result = self.translate(tokens)
            print("Result: ", result)
        print("Test model successfully completed!")