# Simple Calculator Module
# A well-documented calculator with basic operations

def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b

def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    # Example usage
    print("Simple Calculator Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"5 / 3 = {divide(5, 3)}")
