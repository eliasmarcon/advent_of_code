with open("input") as f:
    power = f.read().splitlines()

# Part 1
power_consumption = 0
gamma_rate = ""
epsilon_rate = ""

one_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zero_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for number in power:
    for i in range(0, len(number)):
        temp = int(number[i])
        if temp == 1:
            one_array[i] = one_array[i] + 1
        else:
            zero_array[i] = zero_array[i] + 1

print("Ones:", one_array)
print("Zeros:", zero_array)

for i in range(0, len(one_array)):
    if one_array[i] > zero_array[i]:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

int_gamma_rate = int(gamma_rate, 2)
int_epsilon_rate = int(epsilon_rate, 2)
power_consumption = int_gamma_rate * int_epsilon_rate
print("Solution Part 1:", power_consumption)


# Part 2

life_support_rating = 0
counter_element_oxy = 0
counter_element_CO2 = 0
oxy_array = power
CO2_array = power

while len(oxy_array) > 1:

    zeros_oxy = []
    ones_oxy = []

    for number in oxy_array:
        if number[counter_element_oxy] == "1":
            ones_oxy.append(number)
        else:
            zeros_oxy.append(number)

    if len(ones_oxy) >= len(zeros_oxy):
        oxy_array = ones_oxy
    else:
        oxy_array = zeros_oxy

    print(oxy_array)
    counter_element_oxy += 1

while len(CO2_array) > 1:

    zeros_CO2 = []
    ones_CO2 = []

    for number in CO2_array:
        if number[counter_element_CO2] == "1":
            ones_CO2.append(number)
        else:
            zeros_CO2.append(number)

    if len(ones_CO2) < len(zeros_CO2):
        CO2_array = ones_CO2
    else:
        CO2_array = zeros_CO2

    print(CO2_array)
    counter_element_CO2 += 1

for number in oxy_array:
    oxy_number = number

for number in CO2_array:
    CO2_number = number

print("Oxy Number:", oxy_number)
print("CO2 Number:", CO2_number)

int_oxy_rate = int(oxy_number, 2)
int_CO2_rate = int(CO2_number, 2)

life_support_rating = int_oxy_rate * int_CO2_rate
print("Solution Part 2:", life_support_rating)


