
def divide_numbers():
    while True:
        
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            result = num1 / num2
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please try again. \n") 
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers. \n")
        else:
            return f"The result is: {result}"  # Return the result
        finally:
            print("Thank you for using the calculator. \n")


result = divide_numbers()
print(result)