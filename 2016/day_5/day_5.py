import hashlib

## Your puzzle input is ojvtpuvg. ---------------------------------------------
puzzle_input = "ojvtpuvg"


## PART 1 ----------------------------------------------------------------------------------------------------------
index = 0
password = ""

while len(password ) != 8:

    data = f"{puzzle_input}{index}".encode("utf-8")
    
    hash_code = hashlib.md5(data).hexdigest()

    if hash_code.startswith("00000"):

        password += hash_code[5]

    index += 1

print("Password:", password)


## PART 2 ----------------------------------------------------------------------------------------------------------
index = 0
password = [""] * 8

while "" in password:

    data = f"{puzzle_input}{index}".encode("utf-8")
    
    hash_code = hashlib.md5(data).hexdigest()

    if hash_code.startswith("00000"):

        position_char = int(hash_code[5], 16)
        char = hash_code[6]

        if position_char < len(password) and password[position_char] == "":

            password[position_char] = char     

    index += 1

print("Password:", "".join(password))


