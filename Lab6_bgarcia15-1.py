'''
Lab 6 - Dictionaries
Author: Ben Garcia

Program that simulates a login system using a dictionary
Dictionary has 4 key value pairs, 3 known users and a guest
Each user has a username, real name, password and security level

'''
# Create a dictionary of users to store user information
users = {

# Create a key value pair for each user, with username key and password value
    'Bgarcia15': 'pass1',
    'Jdoe': 'pass2',
    'Guest': 'guest',
    'Titus': 'shakespeare#1'
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
        if password == users[username]:
            print("Login successful. Welcome " + username + "!")
            
        #Add security level for each user, if guest print guest access, else print level 1 access
            if username == 'Guest':
                print("You have guest access.")
            else:
                print("You have level 1 access.")

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

