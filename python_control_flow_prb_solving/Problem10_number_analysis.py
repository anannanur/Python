n=int(input())
numbers = list(map(int,input().split()))
c=0
for i in numbers:
    if i%2==0:
        continue
    elif i%2!=0:
        cn=i
        sum=0
        while(cn!=0):
            m = cn%10
            cn = cn//10 
            sum+=m
        if(sum>20):
            break
        else:
            c+=1
            print(i,sum)
print(c)