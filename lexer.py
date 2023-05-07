import re

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
TT_float = "TT_float"
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
        self.filesContents = self.readFile()

    def readFile(self):
        with open(self.file, 'r') as f:
            return f.read()

    def deconstructCode(self):
        while len(self.filesContents) > 0:
            char = self.filesContents[0]
            if char == "=":
                self.tokens.append(Token(TT_assign, 10))
                self.filesContents = self.filesContents[1:]
            elif char == ")":
                self.tokens.append(Token(TT_rightBrac, 20))
                self.filesContents = self.filesContents[1:]
            elif char == "(":
                self.tokens.append(Token(TT_leftBrac, 30))
                self.filesContents = self.filesContents[1:]
            elif char == "+":
                self.tokens.append(Token(TT_plus, -5))
                self.filesContents = self.filesContents[1:]
            elif char == "-":
                self.tokens.append(Token(TT_minus, -10))
                self.filesContents = self.filesContents[1:]
            elif char == "*":
                self.tokens.append(Token(TT_times, -20))
                self.filesContents = self.filesContents[1:]
            elif char == "/":
                self.tokens.append(Token(TT_divide, -15))
                self.filesContents = self.filesContents[1:]
            elif char == '"':
                self.tokens.append(Token(TT_string, 20))
                self.filesContents = self.filesContents[1:]
                for char in self.filesContents:
                    if char == '"':
                        self.filesContents = self.filesContents[1:]
                        break
                    else:
                        self.filesContents = self.filesContents[1:]

            elif char == "'":
                self.tokens.append(Token(TT_string, 20))
                self.filesContents = self.filesContents[1:]
                for char in self.filesContents:
                    if char == "'":
                        self.filesContents = self.filesContents[1:]
                        break
                    else:
                        self.filesContents = self.filesContents[1:]

            elif re.match(r"\d", char):
                self.filesContents = self.filesContents[1:]
                floate = False
                for char in self.filesContents:
                    if re.match(r"\d", char):
                        floate = False
                        self.filesContents = self.filesContents[1:]
                    elif re.match(r".", char):
                        floate = False
                        self.filesContents = self.filesContents[1:]
                    else: 
                        break
                if floate == True:
                    self.tokens.append(Token(TT_float, 25))
                else:
                    self.tokens.append(Token(TT_integer, 30))
            else:
               self.filesContents = self.filesContents[1:] 

        return self.tokens
