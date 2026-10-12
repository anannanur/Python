n=int(input())

sum = 0
for i in range(n):
    if i%2==0:
        continue
    sum+=i
print(sum)