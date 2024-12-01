list1 = []
list2 = []

with open('input.txt') as f:
    for line in f:
        number1, number2 = map(int, line.split("   "))
        list1.append(number1)
        list2.append(number2)

list1.sort()
list2.sort()

distances = []

for i in range(len(list1)):
    number1 = list1[i]
    number2 = list2[i]

    distances.append(abs(number1 - number2))

sum_distances = sum(distances)

print(sum_distances)