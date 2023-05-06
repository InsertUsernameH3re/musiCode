TT_varName = "TT_varName"
TT_assign = "TT_assign"
TT_leftBrac = "TT_leftBrac"
TT_rightBrac = "TT_rightBrac"
TT_string = "TT_string"
TT_plus = "TT_plus"
TT_minus = "TT_minus"
TT_times = "TT_times"
TT_divide = "TT_divide"
TT_output = "TT_output"
TT_integer = "TT_integer"
TT_cannotRead = "TT_cannotRead"


class Token:
    def __init__(self, type, pitch):
        self.type = type
        self.pitch = pitch

    def __str__(self):
        return f"{self.type} {self.pitch}"


class Lexer:
    def __init__(self, file):
        self.file = file
        self.tokens = []

    def readFile(self):
        with open(self.file, 'r') as f:
            return f.read()

    def deconstructCode(self):
        filesContents = self.readFile()
        for char in filesContents:
            if char == "=":
                self.tokens.append(Token(TT_assign, 10))
            elif char == ")":
                self.tokens.append(Token(TT_rightBrac, 20))
            elif char == "(":
                self.tokens.append(Token(TT_leftBrac, 30))
            elif char == "+":
                self.tokens.append(Token(TT_plus, -5))
            elif char == "-":
                self.tokens.append(Token(TT_minus, -10))
            elif char == "*":
                self.tokens.append(Token(TT_times, -20))
            elif char == "/":
                self.tokens.append(Token(TT_divide, -15))
            else:
                self.tokens.append(Token(TT_cannotRead, -20))
        return self.tokens
