from lexing.lexer import Lexer
from parsing.parser import Parser

class Interpreter:

    def __init__(self) -> None:
        return

    def interpret(self, source: str) -> int:
        lexer = Lexer(source)
        parser = Parser(lexer)

        node = parser.parse()
        return node.evaluate()
