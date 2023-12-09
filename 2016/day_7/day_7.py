import re

with open("input") as file:

    ips = file.read().splitlines()


def find_abba_pairs(string_array, outside_bracket_bool = True):

    for string in string_array:
        
        for i in range(len(string) - 3):
        
            if string[i] == string[i + 3] and string[i + 1] == string[i + 2] and string[i] != string[i + 1]:
        
                if outside_bracket_bool:
                
                    return True
                
                else:
                    
                    return False
                
    return False  # Return False if no ABBA pattern is found
                

def find_aba_pairs(inside_brackets, outside_brackets, valid_ips_ssl):

    for string in outside_brackets:
        
        for i in range(len(string) - 2):

            if string[i] == string[i + 2] and string[i] != string[i + 1]:

                aba_key = string[i : i + 3]
                bab_key = aba_key[1] + aba_key[0] + aba_key[1]

                if any(bab_key in inside_bracket for inside_bracket in inside_brackets):

                    print("ABA_Key", aba_key)
                    print("BAB_Key", bab_key)
                    print("Inside Brackets", inside_brackets)
                    print("Outside Brackets", outside_brackets)

                    valid_ips_ssl += 1

    return valid_ips_ssl
        

## PART 1 ----------------------------------------------------------------------------------------------------------
valid_ips = 0
valid_ips_ssl = 0

for ip in ips:

    # Extract words within square brackets
    inside_brackets = re.findall(r'\[(.*?)\]', ip)

    # Extract words outside square brackets
    outside_brackets = re.split(r'\[.*?\]', ip)

    # Remove empty strings from the outside_brackets list
    outside_brackets = [word for word in outside_brackets if word]

    outside_bool = find_abba_pairs(outside_brackets)
    inside_bool = find_abba_pairs(inside_brackets)

    if outside_bool and not inside_bool:

        valid_ips += 1

    ## PART 2 ----------------------------------------------------------------------------------------------------------
    valid_ips_ssl = find_aba_pairs(inside_brackets, outside_brackets, valid_ips_ssl)


print("There are", valid_ips, "valid IPs which support TLS")
print("There are", valid_ips_ssl, "valid IPs which support SSL")