'''
Raising Exceptions (raise) -- 
   You can manually raise exceptions using the raise keyword. This is useful for signalling error conditions in your 
   own code.
'''
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted"

try :
    print(check_age(20)) # Access granted.
    print(check_age(17)) # Raise ValueError

except ValueError as e:
    print(f"Error : {e}")