with open("input.txt") as f:
    text = f.read()

stock_rauf = "("
stock_runter = ")"
liste = []
stock = 0
stock2 = 0

for index, char in enumerate(text):
    liste.append(char)

for char in liste:
    if char == stock_rauf:
        stock += 1
    if char == stock_runter:
        stock -= 1

# Part 2
print(liste)

for index in range(len(liste)):
    if liste[index] == stock_rauf:
        stock2 += 1
    if liste[index] == stock_runter:
        stock2 -= 1
        if stock2 == -1:
            print(index + 1)

