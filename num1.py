import math

def func(a, b, x):
    if (3 * a) > b: return(round(math.log(x ** 2) - math.exp(x /3), 2))
    elif 3 * a <= b: return(round(math.atan(2 * x - 0.6), 2))
    else: return 'не удов. условиям'

print(func(
    int(input('число "а": ')),
    int(input('число "b": ')),
    int(input('число "x": '))
))
