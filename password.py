""" This program evaluate a password """

print("please enter a password that has 8 or more characters and no spaces")

password = input("Insert a password: ")


if len(password)<8:
    print("The password is incorrect, please try again")

else:
    for i in password :

        if i == " ":
            print("The password is incorrect, please try again")
            password = input("Insert a password: ")
    print("the password is OK")
