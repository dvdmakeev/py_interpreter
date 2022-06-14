from enum import Enum

class TokenType(Enum):
    Number = 0
    Operator = 1
    EOF = 2

class Token:
    value: str
    type: TokenType


class Lexer:
    def __init__(self, source) -> None:
        self.source = source

    def get_next() -> Token:
        pass
        
    def look_ahead() -> Token:
        pass
