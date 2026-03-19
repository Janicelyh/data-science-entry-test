def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

Attempted answer:

def string_reverse(s):
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    
    return s[::-1]


# Invoke the function with the given scenarios
result1 = string_reverse("Hello World")
result2 = string_reverse("Python")

print(result1)
print(result2)

Output:
dlroW olleH
nohtyP
