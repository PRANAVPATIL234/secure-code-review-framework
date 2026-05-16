import os
import hashlib

AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

GITHUB_TOKEN = "ghp_123456789abcdef"

password = "Admin12356@"

user_input = input("Enter ID: ")

query = "SELECT * FROM users WHERE id=" + user_input

os.system("ping " + user_input)

print(query)

hashlib.md5(b"password").hexdigest()