# Loops are used in python to execute decision making statement 
# here we are going to learn about if else loop 

#conditional operators 
# >=, <, >, <=, >=, ==, != 

a =int(input("Enter your age "))

print("Your Age is ",a)

if a>18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
    
budget = 200
    
Expense =190 
    
if Expense>=budget:
        print("Gareeb")
else: 
        print("Thik hai")
    
    
#elif statement only # executes when the if condition is false
# it is used to check multiple conditions

p=int(input("Enter number "))  
     
if p>0:
    print("Positive number")
elif p<0:
    print("Negative number")        
else:
    print("Zero")   
    
# Nested if else statement 
x = int(input("Enter a number: "))

if x<0:
    print("Negative number")
elif x>0: 
    if x<10:
        print("Single digit positive number")
    elif(x<20):
        print("Double digit positive number")
    else:
        print("Number is greater than 20")
else:
    print("Zero")