def fibonacci(n):
    """
    Recursive Fibonacci function.
    Returns the nth Fibonacci number.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Test the function
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
