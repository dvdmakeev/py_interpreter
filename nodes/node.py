from abc import abstractclassmethod

class Node:
    @abstractclassmethod
    def evaluate() -> int:
        pass

class Expression(Node):
    pass

class Factor(Expression):
    pass

class BinaryExpression(Expression):
    pass

class UnaryExpression(Expression):
    pass