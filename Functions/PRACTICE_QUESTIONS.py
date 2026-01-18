"""
Python Functions - Progressive Practice Questions
==================================================

This file contains practice questions organized by difficulty level.
Start from Level 1 and work your way up!

Instructions:
1. Read each question carefully
2. Write your solution in the space provided
3. Test your solution by running the code
4. Compare with the solutions (if provided) to learn

Let's begin! 🚀
"""

# ============================================================================
# LEVEL 1: BEGINNER - Basic Function Concepts
# ============================================================================

print("=" * 70)
print("LEVEL 1: BEGINNER - Basic Function Concepts")
print("=" * 70)

# ----------------------------------------------------------------------------
# Question 1: Simple Function
# ----------------------------------------------------------------------------
"""
Write a function called 'say_hello' that prints "Hello, Python!" when called.
No parameters needed, no return value needed.
"""

# YOUR CODE HERE:
def say_hello():
    print("Hello, Python!")

# Test your function:
say_hello()
print()


# ----------------------------------------------------------------------------
# Question 2: Function with One Parameter
# ----------------------------------------------------------------------------
"""
Write a function called 'greet_person' that takes a name as a parameter
and prints "Hello, [name]! Welcome to Python!"
"""

# YOUR CODE HERE:
def greet_person(name):
    print(f"Hello, {name}! Welcome to Python!")

# Test your function:
greet_person("Alice")
greet_person("Bob")
print()


# ----------------------------------------------------------------------------
# Question 3: Function with Return Value
# ----------------------------------------------------------------------------
"""
Write a function called 'add' that takes two numbers as parameters
and RETURNS their sum (don't print, use return!)
"""

# YOUR CODE HERE:
def add(a, b):
    return a + b

# Test your function:
result = add(5, 3)
print(f"5 + 3 = {result}")
print(f"10 + 20 = {add(10, 20)}")
print()


# ----------------------------------------------------------------------------
# Question 4: Multiple Parameters
# ----------------------------------------------------------------------------
"""
Write a function called 'calculate_area' that takes length and width
as parameters and returns the area of a rectangle.
"""

# YOUR CODE HERE:
def calculate_area(length, width):
    return length * width

# Test your function:
area = calculate_area(5, 4)
print(f"Area of rectangle (5x4): {area}")
print()


# ----------------------------------------------------------------------------
# Question 5: Function with Logic
# ----------------------------------------------------------------------------
"""
Write a function called 'is_even' that takes a number and returns True
if the number is even, False if it's odd.
Hint: Use modulo operator (%)
"""

# YOUR CODE HERE:
def is_even(number):
    return number % 2 == 0

# Test your function:
print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")
print()


# ============================================================================
# LEVEL 2: INTERMEDIATE - More Complex Functions
# ============================================================================

print("=" * 70)
print("LEVEL 2: INTERMEDIATE - More Complex Functions")
print("=" * 70)

# ----------------------------------------------------------------------------
# Question 6: Function with Default Parameters
# ----------------------------------------------------------------------------
"""
Write a function called 'create_greeting' that takes a name and an optional
greeting word (default: "Hello"). It should return a string like:
"Hello, Alice!" or "Hi, Alice!" if greeting="Hi"
"""

# YOUR CODE HERE:
def create_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Test your function:
print(create_greeting("Alice"))
print(create_greeting("Bob", "Hi"))
print(create_greeting("Charlie", "Good morning"))
print()


# ----------------------------------------------------------------------------
# Question 7: Function with Multiple Return Values
# ----------------------------------------------------------------------------
"""
Write a function called 'get_stats' that takes a list of numbers and returns
both the minimum and maximum value in the list.
Hint: return min_value, max_value
"""

