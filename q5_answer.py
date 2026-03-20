def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

Attemmpted answers:

def check_divisibility(num, divisor):
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both num and divisor must be numeric")
    
    if divisor == 0:
        raise ValueError("divisor cannot be zero")
    
    return num % divisor == 0


# Invoke the function with the given scenarios
result1 = check_divisibility(10, 2)
result2 = check_divisibility(7, 3)

print(result1)
print(result2)

Output:
True
False

Explainations: 
The function allows us to ensure only numnbers are allowed and check if one number is divisiable by another set of number. 
In the above task, there is remainder for result1 so the output is true. 
For result2, there is a remainder and hence the output is false. 
We can also run the codes for numbers with decimal points which is useful during data analysis. 
