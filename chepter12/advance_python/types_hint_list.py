#  advance type hinting with list


from typing import List, Optional      #Optional[int] → can return an int or None

# A list of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Add a new number
numbers.append(6)

# Function that takes a list of integers and returns the sum
def sum_list(nums: List[int]) -> int:
    return sum(nums)

# Function that returns the first element or None if the list is empty
def first_element(nums: List[int]) -> Optional[int]:      #Optional[int] → can return an int or None
    if nums:
        return nums[0]
    return None

# Using the functions
print("Numbers:", numbers)
print("Sum:", sum_list(numbers))
print("First element:", first_element(numbers))
print("First element of empty list:", first_element([]))




# other typing hints 

# tuple
from typing import Tuple
coordinates: tuple[int,int] = (1,2)
# mixed type tuple
mixed: tuple[str,int,float]= ("raman", 34, 23.5)

# function calculate distance
def calculate(p1:tuple[int,int],p2:tuple[int,int])->float:
    x1, y1 =p1
    x2, y2 =p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5
# a function that multiple values in a tuple

def divide(a:[int], b:[int])->tuple[int]:
 """Return quotient and remainder as a tuple."""
 return (a//b, a%b)

print("coordinates:", coordinates)
print("mixed tuple :", mixed)
print("calculate distance: ",calculate((1,2),(3,4)))
Quotient, remainder = divide(17,5)
print("Quotient:", Quotient)
print("Remainder:", remainder)


#Dictionary type hints

from typing import Dict

# A dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 80}

def add_score(data: Dict[str, int], name: str, score: int) -> Dict[str, int]:
    data[name] = score
    return data

print(add_score(scores, "Charlie", 85))


#Set — for unique values

from typing import Set

unique_ids: Set[int] = {101, 102, 103}

unique_ids.add(104)
print(unique_ids)


#Union — variable can have multiple types

from typing import Union

data: Union[int, str]

data = 10
print(data)

data = "hello"
print(data)
''' variable data can be int or str '''


#Optional — value can be None or something

from typing import Optional

def find_name(name: Optional[str] = None):
    if name:
        return f"Hello, {name}"
    return "Hello, Guest"

print(find_name())
print(find_name("Alice"))


# Callable — functions as arguments

from typing import Callable

def apply_operation(a: int, b: int, func: Callable[[int, int], int]) -> int:
    return func(a, b)

def multiply(x: int, y: int) -> int:
    return x * y

print(apply_operation(5, 3, multiply))





    




