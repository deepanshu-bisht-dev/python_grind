'''Python allows you to define your own custom exception classes by creating a new class that inherits 
(directly or indirectly) from the built-in Exception class (or one of its subclasses). This makes your error
handling more specific and informative.'''

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older!"):
        self.message = message
        super().__init__(self.message)

def verify_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise your custom exception
    return "Welcome!"

try:
    print(verify_age(15))
except InvalidAgeError as e:
    print(f"Error: {e}")