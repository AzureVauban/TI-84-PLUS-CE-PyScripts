"""
script to test how python code executes on the TI-84
- need non-standard lib square root & power function
"""

#!import math


def sqroot(value: float) -> float:
    """
    function obtained from https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python#:~:text=Also%20there%20are%20other%20methods,square%20roots%20like%20shown%20here.&text=here%20is%20the%20way%20you,any%20inbuilt%20function%20of%20python.&text=Basically%20the%20program%20run%20for,true%20%2D%20return%20i%20and%20break
    """
    x_val = value
    y_val = 1.000000  # iteration initialisation.
    e_val = 0.000001  # accuracy after decimal place.
    while x_val-y_val > e_val:
        x_val = (x_val+y_val)/2
        y_val = value/x_val
    return x_val


def abs_value(value: float) -> float:
    """
    return the absolute value of a function
    """
    if value < 0:
        return value * -1
    return value


def power(value: float, exponent: float) -> float:
    """
    function obtained from https://stackoverflow.com/questions/5246856/how-did-python-implement-the-built-in-function-pow
    """
    p_value = 1
    if exponent < 0:
        value = 1/value
        # ? might need to make an absolute value function
        exponent = abs_value(exponent)

    # Exponentiation by Squaring

    while exponent:
        if exponent % 2:
            p_value *= value
        value *= value
        exponent //= 2
    return p_value


def fib(nth_term: int) -> int:
    """
    output the nth term of the fibonacci sequence
    using Binet's formula
    """
    a_value = (1+sqroot(5))/2
    b_value = (1-sqroot(5))/2
    m_flt = power(a_value, nth_term)
    n_flt = power(b_value, nth_term)
    return int((m_flt - n_flt) / (sqroot(5)))


# main script
limit = input('TEST PROMPT: ')
print(int(limit), ':', fib(int(limit)))
