from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    Number = 0
    Plus = 1
    Minus = 2
    Division = 3
    Mult = 4
    LeftBracket = 5
    RightBracket = 6
    EOF = 100

@dataclass
class Token:
    value: str or None
    type: TokenType


class Lexer:
    def __init__(self, source) -> None:
        self.source = source
        self.cur_pos = 0

    def get_next(self) -> Token:
        pos = self._skip_whitespaces(self.source, self.cur_pos)
        
        token = self._try_get_eof(self.source, pos)
        if not token:
            token = self._try_get_number(self.source, pos)
        if not token:
            token = self._try_get_reserved(self.source, pos)
        if not token:
            raise Exception()

        if token.value:
            self.cur_pos = pos + len(token.value)

        return token

        
    def look_ahead(self) -> Token:
        init_pos = self.cur_pos

        token = self.get_next()
        self.cur_pos = init_pos

        return token

    def _try_get_eof(self, source, pos) -> Token or None:
        return None if pos < len(source) else Token(value=None, type=TokenType.EOF)

    def _try_get_reserved(self, source, pos) -> Token or None:
        tokens = {
            '(': TokenType.LeftBracket,
            ')': TokenType.RightBracket,
            '+': TokenType.Plus,
            '-': TokenType.Minus,
            '*': TokenType.Mult,
            '/': TokenType.Division
        }

        tokenType = tokens.get(source[pos], None)
        if tokenType:
            return Token(source[pos], tokenType)

        return None

    def _try_get_number(self, source: str, pos: int) -> Token or None:
        if source[pos].isnumeric():
            return Token(source[pos], TokenType.Number)

        return None

    @staticmethod
    def _skip_whitespaces(src: str, pos: int) -> int:
        while pos < len(src) and src[pos].isspace():
            pos += 1
        return pos
