a = 1
def f(g):
    a = 2
    return lambda y : a * g(y)
f(lambda a : a + y)(a)


"""观察以下代码的环境图"""
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake()

chocolate()

more_chocolate, more_cake = chocolate(), cake

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y

snake(10, 20)

snake(10, 20)()

cake = 'cake'
snake(10, 20)

"""--------------------------"""

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(g)(2)

"""--------------------------"""

call_thrice = lambda f: lambda x: f(f(f(x)))
call_thrice(lambda y: y + 1)(0)

"""--------------------------"""

n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)

