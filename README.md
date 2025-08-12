***
# Basics of FastAPI
***
...

...

...

# Built-in functions

## print()
* Outpus a specified object to the screen
* Receives the object you want to print as an argument
* Takes any number of arguments, separated by a comma. Prints all arguments

```python
month = "August"
print("Investigate failed jobs during", month, "to detect possible recurrence.")
```
## type()
* Returns the data type of its argument
* Receives the object you want the type of as an argument, returns the data type.
* Takes only one argument

```python
month = "August"
print(type(month))

# Will return:
$ <class 'str'>
```

## str()
* Converts any data type to a string
* Takes only one argument, the object you want to convert to a string. Returns a `str()` representation of the argument

```python
month_num = 8
string_month_num = str(month_num)
print(month_num)
print(type(month_num))

# Will return 8 as a str
$ 8
$ <class 'str'>
```

## sorted()
* Sorts the components of a list
* It does not modify the order of the iterable
* Works on any iterable, like a string.
* Sorts in ascending order, ie; numbers are sorted from smallest to ragest.

```python
month_list = [10, 12, 1, 4, 3, 2]
print(sorted(month_list))

# Will return a sorted iterable
$ [1, 2, 3, 4, 10, 12]
```

## min() - max()
* Accept arguments of an iterable
* returns the largest or smallest value

```python
session_minutes = [65, 10, 120, 45, 30, 180, 115]
print(min(session_minutes))
print(max(session_minutes))

# Will return a sorted iterable
$ 10
$ 180
```

# Type hints

## Annotating Variables

Lets take the basics:

`name = "Eddie"`

`age = 35`

`months = 420.5`

`num_list = [40, 20, 10, 4, 100, 200]`

`host_tuple = ("uuprd1845", "xxdev9031", "ttuat1903")`

`location_dict = {"State": "Veracruz", "Capital_city": "Xalapa"}`

`range_set = {10, 20, 30, 40, 50}`

```python
import typing

name: str = "Eddie"
age: int = 35
months: float = 420.5
num_list: typing.List[int] = [40, 20, 10, 4, 100, 200]
host_tuple:  typing.Tuple[int, int, int] = ("uuprd1845", "xxdev9031", "ttuat1903")
location_dict: typing.Dict[str, int] = {"State": "Veracruz", "Capital_city": "Xalapa"}
range_set: typing.Set[int] = {10, 20, 30, 40, 50}
```





## Simple Type Hints:

**Basic Syntax**: Type hints in Python are used to indicate the expected type of function arguments, return values, and variables. They are not enforce by Python itself but serve as documentation and can be used by tools like static type checkers, IDEs, and linters.

```python
def total_hinted(price_1:int, price_2:int) -> str:
    return f'Your total bill is USD: {price_1+price_2}'
```

In the above code, price_1 and price_2 are **hinted** to be integers, and the function returns a string.

Benefits: **IDE support** provides better autocomplete, suggestions and error caching. **Code Documentation** is clearer as you know the types of data the function expects and returns. **Fewer Bugs**, you may catch mismatches before runtime.

## Intermediate Type Hints

Using Union from the typing module allows you to specify that a variable could be one of several types.


```python
from typing import Union

def mxn_to_usd(value:float) -> Union[float, None]:
    try:
        convertion_factor = 20.1
        value = value/convertion_factor
        return value
    except TypeError:
        return None
```

The above function can return either a float or a None, which is useful for functions that might fail in a predictable way (like division by zero or invalid input)

## Optional Types

In Python 3.9 and below, **Optional[T]** is equivalent to Union[T, None]. It's used when a value can be of type **T or None.**

```python
from typing import Optional

def ex_function(value:Optional[int]) -> int:
    if value is None:
        return 0  # or some other value
    return value
```

**For Python 3.10 and above, use syntactic sugar for union types with the | symbol without the need to import Union or Optional**

```python
def example_function(value: int | None) -> int:
    if value is None:
        return 0
    return value
```

