input_string = "137683-596253"


def secure_container(password_list):

    begin, end = password_list.split("-")
    begin = int(begin)
    end = int(end)
    passwords_counter = 0
    passwords_counter_2 = 0

    for password in range(begin, end + 1):

        number = [int(x) for x in str(password)]

        increase = any([number[i] > number[i + 1] for i in range(0, len(number) - 1)])
        double = any([int(number[k]) == int(number[k + 1])] for k in range(0, len(number) - 1))
        triple = any([(j == 0 or number[j] != number[j - 1]) and number[j] == number[j + 1] and (
                j == len(number) - 2 or number[j] != number[j + 2]) for j in range(0, len(number) - 1)])

        if not increase and double:
            passwords_counter += 1

        if not increase and triple:
            passwords_counter_2 += 1

    return passwords_counter, passwords_counter_2


solutions = secure_container(input_string)

print("Solution Part 1:", solutions[0])
print("Solution Part 2:", solutions[1])

#
# counter = 0
#
# for password in range(137683, 596253 + 1):
#
#     string_password = str(password)
#
#     if len(string_password) == 6:
#         counter_double = 0
#         counter_increase = 0
#         triple_list = []
#         has_triple = False
#
#         for i in range(0, len(string_password) - 1):
#             if int(string_password[i]) <= int(string_password[i + 1]):
#                 counter_increase += 1
#
#         for i in range(0, len(string_password) - 2):
#             if int(string_password[i]) == int(string_password[i + 1]) != int(string_password[i + 2]):
#                 counter_double += 1
#
#         if counter_double > 0 and counter_increase == len(string_password) - 1:
#             counter += 1
#
# print(counter)
