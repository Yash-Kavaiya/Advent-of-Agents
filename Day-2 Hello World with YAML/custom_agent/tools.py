"""Custom tools for the calculator agent."""

import math
from typing import Union


def calculate(expression: str) -> dict:
    """
    Evaluate a mathematical expression safely.
    
    Args:
        expression: A math expression like "2 + 2" or "sqrt(16) * 3"
    
    Returns:
        dict with 'result' or 'error' key
    
    Examples:
        calculate("2 + 2") -> {"result": 4, "expression": "2 + 2"}
        calculate("sqrt(16)") -> {"result": 4.0, "expression": "sqrt(16)"}
    """
    # Define safe mathematical functions
    safe_functions = {
        # Basic operations
        'abs': abs,
        'round': round,
        'min': min,
        'max': max,
        'sum': sum,
        'pow': pow,
        
        # Math module functions
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log,
        'log10': math.log10,
        'log2': math.log2,
        'exp': math.exp,
        'floor': math.floor,
        'ceil': math.ceil,
        
        # Constants
        'pi': math.pi,
        'e': math.e,
    }
    
    try:
        # Safely evaluate the expression
        result = eval(expression, {"__builtins__": {}}, safe_functions)
        return {
            "success": True,
            "result": result,
            "expression": expression
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "expression": expression
        }


def is_prime(numbers: list[int]) -> dict:
    """
    Check if numbers are prime.
    
    Args:
        numbers: List of integers to check
    
    Returns:
        dict with results for each number and list of primes
    
    Examples:
        is_prime([2, 3, 4, 5]) -> {
            "results": {2: True, 3: True, 4: False, 5: True},
            "primes": [2, 3, 5],
            "not_primes": [4]
        }
    """
    def check_prime(n: int) -> bool:
        """Check if a single number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    results = {num: check_prime(num) for num in numbers}
    
    return {
        "results": results,
        "primes": [num for num, is_p in results.items() if is_p],
        "not_primes": [num for num, is_p in results.items() if not is_p],
        "count": {
            "total": len(numbers),
            "primes": sum(1 for is_p in results.values() if is_p),
            "not_primes": sum(1 for is_p in results.values() if not is_p)
        }
    }


def factorial(n: int) -> dict:
    """
    Calculate the factorial of a number.
    
    Args:
        n: Non-negative integer
    
    Returns:
        dict with factorial result
    """
    if n < 0:
        return {"success": False, "error": "Factorial not defined for negative numbers"}
    if n > 170:
        return {"success": False, "error": "Number too large (max 170)"}
    
    return {
        "success": True,
        "n": n,
        "factorial": math.factorial(n)
    }


def fibonacci(n: int) -> dict:
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n: Number of terms to generate
    
    Returns:
        dict with Fibonacci sequence
    """
    if n <= 0:
        return {"success": False, "error": "n must be positive"}
    if n > 100:
        return {"success": False, "error": "n too large (max 100)"}
    
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return {
        "success": True,
        "n": n,
        "sequence": sequence,
        "sum": sum(sequence)
    }