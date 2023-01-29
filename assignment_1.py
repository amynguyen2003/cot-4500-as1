#COT4500 Assignment 1

import numpy as np
import math
import decimal

def questions_1_to_4():
    sign = 0
    integer = 10000000111
    y, x = 0, 0
    while(integer != 0):
        exponent = integer % 10
        y = y + exponent * pow(2, x)
        integer = integer//10
        x = x + 1

    dec = str(1110101110010000000000000000000000000000000000000000)
    d = 0
    x = 1
    for item in dec:
        d = d + int(item) * (0.5**x)
        x = x + 1

    #1.
    n = ((1 + d)*(-1)**sign)*(2**(y - 1023))
    m = n
    print("1:", "{:.5f}".format(n))
    print("\n")

    #2. 
    n = n * (10**-3)
    print("2:", (math.floor(n * 1000))/1000)
    print("\n")

    #3. 
    n = n + 0.0005
    print("3:", round(n, ndigits = 3))
    print("\n")

    #4.
    def absolute_error(value: float, approx: float):
        return abs(value - approx)
    
    def relative_error(value: float, approx: float):
        return abs((absolute_error(decimal.Decimal(value), decimal.Decimal(approx))) / decimal.Decimal(value))

    print("4:")
    print("Absolute Error:",  absolute_error(m, round(m, 0)) / 1000)
    print("Relative Error:",  relative_error(m, round(m, 0)))
    print("\n")

    return

questions_1_to_4()

#5.
def question_5():
    def series(i, j:int):
        return ((-1)**j) * ((i**j)/(j**3))

    error = 1e-4
    min_terms = 1
    while(abs(series(1, min_terms)) > error):
        min_terms = min_terms + 1

    print("5:", min_terms - 1)
    print("\n")

    return

question_5()

#6. 
def question_6():
    def question_6a(f, a, b, accuracy):
        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("The scalars a and b do not bound a root")
        num = (a + b) / 2
        if np.abs(a - b) <= accuracy:
            return 0
        elif np.sign(f(a)) == np.sign(f(num)):
            return question_6a(f, num, b, accuracy) + 1
        elif np.sign(f(b)) == np.sign(f(num)):
            return question_6a(f, a, num, accuracy) + 1
    
    def question_6b(f, df, initial, accuracy):
        result = f(initial) / df(initial)
        x = initial
        count = 1
        while(abs(result) >= accuracy):
            x = x - result
            count = count + 1
            result = f(x) / df(x)
        return count

    fx = lambda x : (x ** 3) + (4 * (x ** 2)) - 10
    dx = lambda x: 3 * (x ** 2) + (8 * x)
    print("6a:", question_6a(fx, -4, 7, 0.0001))
    print("6b:", question_6b(fx, dx, 7, 0.0001))
    print("\n")

question_6()
