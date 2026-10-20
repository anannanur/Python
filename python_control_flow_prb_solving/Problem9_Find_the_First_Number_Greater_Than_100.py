# n=int(input())
# ns=[]
# for i in range(n):
#     m=int(input())
#     ns.append(m)

# for i in range(n):
#     if ns[i]>100:
#             print(ns[i])
#             break

n= int(input())
a = list(map(int,input().split()))
for x in a:
    if x>100:
        print(x)
        break