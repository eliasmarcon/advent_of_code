import re
from collections import Counter

def is_real_room(name, checksum):

    name = name.replace("-", "")
    letter_counts = Counter(name)
    sorted_letters = sorted(letter_counts.keys(), key=lambda letter: (-letter_counts[letter], letter))
    calculated_checksum = "".join(sorted_letters[:5])

    return calculated_checksum == checksum



## PART 1 ----------------------------------------------------------------------------------------------------------
with open("input", "r") as file:
        
    input_data = file.read()

lines = input_data.strip().split("\n")
total_sector_ids = 0

for line in lines:

    match = re.match(r"([a-z-]+)-(\d+)\[([a-z]+)\]", line)

    name, sector_id, checksum = match.groups()

    if is_real_room(name, checksum):

        total_sector_ids += int(sector_id)

print("Sum of sector IDs of real rooms:", total_sector_ids)



## PART 2 ----------------------------------------------------------------------------------------------------------

def decrypt_name(name, sector_id):

    decrypted = ""
    for char in name:

        if char == "-":

            decrypted += " "
        
        else:
            
            shift = int(sector_id) % 26
            decrypted += chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
    
    return decrypted

with open("input", "r") as file:

    input_data = file.read()

lines = input_data.strip().split("\n")

for line in lines:
    
    match = re.match(r"([a-z-]+)-(\d+)\[([a-z]+)\]", line)
    name, sector_id, checksum = match.groups()
    
    if is_real_room(name, checksum):
    
        decrypted_name = decrypt_name(name, sector_id)
    
        if "northpole" in decrypted_name:
    
            print("Sector ID of the room with North Pole objects:", sector_id)
    
            break





























