***
# Basics of FastAPI
***
...

...

...

...
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
- Improved Readability: The decorator syntax @smart_divide clearly indicates that the function is being enhanced in some way, making the intent of the code cleare. In general, Decorators can separate cross-cutting concerns (like logging, error handling, etc.) from the main function logic.
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

- **smart_divide** is defined to take a function func as its argument. 
- Inside **smart_divide**, , there's a function, **inner**   that captures the arguments a and b.
- **inner** if b is 0 prints an error message and returns None to prevent a division by zero error.
- if b is not 0, inner calls **func(a,b)** which is the original function passed to smart_divide.
- Finally, **smart_divide** returns the inner function.

### The decorated function

- **divide** is the function decorated with @smart_divide, this means divide = smart_divide(divide)
- when divide is called, it's actually invoking smart_divide's inner function with divide as func.

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


