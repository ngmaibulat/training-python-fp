from functools import partial


def multiply(x, y):
    """
    Multiplies two numbers and returns the result.

    Args:
        x (int or float): First number to be multiplied.
        y (int or float): Second number to be multiplied.

    Returns:
        int or float: The product of x and y.
    """
    return x * y


# Create a new function that multiplies by 2
double = partial(multiply, 2)
