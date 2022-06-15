# console application
# given a string which represents arithmetic expression
# e.g. 2 + 4 * (3 + 4) / -34
# evaluate the expression

from interpertation.interpreter import Interpreter

def run():
    print("This is a simple interpreter. Write an expression to evaluete:")
    expr = input()
    interpreter = Interpreter()

    result = interpreter.interpret(expr)

    print(result)


if __name__ == '__main__':
    run()
