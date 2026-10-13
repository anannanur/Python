n=int(input())
numbers=[]
for i in range(n):
    x=int(input())
    numbers.append(x)

count_pos=0
count_neg=0
count_even=0
count_odd=0

for i in range(n):
    if(numbers[i]>0):
        count_pos+=1
    if(numbers[i]<0):
        count_neg+=1
    if(numbers[i]%2==0):
        count_even+=1
    else:
        count_odd+=1

print("Positive:",count_pos)
print("Negative:",count_neg)
print("Even:",count_even)
print("Odd:",count_odd)