import lexer
if __name__ == "__main__":
    lexer = lexer.Lexer("main.py")
    for obj in lexer.deconstructCode():
        print(obj)
