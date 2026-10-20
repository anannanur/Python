# # # list = [int(i) for i in input().split()]
# # # a=[]
# # # for i in list:
# # #     if i%4==0 and i%8!=0:
# # #         a.append(i)
# # # print(a)


# # def compute_ratio(x,y):
# #     try:
# #         div = (x+y)/(x*y)
# #     except Exception as e:
# #         return "Error: Division not possible"
# #     else:
# #         return div
# # x,y = map(int,input().split())
# # print(compute_ratio(x,y))

# str = input()
# list = str.split()
# a=[]
# for i in list:
#     if i[0] == 'A' or i[0]=='a' or i[0]=='E'or i[0]=='e' or i[0]=='I'or i[0]=='i'or i[0]=='O' or i[0]=='o' or i[0]=='U' or i[0]=='u':
#         a.append(i)
# print(a)

s = input()
s= s.lower()
a,b=0,len(s)-1
while(a<b):
    if s[a] != s[b]:
        print("Not Palindrome")
        break
    a+=1
    b-=1
else:
    print("Palindrome")