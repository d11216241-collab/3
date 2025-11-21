"""
Safe Division Module

This module provides a safe_division function that prevents division by zero errors.
"""


def safe_division(a, b):
    """
    Safely divide two numbers, preventing division by zero.
    
    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)
    
    Returns:
        The result of a / b if b is not zero
        None if b is zero (to prevent ZeroDivisionError)
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    if b == 0:
        return None
    return a / b
