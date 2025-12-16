#variables
username = "admin"
password = "admin123"
max_attempt = 3
success = False

#Print header
print("=======================================")
print("=========== LOGIN SMULATION ===========")
print("=======================================")
print("#### You have 3 attempts to login ####")
print("")

#User input login codes
for attempt in range(max_attempt):
    operator = input("Please input your username: ")
    pw = input("Please enter the password: ")

    #if login information is correct
    if operator == username and pw == password:
        print("")
        print("login successful")
        success = True  # Set 'success' to True
        break 

    #if login information is false
    else:
        attempts_left = max_attempt - attempt - 1
        if attempts_left == 0:
            print("Your login attempt has failed 3 times!")
        else:
            print("Incorrect username or password")
            print("you have", attempts_left, "attempts left!")
        print("")

#if login failed after max attempts
if not success:
    print("Account locked!")
