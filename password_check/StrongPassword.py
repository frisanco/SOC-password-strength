import re

passwordRegex = re.compile(r'''(
    ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$
)''', re.VERBOSE)

password = input('Enter your password: ')

if passwordRegex.search(password) == None:
    print("NOT ACCEPTABLE.")
else:
    print("Password Set.")