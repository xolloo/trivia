from functools import singledispatch
from decimal import Decimal


@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported type")


@add.register(int)
def _(a, b):
    print(type(a))
    return a + b


@add.register(str)
def _(a, b):
    print(type(a))
    return "{} | {}".format(a, b)


@add.register(list)
def _(a, b):
    print(type(a))
    return a + b


@add.register(dict)
def _(a, b):
    print(type(b))
    return "{} + {}".format(a, b)


@add.register(float)
@add.register(Decimal)
def _(a, b):
    print(type(a))
    return a * b

if __name__ == "__main__":
    print(add(1, 2))
    print(add("str", "str"))
    print(add([1, 2, 3], [4, 5]))

    print(add({}, 5))
    print(add(.4, 5.6))
