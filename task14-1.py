# task1
def logger(func):
    def adder(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
    return adder

@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


num1 = 13
num2 = 56
res1 = add(num1, num2)
res2 = square_all(num1,num2)



