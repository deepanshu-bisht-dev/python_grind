# Write a program that keeps asking the user to enter a password until they enter the correct one.
password = "abcdef"
enter_pass = (input("Enter password"))
while (enter_pass != password):
    enter_pass = input("Try again, You entered the wrong password")

print("Success,You are logged in.")
  