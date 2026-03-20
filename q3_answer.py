def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

Attempted answer:

def update_dictionary(dct, key, value):
    if not isinstance(dct, dict):
        raise TypeError("dct must be a dictionary")
    
    if key in dct:
        print("Original value:", dct[key])
    
    dct[key] = value
    return dct


# Invoke the function with the given scenarios
result1 = update_dictionary({}, "name", "Alice")
result2 = update_dictionary({"age": 25}, "age", 26)

print(result1)
print(result2)

Output:
Original value: 25
{'name': 'Alice'}
{'age': 26}

Explainations: 
This function allows us to do updates within the dataset and tracking the changes made. 
This is important to ensure data accuracy within the dataset.
The invoke function calls out the variables that needed to changes and allows users to change the age of the Alice 
from 25 to 26 while tracking the orignal values. 
