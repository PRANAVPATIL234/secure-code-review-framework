import os
import hashlib

GITHUB_TOKEN = "ghp_123456789abcdef"


hashlib.md5(b"password").hexdigest()

password = "admin123"

user_input = input("Enter ID: ")

query = "SELECT * FROM users WHERE id=" + user_input

os.system("ping " + user_input)

print(query)