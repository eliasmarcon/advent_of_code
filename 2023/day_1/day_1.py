import re

with open("input") as f:
    
    data  = f.read().strip().split("\n")

#### Part 1
    
new_numbers = [int(re.search(r'\d{1}', text).group(0) + re.search(r'\d{1}', text[::-1]).group(0)) for text in data]
print("What is the sum of all of the calibration values? ~ Answer:", sum(new_numbers))


#### Part 2
p2_score = 0

for line in data:
    prob_2_digits = []
    
    for index, value in enumerate(line):
        
        if value.isdigit():
            prob_2_digits.append(value)
        
        for index2, value2 in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[index:].startswith(value2):
                prob_2_digits.append(str(index2 + 1))
                
    p2_score += int(prob_2_digits[0] + prob_2_digits[-1])
    
    
print("What is the sum of all of the calibration values? ~ Answer:", p2_score)