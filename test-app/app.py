import os

password = "admin123"

user_input = input("Enter ID: ")

query = "SELECT * FROM users WHERE id=" + user_input

os.system("ping " + user_input)

print(query)