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

Explainations: 
The above coding functions allows us to revese text strings and is useful when doing data slicing for text analysis.  
We can also do palindromes checks to normalise a string of text. The invoke functions calls out the string of text where we want to reverse or 
do palimdromes checks. This coding is usful when doing data cleaning for string text to slice out meaningful insiights for reporting eventually. 
                                                                                                 

                                                                                                 