It is advisable to use Union[str, None] as it's similar to what python 3.10 and above uses.
Check documentation [here.](https://fastapi.tiangolo.com/python-types/#using-union-or-optional)


## Generic Collections:

For collections like list, dict, or tuple, you can hint the types of their contents:

```python
from typing import List, Dict, Tuple

numbers: List[int] =[1, 2, 3]
user_data: Dict[str, Union[int, str]] = {"name": "John", "age": 30}
point: Tuple[int, int] = (1, 2)
```

## Advanced Type Hints

### Type Variables(TypeVar)

Useful for defining generic functions where the type is not known until the function is called.

**TypeVar** - Type Variables are used to create type variables which are placeholders for types in generic programming. This allows you to write functions or classes that work with any type, where the type is determined at the time of use. i.e., when the function is called or the class is instantiated.

```python
from typing import TypeVar, List

T = TypeVar('T')

def first_element(lst: List[T]) -> T:
    return lst[0]
```

**TypeVar** is imported from the typing module to define type variables. **List** is also from typing and represents a list type, but it's used here for its generic capability.

```python
T = TypeVar('T')
```

**T** is now a type variable. The 'T' inside the parentheses is just a name for this variable, you can use any name you find appropriate, though single uppercase letters like T, V or K are conventionally used.

```python
def first_element(lst: List[T]) -> T:
```

**lst: List[T]** means that lst is a list where all elements are of the same type T. T here acts as a placeholder for any type that will be specified when the function is used.

**-> T** indicates that the function returns an element of the same type T as the elements in the list.

```python
return lst[0]
```

Function returns the first element of the list, which will be of type **T** regardless of what T actually is.

**How it works?** When you call first_element([1, 2, 3]), the type inference or type checker understands that T in this case is int, so first_element will return an int.

If you call **first_element(['a', 'b'])**, T becomes str, and the function will return a str.

#### Benefits
- Genericity: Function can work with any type of list without rewriting the function for each type.
- Type checking: Static type checkers like mypy can verify that you're using the function correctly based on the types provided at runtime or in the typing annotation.
- Documentation: Clearly communicates to other developers (or you, 6 months in the future) what types the function expects and returns, enhancing readability and maintainability.

#### Complex Scenarios

Type variables can also be constrained or bound:

```python
from typing import TypeVar, List

T = TypeVar('T', int, float)  # T can only be int or float

def sum_list(lst: List[T]) -> T:
    return sum(lst)


sum_list([1,3,4,5,6])  # Returns an int
sum_list([1.1, 3.14159])  # Returns a float
# sum_list(['a','b','c','d','e','f'])  # Will cause a TypeError
```

Here, T is not just any type but is constrained to be either int or float, which makes the sum_list function more specific while still being generic within those constraints.


***
# Decorators

Decorators are a powerful way to modify the behavior of functions without changing their code directly. They are essentially functions that wrap around other functions, adding extra functionality before, after, or around the original function's execution.

**Breakdown**

1. Function as an Object: Everything in Python, including functions, is an object. This means you can pass functions to other functions, return them from functions, or even store them in data structures.
2. Higher-Order Functions: A decorator itself is a function that takes another function as an argument and returns a function. This allows for the modification of the behavior of the original function.
3. Syntax: Decorators use the @ symbol in Python. When you use @decorator above a function definition, it's shorthand for function = decorator(function). 
4. Use Cases: Common uses include logging, timing execution, caching, authorization checks, and the example here, error handling.


## Key benefits of decorators

- Code Reusability: Once you write a decorator, you can apply it to multiple functions, promoting DRY (Don't Repeat Yourself) principles.
- Improved Readability: The decorator syntax @smart_divide clearly indicates that the function is being enhanced in some way, making the intent of the code clearer. In general, Decorators can separate cross-cutting concerns (like logging, error handling, etc.) from the main function logic.
- Flexibility: Decorators allow you to dynamically alter the behavior of functions without modifying their source code.
- Separation of Concerns: You can handle cross-cutting concerns like error handling or logging without cluttering your main functions.

### The decorator

```python
def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)
    return inner
```

- **smart_divide** is defined to take a function 'func' as its argument. 
- Inside **smart_divide**, , there's a function, **inner**   that captures the arguments a and b.
- **inner** if b is 0 prints an error message and returns None to prevent a division by zero error.
- if b is not 0, inner calls **func(a,b)** which is the original function passed to smart_divide.
- Finally, **smart_divide** returns the inner function.

### The decorated function

- **divide** is the function decorated with @smart_divide, this means divide = smart_divide(divide)
- when divide is called, it's actually invoking smart_divide's inner function with divide as 'func'.

```python
@smart_divide
def divide(a, b):
    print(a/b)

divide(9, 0)
```

### Execution

```python
divide(9,0)
```

- When divide(9,0) is called.
    - The inner function from smart_divide is executed.
    - It checks if b (which is 0) is zero, finds it is, prints "Whoops! Division by 0", and returns None instead of performing the division, thus avoiding an error.


