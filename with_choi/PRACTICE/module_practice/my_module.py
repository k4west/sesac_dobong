def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Multiplier:
    def __init__(self):
        pass

    def do(self, a, b):
        return a * b


def function():
    print("Function called!")


if __name__ == "__main__":
    print("mymodule is being run directly")
else:
    print("mymodule is being imported")
