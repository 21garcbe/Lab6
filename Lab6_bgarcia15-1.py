'''
Lab 6 - Dictionaries
Author: Ben Garcia

Program that simulates a login system using a dictionary
Dictionary has 3 known users and a guest
Each user has a username, real name, password and security level

'''
# Create a dictionary of users to store user information
users = {

# Create a dictionary for each user with key = username, value = another dictionary with keys name, password, and security_level
    'Bgarcia15': {'name': 'Ben', 'password': 'pass1', 'security_level': 'Level 1'},
    'Jdoe': {'name': 'John', 'password': 'pass2', 'security_level': 'Level 1'},
    'Guest': {'name': 'Guest', 'password': 'guest', 'security_level': 'guest'},
    'TitusAndronicus': {'name': 'Titus', 'password': 'shakespeare#1', 'security_level': 'Level 1'}
}

print("Welcome to the login system. Please enter your username and password.")

# Prompt the user to enter their username and check if valid
username = input("Username: ").title()

#set password attempt iterator to 0
password_attempts = 0
if username in users:
     #if username is valid, prompt for password, start password attempt loop, and check if password is correct
    while password_attempts < 3:
        password = input("Password: ")
        # if password correct print welcome and security level
        if password == users[username]['password']:
            print("Login successful. Welcome " + users[username]['name'] + "!" + " You have " + str(users[username]['security_level']) + " security access.")
            break
        else:
            #if password is incorrect increment password_attempts, print try again and remainaing attempts
            password_attempts += 1
            print("Incorrect password. Please try again.")
            print("\nAttempts remaining: " + str(3 - password_attempts))
    #if 3 incorrect attempts, exit        
    if password_attempts >= 3:
        print("Too many failed attempts. Exiting program.")
else:
    print("Username not found. Exitting program.")

