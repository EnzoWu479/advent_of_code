list1 = []
list2 = []

with open('input.txt') as f:
    for line in f:
        number1, number2 = map(int, line.split("   "))
        list1.append(number1)
        list2.append(number2)

list1.sort()
list2.sort()

similarities = []

for i in range(len(list1)):
    number1 = list1[i]
    similarity = list2.count(number1)
    similarities.append(similarity * number1)

sum_similarity = sum(similarities)
print(sum_similarity)