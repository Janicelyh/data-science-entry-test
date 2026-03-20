class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def describe_car(self):
        print("")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

Attempted answers: 

 class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Create an instance of Car
car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()
Output:
2020 Toyota Corolla

Explainations: 
The purpose of this coding function is to allow us to create a readable descriptions of the datasets that we will be working on. 
This coding is useful for us to create key attributes within the raw dataset which helps to make the data more meaningful when doing analysis.  
We are also able to easily extract and provide detailed information through the attributes if needed from the datset.    
In the above task 1, it allows us to create the key attributes of the car by make, model and year which helps to extract the car information easily from 
the dataset. Meanwhile task 2, it is used to call out the specific car attributes that we have created in task 1. 
In the event if we only create the attributes in task 1 but didnt create an instance/ call a method to call out the information, the program will 
not be to produce any output. 
