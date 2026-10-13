
n = int(input())
numbers = []

for i in range(n):
    x = int(input())
    numbers.append(x)

min = numbers[0]
max = numbers[0]

for i in range(n):
    if min > numbers[i]:
        min = numbers[i]

    if max < numbers[i]:
        max = numbers[i]

print(min, max)
