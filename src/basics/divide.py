def divide(x: float, y: float) -> float:
    if y == 0:
        # return 1
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
