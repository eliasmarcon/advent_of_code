with open("input") as f:
    raw_passports = f.read().split("\n\n")

passports = []

for line in raw_passports:
    line = line.replace("\n", " ")
    passports.append(line)

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = []

for passport in passports:
    counter_valid = 0
    for valid in valid_fields:
        if valid in passport:
            counter_valid += 1
            if counter_valid == len(valid_fields):
                valid_passports.append(passport)

print("Solution Part 1:", len(valid_passports))
#print("Solution Part 1 list valid Passports:", valid_passports)


# Part 2
valid_present_passports = []
bad_passports = []
eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


for valid_passport in valid_passports:
    counter_valid_present = 0
    passport = valid_passport.split(" ")

    for element in passport:
        valid_field, value = element.split(":")
        if valid_field == 'byr' and 1920 <= int(value) <= 2002:
            counter_valid_present += 1
        elif valid_field == "iyr" and 2010 <= int(value) <= 2020:
            counter_valid_present += 1
        elif valid_field == "eyr" and 2020 <= int(value) <= 2030:
            counter_valid_present += 1
        elif valid_field == "hgt":
            if "cm" in value:
                cm, rest = value.split("cm")
                if 150 <= int(cm) <= 193:
                    counter_valid_present += 1
            elif "in" in value:
                inches, rest = value.split("in")
                if 59 <= int(inches) <= 76:
                    counter_valid_present += 1
        elif valid_field == "hcl":
            if "#" in value and len(value) == 7:
                counter_valid_present += 1
        elif valid_field == "ecl":
            if value in eye_color:
                counter_valid_present += 1
        elif valid_field == "pid":
            if len(value) == 9 and value.isdigit():
                counter_valid_present += 1
    if counter_valid_present == 7:
        valid_present_passports.append(valid_passport)
    else:
        bad_passports.append(valid_passport)

print("Solution Part 2:", len(valid_present_passports))


