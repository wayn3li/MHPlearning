number = [20, 56, 89, 568, 58, 4, 585, 9, 5, 8]
number1 = []
for item in range(10):
    number1.append(min(number))
    number.remove(min(number))
print(number1)