
def addition(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

def subtraction(a, b):
    """
    Returns the difference between two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The difference between a and b.
    """
    return a - b

def multiplication(a, b):
    """
    Returns the product of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The product of a and b.
    """
    return a * b

def division(a, b):
    """
    Returns the quotient of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The quotient of a and b.

    Raises:
    ValueError: If b is zero, raises a ValueError to indicate division by zero is not allowed.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """
    Returns the result of raising a to the power of b.

    Parameters:
    a (int or float): The base number.
    b (int or float): The exponent.

    Returns:
    int or float: The result of a raised to the power of b.
    """
    return a ** b

def square_root(a):
    """
    Returns the square root of a number.

    Parameters:
    a (int or float): The number to find the square root of.

    Returns:
    float: The square root of a.

    Raises:
    ValueError: If a is negative, raises a ValueError to indicate that square root of negative numbers is not allowed.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return a ** 0.5