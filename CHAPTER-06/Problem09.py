'''Set the correct username as "admin" and password as "12345".
Take the username and password as input.
- If both are correct, print Login successful.
- Otherwise, print Invalid username or password.'''


username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid username or password")
