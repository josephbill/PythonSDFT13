def check_number(number):
    message = "jkdjfkdjf"
    if number > 10:
        message = "Greater than 10"
    
    print(message)  # Will raise an error if `if` condition is not met

check_number(5)  # Error: UnboundLocalError: local variable 'message' referenced before assignment
