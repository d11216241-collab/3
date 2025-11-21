"""
Safe Division Module

This module provides a safe_division function that prevents division by zero errors.
"""

from typing import Union, Optional


def safe_division(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """
    Safely divide two numbers, preventing division by zero.
    
    Args:
        a (Union[int, float]): The dividend (numerator)
        b (Union[int, float]): The divisor (denominator)
    
    Returns:
        float: The result of a / b if b is not zero
        None: If b is zero (to prevent ZeroDivisionError)
    
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
