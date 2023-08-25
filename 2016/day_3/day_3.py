
with open("input") as input_file:

    inputs = [int(num) for line in input_file for num in line.split() ]


## PART 1 ----------------------------------------------------------------------------------------------------------
possible_counter = 0

for index in range(0, len(inputs), 3):

    if inputs[index] + inputs[index + 1] > inputs[index + 2] and \
       inputs[index + 1] + inputs[index + 2] > inputs[index] and \
       inputs[index] + inputs[index + 2] > inputs[index + 1]:

       possible_counter += 1


print("There are", possible_counter, "possible listed traingles!")


## PART 2 ----------------------------------------------------------------------------------------------------------
possible_counter_2 = 0

for index in range(0, len(inputs), 9):

    current_inputs = inputs[index : index + 9]

    for index_current in range(0, 3):

        if current_inputs[index_current] + current_inputs[index_current + 3] > current_inputs[index_current + 6] and \
           current_inputs[index_current + 3] + current_inputs[index_current + 6] > current_inputs[index_current] and \
           current_inputs[index_current] + current_inputs[index_current + 6] > current_inputs[index_current + 3]:
            
            possible_counter_2 += 1
    
print("There are", possible_counter_2, "possible listed traingles!")
