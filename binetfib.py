"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
script to test how python code 
executes on the TI-84
"""


def sq_rt(val: float):
    """
    function obtained from https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python#:~:text=Also%20there%20are%20other%20methods,square%20roots%20like%20shown%20here.&text=here%20is%20the%20way%20you,any%20inbuilt%20function%20of%20python.&text=Basically%20the%20program%20run%20for,true%20%2D%20return%20i%20and%20break
    """
    x_val = val
    y_val = 1.000000  # iteration initialisation.
    e_val = 0.000001  # accuracy after decimal place.
    while x_val-y_val > e_val:
        x_val = (x_val+y_val)/2
        y_val = val/x_val
    return x_val


def abs_val(val: float):
    """
    return the absolute value of 
    a number
    """
    if val < 0:
        return val * -1
    return val


def power(val: float, expo: float) -> float:
    """
    function obtained from https://stackoverflow.com/questions/5246856/how-did-python-implement-the-built-in-function-pow
    """
    p_value = 1
    if expo < 0:
        val = 1/val
        # ? might need to make an absolute value function
        expo = abs_val(expo)

    # Exponentiation by Squaring

    while expo:
        if expo % 2:
            p_value *= val
        val *= val
        expo //= 2
    return p_value


def fib(nth: int) -> int:
    """
    output the nth term of the fibonacci sequence
    using Binet's formula
    """
    a_value = (1+sq_rt(5))/2
    b_value = (1-sq_rt(5))/2
    m_flt = power(a_value, nth)
    n_flt = power(b_value, nth)
    return int((m_flt - n_flt) / (sq_rt(5)))


def isinputvalid(uinput: str) -> bool:
    """
    validate user input by 
    making sure it only has 
    integers in its input
    """
    for character in uinput:
        if not character in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return False
    return True


# main script
print('PRESS 2ND + MODE/QUIT TO STOP\nTWICE RUNNING PROCESS')
print('NTH : TERM')
while True:
    while True:
        limit = input('NTH TERM DESIRED: ').strip()
        if not isinputvalid(limit):
            print('ERROR - ONLY TYPE NUMBERS IN INPUT')
        else:
            limit = int(limit)
            break
    print(limit, ':', fib(limit))
# end of main script
