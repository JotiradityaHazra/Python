

# Functions are reusable blocks of code that perform specific tasks.
# They help organize code, reduce repetition, and make programs more modular.

# Key Concepts Covered:
# 1. Basic function definition and calling
# 2. Parameters and arguments
# 3. Return values
# 4. Default parameters
# 5. *args (variable positional arguments)
# 6. **kwargs (variable keyword arguments)
# 7. Lambda functions
# 8. Docstrings
# 9. Scope (local vs global)




# ============================================================================
# 1. BASIC FUNCTION - No parameters, no return value
# ============================================================================

def greet():
    """Simple function that prints a greeting."""
    print("Hello! Welcome to Python Functions!")


# ============================================================================
# 2. FUNCTION WITH PARAMETERS - Takes input
# ============================================================================

def greet_person(name):
    """Function that takes a parameter and uses it."""
    print(f"Hello, {name}! Nice to meet you!")


# ============================================================================
# 3. FUNCTION WITH RETURN VALUE - Gives back a result
# ============================================================================

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    result = a + b
    return result


# ============================================================================
# 4. DEFAULT PARAMETERS - Optional arguments with default values
# ============================================================================

def greet_with_title(name, title="Friend"):
    """Greets a person with an optional title."""
    return f"Hello, {title} {name}!"


# ============================================================================
# 5. *args - VARIABLE POSITIONAL ARGUMENTS
# ============================================================================

def calculate_average(*numbers):
    """
    Calculates average of any number of arguments.
    *args allows passing any number of positional arguments.
    """
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)


# ============================================================================
# 6. **kwargs - VARIABLE KEYWORD ARGUMENTS
# ============================================================================

def display_student_info(**student_data):
    """
    Displays student information using keyword arguments.
    **kwargs allows passing any number of keyword arguments as a dictionary.
    """
    print("\n--- Student Information ---")
    for key, value in student_data.items():
        print(f"{key.capitalize()}: {value}")


# ============================================================================
# 7. COMBINING ALL PARAMETER TYPES
# ============================================================================

def create_profile(name, age, *hobbies, **additional_info):
    """
    Demonstrates using regular params, *args, and **kwargs together.
    Order matters: regular params → *args → **kwargs
    """
    profile = {
        "name": name,
        "age": age,
        "hobbies": list(hobbies),
        "additional_info": additional_info
    }
    return profile


# ============================================================================
# 8. LAMBDA FUNCTIONS - Anonymous one-line functions
# ============================================================================

# Lambda function to square a number
square = lambda x: x ** 2

# Lambda function with multiple parameters
multiply = lambda x, y: x * y


# ============================================================================
# 9. SCOPE - Local vs Global Variables
# ============================================================================

global_counter = 0  # Global variable

def demonstrate_scope():
    """Shows the difference between local and global scope."""
    local_variable = 10  # Local variable (only exists inside this function)
    global global_counter  # Declare we want to modify the global variable
    global_counter += 1
    print(f"Local variable: {local_variable}")
    print(f"Global counter: {global_counter}")


# ============================================================================
# COMPREHENSIVE EXAMPLE - Student Management System
# ============================================================================

def student_management_system():
    """
    A comprehensive example that uses all the concepts explained above.
    This simulates a simple student management system.
    """
    
    print("\n" + "="*60)
    print("STUDENT MANAGEMENT SYSTEM - Demonstrating All Concepts")
    print("="*60)
    
    # Using basic function
    greet()
    
    # Using function with parameters
    greet_person("Alice")
    
    # Using function with return value
    total_score = add_numbers(85, 92)
    print(f"\nTotal score: {total_score}")
    
    # Using default parameters
    print(greet_with_title("Bob"))
    print(greet_with_title("Charlie", "Dr."))
    
    # Using *args - calculating average grades
    print(f"\nAverage grade (3 subjects): {calculate_average(85, 92, 78)}")
    print(f"Average grade (5 subjects): {calculate_average(85, 92, 78, 88, 95)}")
    
    # Using **kwargs - displaying student info
    display_student_info(
        name="David",
        age=20,
        major="Computer Science",
        gpa=3.8,
        year="Junior"
    )
    
    # Using combined parameters
    student_profile = create_profile(
        "Emma",
        22,
        "Reading", "Coding", "Gaming",  # *hobbies
        university="MIT",
        graduation_year=2025,
        email="emma@example.com"
    )
    
    print("\n--- Complete Student Profile ---")
    print(f"Name: {student_profile['name']}")
    print(f"Age: {student_profile['age']}")
    print(f"Hobbies: {', '.join(student_profile['hobbies'])}")
    print("Additional Info:")
    for key, value in student_profile['additional_info'].items():
        print(f"  {key}: {value}")
    
    # Using lambda functions
    print(f"\nSquare of 5: {square(5)}")
    print(f"Multiply 4 and 7: {multiply(4, 7)}")
    
    # Demonstrating scope
    print("\n--- Scope Demonstration ---")
    demonstrate_scope()
    demonstrate_scope()  # Counter increases
    
    # Using lambda with built-in functions
    grades = [85, 92, 78, 88, 95]
    sorted_grades = sorted(grades, reverse=True)
    print(f"\nOriginal grades: {grades}")
    print(f"Sorted grades (descending): {sorted_grades}")
    
    # Filter passing grades (>= 80) using lambda
    passing_grades = list(filter(lambda x: x >= 80, grades))
    print(f"Passing grades (>= 80): {passing_grades}")
    
    # Map grades to letter grades using lambda
    def get_letter_grade(score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'F'
    
    letter_grades = list(map(get_letter_grade, grades))
    print(f"Letter grades: {letter_grades}")
    
    print("\n" + "="*60)
    print("End of demonstration!")
    print("="*60 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Run the comprehensive example
    student_management_system()
    
    # Additional practice examples
    print("\n--- Additional Practice Examples ---\n")
    
    # Example 1: Function returning multiple values
    def get_min_max(numbers):
        """Returns both minimum and maximum values."""
        return min(numbers), max(numbers)
    
    nums = [45, 23, 67, 89, 12, 34]
    minimum, maximum = get_min_max(nums)
    print(f"Numbers: {nums}")
    print(f"Min: {minimum}, Max: {maximum}")
    
    # Example 2: Nested functions
    def outer_function(text):
        """Demonstrates nested functions and closures."""
        def inner_function():
            return text.upper()
        return inner_function()
    
    print(f"\nNested function result: {outer_function('hello world')}")
    
    # Example 3: Function as argument (Higher-order function)
    def apply_operation(x, y, operation):
        """Applies a given operation function to two numbers."""
        return operation(x, y)
    
    result1 = apply_operation(10, 5, lambda a, b: a + b)
    result2 = apply_operation(10, 5, lambda a, b: a * b)
    print(f"\nApplying addition: {result1}")
    print(f"Applying multiplication: {result2}")
