""" This program check if an email is valid or not """

email = input("Please write the email: ")
symbol_email = 0
point = 0

for i in range(len(email)):
    if email[i] == "@":
        symbol_email+=1
    if email[i] == ".":
        point+=1

if symbol_email!= 1 and point ==0:
    print("The email is not correct")
else:
    print("The email is correct")



