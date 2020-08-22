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

def fibonacci_sequence(n):
    def fibonacci(y):
        if y <= 1:
            return y
        else:
            return fibonacci(y-2) + fibonacci(y-1)
    if n < 0:
        print('please provide a value >=0')
    else:
        for i in range(n):
            f = fibonacci(i)
            if f <= n: print(f)
            else: break

