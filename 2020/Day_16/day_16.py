with open("input") as f:
    train_tickets = f.read().splitlines()

valid_numbers = []
range_numbers = []

for element in train_tickets:

    if element == "":
        break

    rest, value = element.split(" ", 1)
    value2 = value.split(" ")

    for index in value2:
        numbers = index.split("-")

        for number in numbers:
            if number.isdigit():
                temp = int(number)
                valid_numbers.append(temp)

for i in range(0, len(valid_numbers) - 1, 2):
    number1 = valid_numbers[i]
    number2 = valid_numbers[i + 1]

    for j in range(number1, number2 + 1):
        range_numbers.append(j)

range_numbers = list(set(range_numbers))

# Getting the tickets to be validated
searching_value = 'nearby tickets:'
index_searching = train_tickets.index(searching_value)
tickets = train_tickets[index_searching + 1:]
error_rate = 0

for element in tickets:
    numbers = element.split(",")

    for number in numbers:
        int_number = int(number)
        if int_number not in range_numbers:
            error_rate += int_number

print("Solution Part 1:", error_rate)

# Part 2
valid_tickets = []
departure_multiplied = 1

# getting my ticket
my_ticket = 'your ticket:'
index_my_ticket = train_tickets.index(my_ticket, 1)

my_ticket = train_tickets[index_my_ticket:index_my_ticket + 2]
print(my_ticket)

# getting the fields
empty_string = ''
index = train_tickets.index(empty_string)
fields = train_tickets[:index]
print(fields)

dictionary_fields = {}
dictionary_taken_fields = {}

for element in fields:
    field, value = element.split(": ")
    temp_list = []
    range_2 = []

    value2 = value.split(" ")

    for index in value2:
        numbers = index.split("-")

        for number in numbers:
            if number.isdigit():
                temp = int(number)
                temp_list.append(temp)

    for i in range(0, len(temp_list) - 1, 2):
        number1 = temp_list[i]
        number2 = temp_list[i + 1]

        for j in range(number1, number2 + 1):
            range_2.append(j)

    range_2 = list(set(range_2))

    dictionary_fields.update({field: range_2})
    dictionary_taken_fields.update({field: False})

print("Fields:", dictionary_fields)
print("Taken Fields:", dictionary_taken_fields)

# getting the tickets
dictionary_tickets = {}
dictionary_taken_tickets = {}
searching_ticket = 'nearby tickets:'
index_searching = train_tickets.index(searching_ticket)
tickets = train_tickets[index_searching + 1:]

for element in tickets:
    numbers = element.split(",")
    clear = True
    for number in numbers:
        int_number = int(number)
        if int_number not in range_numbers:
            clear = False

    if clear:
        valid_tickets.append(element)


for element in valid_tickets:
    numbers = element.split(",")
    counter = 1

    for number in numbers:

        string = str(counter)
        int_number = int(number)

        column_name = "Column " + string

        if column_name not in dictionary_tickets:
            dictionary_tickets[column_name] = int_number
        elif type(dictionary_tickets[column_name]) == list:
            dictionary_tickets[column_name].append(int_number)
        else:
            dictionary_tickets[column_name] = [dictionary_tickets[column_name], int_number]
            dictionary_taken_tickets.update({column_name: False})
        counter += 1

print("Tickets:", dictionary_tickets)

my_ticket_index = []

# compare dictionaries
for key in dictionary_tickets:
    temp_tickets_list = dictionary_tickets[key]

    for key2 in dictionary_fields:
        temp_fields_list = dictionary_fields[key2]

        check = all(element in temp_fields_list for element in temp_tickets_list)
        if check:
            if not dictionary_taken_fields[key2] and not dictionary_taken_tickets[key]:
                dictionary_taken_fields[key2] = True
                dictionary_taken_tickets[key] = True
                print(key, key2)
                if "departure" in key2:
                    string = key.split(" ")
                    integer = int(string[1]) - 1
                    my_ticket_index.append(integer)



# calculating my ticket
print(my_ticket_index)
print(my_ticket)
ticket = my_ticket[1].split(",")

for index in my_ticket_index:
    departure_multiplied *= int(ticket[index])

print("Solution Part 2:", departure_multiplied)






