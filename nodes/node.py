from abc import abstractclassmethod

class Node:
    @abstractclassmethod
    def evaluate():
        pass

class Factor(Node):
    pass

class Expression(Node):
    pass

class BinaryExpression(Expression):
    pass

class UnaryExpression(Expression):
    pass