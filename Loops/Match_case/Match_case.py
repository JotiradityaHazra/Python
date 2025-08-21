# MAtch case is used to match the value of a variable against a series of patterns.

x= int(input("Enter a number: "))

match x: 
    case 0:
        print("You entered zero.")
    case 1:
        print("You entered one.")   
    case 2:
        print("You entered two.")    
    case _ if x > 50:
        print(x)
        
        # U can you if else elif statements to achieve the same result.
        