# Python Functions - Quick Reference Guide

## 📋 Essential Function Syntax

### 1. Basic Function
```python
def function_name():
    # code here
    pass
```

### 2. Function with Parameters
```python
def function_name(param1, param2):
    # use param1 and param2
    return result
```

### 3. Function with Default Parameters
```python
def function_name(param1, param2="default"):
    # param2 is optional
    return result
```

### 4. Function with *args (Variable Arguments)
```python
def function_name(*args):
    # args is a tuple of all arguments
    for arg in args:
        print(arg)
```

### 5. Function with **kwargs (Keyword Arguments)
```python
def function_name(**kwargs):
    # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### 6. Lambda Function
```python
square = lambda x: x ** 2
# Equivalent to:
def square(x):
    return x ** 2
```

---

## 🔑 Key Concepts Cheat Sheet

| Concept | Description | Example |
|---------|-------------|---------|
| **def** | Keyword to define a function | `def my_func():` |
| **return** | Sends value back to caller | `return 42` |
| **parameter** | Variable in function definition | `def func(x):` |
| **argument** | Value passed when calling | `func(5)` |
| ***args** | Variable positional arguments | `def func(*args):` |
| **\*\*kwargs** | Variable keyword arguments | `def func(**kwargs):` |
| **lambda** | Anonymous one-line function | `lambda x: x*2` |
| **scope** | Where variables are accessible | Local vs Global |

---

## 💡 Common Patterns

### Pattern 1: Input → Process → Output
```python
def process_data(input_data):
    # Process the input
    result = input_data * 2
    # Return the output
    return result
```

### Pattern 2: Validation Function
```python
def is_valid(value):
    if value > 0:
        return True
    return False
```

### Pattern 3: Multiple Return Values
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9])
```

### Pattern 4: Function with Defaults
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")  # Uses default "Hello"
greet("Bob", "Hi")  # Uses "Hi"
```

---

## ⚠️ Common Mistakes

1. **Missing Colon**
   ```python
   # Wrong:
   def my_func()
   # Right:
   def my_func():
   ```

2. **Wrong Indentation**
   ```python
   # Wrong:
   def my_func():
   print("Hello")  # Not indented!
   
   # Right:
   def my_func():
       print("Hello")  # Properly indented
   ```

3. **Forgetting Return**
   ```python
   # Wrong:
   def add(a, b):
       a + b  # No return!
   
   # Right:
   def add(a, b):
       return a + b
   ```

4. **Mixing Parameters and Arguments**
   ```python
   # Parameters are in definition:
   def greet(name):  # 'name' is a parameter
       pass
   
   # Arguments are when calling:
   greet("Alice")  # "Alice" is an argument
   ```

---

## 🎯 Function Best Practices

1. **Use Descriptive Names**
   - ✅ Good: `calculate_total_price()`
   - ❌ Bad: `calc()` or `func1()`

2. **Keep Functions Focused**
   - One function should do one thing well
   - If it does multiple things, split it up

3. **Use Docstrings**
   ```python
   def add(a, b):
       """Adds two numbers together.
       
       Args:
           a: First number
           b: Second number
       
       Returns:
           Sum of a and b
       """
       return a + b
   ```

4. **Return Early for Edge Cases**
   ```python
   def divide(a, b):
       if b == 0:
           return None  # Handle error case first
       return a / b
   ```

5. **Use Type Hints (Advanced)**
   ```python
   def add(a: int, b: int) -> int:
       return a + b
   ```

---

## 📚 Study Order

1. ✅ Basic functions (no parameters)
2. ✅ Functions with parameters
3. ✅ Return values
4. ✅ Default parameters
5. ✅ Multiple return values
6. ✅ *args and **kwargs
7. ✅ Lambda functions
8. ✅ Scope and global variables
9. ✅ Advanced concepts (decorators, closures, etc.)

---

## 🚀 Quick Practice Ideas

1. **Calculator Functions**
   - `add()`, `subtract()`, `multiply()`, `divide()`

2. **String Functions**
   - `reverse_string()`, `count_words()`, `capitalize_words()`

3. **List Functions**
   - `find_max()`, `find_min()`, `filter_even()`, `sort_list()`

4. **Validation Functions**
   - `is_email_valid()`, `is_password_strong()`, `is_number_positive()`

5. **Utility Functions**
   - `format_currency()`, `calculate_percentage()`, `convert_temperature()`

---

## 📖 Resources

- **Your Files:**
  - `LEARNING_GUIDE.md` - Detailed step-by-step guide
  - `PRACTICE_QUESTIONS.py` - 20+ practice problems
  - `Functions.py` - Advanced examples
  - `Functions_Example.py` - Basic examples

- **Practice Strategy:**
  1. Read the learning guide
  2. Complete practice questions level by level
  3. Review advanced examples
  4. Build your own projects!

---

**Remember**: Functions are the building blocks of Python programming. Master them, and you'll write better, more organized code! 🎉

