def largest_divisible(x, y):
    """Determine the largest number divisible by a provided number 
    for a provided number of digits

    Parameters:
    x (int): Number to check
    y (int): Number of digits

    Returns:
    int:Return largest divisible value
    
    """
    
    #Determine max value for y digits
    MAX = pow(10, y) - 1
     
    return (MAX - (MAX % x))

def smallest_divisible(x, y):
    """Determine the smallest number divisible by a provided number
    for a provided number of digits

    Parameters:
    x (int): Number to check
    y (int): Number of digits

    Returns:
    int: Returns smallest divisible value
    """

    #Determine the max value for y digits
    MIN = pow(10, y-1)

    if (MIN % x == 0):
        return MIN
    else:
        return (MIN + x) - ((MIN + x) % x)

    return x

def fibonacci(n):
    if n < 0:
        return 'please give >=0'
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n-1)
