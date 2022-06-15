from lexing.lexer import Lexer, Token, TokenType
from nodes.node import Node

class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer

    def parse(self) -> Node:
        token = self.lexer.get_next()
        while token.type is not TokenType.EOF:
            token = self.lexer.get_next()