# YOUR CODE HERE:
def get_stats(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

# Test your function:
nums = [45, 23, 67, 89, 12, 34]
min_val, max_val = get_stats(nums)
print(f"Numbers: {nums}")
print(f"Min: {min_val}, Max: {max_val}")
print()


# ----------------------------------------------------------------------------
# Question 8: Function with Conditional Logic
# ----------------------------------------------------------------------------
"""
Write a function called 'get_grade' that takes a score (0-100) and returns
the letter grade:
- 90-100: 'A'
- 80-89: 'B'
- 70-79: 'C'
- 60-69: 'D'
- Below 60: 'F'
"""

# YOUR CODE HERE:
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test your function:
print(f"Score 95: Grade {get_grade(95)}")
print(f"Score 85: Grade {get_grade(85)}")
print(f"Score 72: Grade {get_grade(72)}")
print(f"Score 55: Grade {get_grade(55)}")
print()


# ----------------------------------------------------------------------------
# Question 9: Function with Loops
# ----------------------------------------------------------------------------
"""
Write a function called 'count_vowels' that takes a string and returns
the number of vowels (a, e, i, o, u) in that string.
Hint: Loop through the string and check each character
"""

# YOUR CODE HERE:
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test your function:
print(f"Vowels in 'Hello': {count_vowels('Hello')}")
print(f"Vowels in 'Python Programming': {count_vowels('Python Programming')}")
print()


# ----------------------------------------------------------------------------
# Question 10: Function that Uses Another Function
# ----------------------------------------------------------------------------
"""
Write a function called 'calculate_total' that takes a list of prices
and a discount percentage (default: 0). It should:
1. Calculate the sum of all prices
2. Apply the discount
3. Return the final total

Use the 'add' function you created earlier if helpful, or just use sum()
"""

# YOUR CODE HERE:
def calculate_total(prices, discount=0):
    total = sum(prices)
    discount_amount = total * (discount / 100)
    return total - discount_amount

# Test your function:
prices = [10, 20, 30, 15]
print(f"Prices: {prices}")
print(f"Total (no discount): ${calculate_total(prices)}")
print(f"Total (10% discount): ${calculate_total(prices, 10)}")
print()


# ============================================================================
# LEVEL 3: ADVANCED - Complex Functions
# ============================================================================

print("=" * 70)
print("LEVEL 3: ADVANCED - Complex Functions")
print("=" * 70)

# ----------------------------------------------------------------------------
# Question 11: Function with *args
# ----------------------------------------------------------------------------
"""
Write a function called 'multiply_all' that takes any number of arguments
and returns the product (multiplication) of all of them.
Use *args to accept variable number of arguments.
"""

# YOUR CODE HERE:
def multiply_all(*args):
    if not args:
        return 0
    result = 1
    for num in args:
        result *= num
    return result

# Test your function:
print(f"multiply_all(2, 3, 4) = {multiply_all(2, 3, 4)}")
print(f"multiply_all(5, 2) = {multiply_all(5, 2)}")
print(f"multiply_all(1, 2, 3, 4, 5) = {multiply_all(1, 2, 3, 4, 5)}")
print()


# ----------------------------------------------------------------------------
# Question 12: Function with **kwargs
# ----------------------------------------------------------------------------
"""
Write a function called 'create_profile' that takes any number of keyword
arguments and returns a formatted string with all the information.
Example: create_profile(name="Alice", age=25, city="NYC")
Should return: "Profile: name=Alice, age=25, city=NYC"
"""

# YOUR CODE HERE:
def create_profile(**kwargs):
    profile_parts = [f"{key}={value}" for key, value in kwargs.items()]
    return "Profile: " + ", ".join(profile_parts)

# Test your function:
print(create_profile(name="Alice", age=25, city="NYC"))
print(create_profile(name="Bob", occupation="Developer", experience=5))
print()


# ----------------------------------------------------------------------------
# Question 13: Lambda Function
# ----------------------------------------------------------------------------
"""
Create a lambda function called 'square' that takes a number and returns
its square. Then use it to square the numbers: 5, 10, 15
"""

# YOUR CODE HERE:
square = lambda x: x ** 2

# Test your function:
print(f"Square of 5: {square(5)}")
print(f"Square of 10: {square(10)}")
print(f"Square of 15: {square(15)}")
print()


# ----------------------------------------------------------------------------
# Question 14: Function with List Processing
# ----------------------------------------------------------------------------
"""
Write a function called 'filter_positive' that takes a list of numbers
and returns a new list containing only the positive numbers.
"""

# YOUR CODE HERE:
def filter_positive(numbers):
    return [num for num in numbers if num > 0]

# Alternative solution:
# def filter_positive(numbers):
#     result = []
#     for num in numbers:
#         if num > 0:
#             result.append(num)
#     return result

# Test your function:
numbers = [-5, 10, -3, 0, 7, -2, 15]
print(f"Original: {numbers}")
print(f"Positive only: {filter_positive(numbers)}")
print()


# ----------------------------------------------------------------------------
# Question 15: Recursive Function (Challenge!)
# ----------------------------------------------------------------------------
"""
Write a function called 'factorial' that calculates the factorial of a number
using recursion. Factorial of n = n * (n-1) * (n-2) * ... * 1
Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
Hint: factorial(0) = 1, factorial(1) = 1
"""

# YOUR CODE HERE:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test your function:
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")
print(f"Factorial of 7: {factorial(7)}")
print()


# ============================================================================
# LEVEL 4: PROJECT-BASED - Real-World Applications
# ============================================================================

print("=" * 70)
print("LEVEL 4: PROJECT-BASED - Real-World Applications")
print("=" * 70)

# ----------------------------------------------------------------------------
# Question 16: Temperature Converter
# ----------------------------------------------------------------------------
"""
Create a function called 'temperature_converter' that:
- Takes a temperature value and a unit ('C' for Celsius or 'F' for Fahrenheit)
- Converts it to the other unit
- Returns the converted temperature

Formulas:
- Celsius to Fahrenheit: F = (C * 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) * 5/9
"""

# YOUR CODE HERE:
def temperature_converter(temp, unit):
    if unit.upper() == 'C':
        # Convert Celsius to Fahrenheit
        return (temp * 9/5) + 32
    elif unit.upper() == 'F':
        # Convert Fahrenheit to Celsius
        return (temp - 32) * 5/9
    else:
        return None

# Test your function:
print(f"32°F to Celsius: {temperature_converter(32, 'F'):.2f}°C")
print(f"0°C to Fahrenheit: {temperature_converter(0, 'C'):.2f}°F")
print(f"100°C to Fahrenheit: {temperature_converter(100, 'C'):.2f}°F")
print()


# ----------------------------------------------------------------------------
# Question 17: Password Validator
# ----------------------------------------------------------------------------
"""
Create a function called 'validate_password' that takes a password string
and returns True if it's valid, False otherwise.

Password requirements:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
"""

# YOUR CODE HERE:
def validate_password(password):
    if len(password) < 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    return has_upper and has_lower and has_digit

# Test your function:
print(f"'Password123' is valid: {validate_password('Password123')}")
print(f"'weak' is valid: {validate_password('weak')}")
print(f"'NoDigitHere' is valid: {validate_password('NoDigitHere')}")
print(f"'nouppercase123' is valid: {validate_password('nouppercase123')}")
print()


# ----------------------------------------------------------------------------
# Question 18: Shopping Cart Calculator
# ----------------------------------------------------------------------------
"""
Create a function called 'calculate_cart_total' that:
- Takes a dictionary of items and their prices: {'item1': 10.50, 'item2': 5.00}
- Takes an optional tax rate (default: 0.08 for 8%)
- Takes an optional discount percentage (default: 0)
- Returns the final total after discount and tax

Calculation order:
1. Sum all item prices
2. Apply discount
3. Add tax to the discounted amount
"""

# YOUR CODE HERE:
def calculate_cart_total(items, tax_rate=0.08, discount=0):
    subtotal = sum(items.values())
    discount_amount = subtotal * (discount / 100)
    discounted_total = subtotal - discount_amount
    tax_amount = discounted_total * tax_rate
    final_total = discounted_total + tax_amount
    return final_total

# Test your function:
cart = {'apple': 2.50, 'banana': 1.50, 'orange': 3.00}
print(f"Cart items: {cart}")
print(f"Total (no discount): ${calculate_cart_total(cart):.2f}")
print(f"Total (10% discount): ${calculate_cart_total(cart, discount=10):.2f}")
print()


# ----------------------------------------------------------------------------
# Question 19: Text Analyzer
# ----------------------------------------------------------------------------
"""
Create a function called 'analyze_text' that takes a string and returns
a dictionary with the following statistics:
- word_count: number of words
- char_count: number of characters (excluding spaces)
- sentence_count: number of sentences (ends with . ! or ?)
- avg_word_length: average length of words
"""

# YOUR CODE HERE:
def analyze_text(text):
    words = text.split()
    word_count = len(words)
    
    char_count = len(text.replace(' ', ''))
    
    sentence_count = sum(1 for char in text if char in '.!?')
    if sentence_count == 0:
        sentence_count = 1  # At least one sentence if no punctuation
    
    if word_count > 0:
        total_word_length = sum(len(word.strip('.,!?;:')) for word in words)
        avg_word_length = total_word_length / word_count
    else:
        avg_word_length = 0
    
    return {
        'word_count': word_count,
        'char_count': char_count,
        'sentence_count': sentence_count,
        'avg_word_length': round(avg_word_length, 2)
    }

# Test your function:
sample_text = "Hello world! This is Python. Functions are great?"
analysis = analyze_text(sample_text)
print(f"Text: '{sample_text}'")
print(f"Analysis: {analysis}")
print()


# ----------------------------------------------------------------------------
# Question 20: Number Guessing Game Helper
# ----------------------------------------------------------------------------
"""
Create a function called 'check_guess' that:
- Takes the secret number, user's guess, and the number of attempts
- Returns a dictionary with:
  - 'correct': True/False
  - 'message': Hint message ("Too high!", "Too low!", or "Correct!")
  - 'attempts_left': remaining attempts
  - 'game_over': True if no attempts left
"""

# YOUR CODE HERE:
def check_guess(secret, guess, attempts_left):
    if guess == secret:
        return {
            'correct': True,
            'message': 'Correct!',
            'attempts_left': attempts_left,
            'game_over': False
        }
    elif guess > secret:
        message = 'Too high!'
    else:
        message = 'Too low!'
    
    attempts_left -= 1
    return {
        'correct': False,
        'message': message,
        'attempts_left': attempts_left,
        'game_over': attempts_left == 0
    }

# Test your function:
secret_num = 42
print(f"Secret number: {secret_num}")
result1 = check_guess(secret_num, 50, 5)
print(f"Guess 50: {result1}")

result2 = check_guess(secret_num, 30, 4)
print(f"Guess 30: {result2}")

result3 = check_guess(secret_num, 42, 3)
print(f"Guess 42: {result3}")
print()


# ============================================================================
# BONUS CHALLENGES - Test Your Mastery!
# ============================================================================

print("=" * 70)
print("BONUS CHALLENGES - Test Your Mastery!")
print("=" * 70)

# ----------------------------------------------------------------------------
# Bonus 1: Function Decorator Pattern
# ----------------------------------------------------------------------------
"""
Create a function called 'timer_decorator' that can wrap other functions
to measure how long they take to execute. (This is advanced - don't worry
if you can't solve it yet, but try to understand the concept!)
"""

# This is advanced - study this after mastering basics
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Example usage:
@timer_decorator
def slow_function():
    import time
    time.sleep(0.1)
    return "Done!"

print("Testing timer decorator:")
slow_function()
print()


# ============================================================================
# SUMMARY AND NEXT STEPS
# ============================================================================

print("=" * 70)
print("🎉 CONGRATULATIONS! You've completed the practice questions!")
print("=" * 70)
print("""
Next Steps:
1. Review any questions you found difficult
2. Try modifying the functions to add new features
3. Create your own practice problems
4. Build a small project using functions
5. Move on to learning Classes and Objects!

Remember: Practice makes perfect! Keep coding! 🚀
""")

