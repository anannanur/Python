# str="Welcome to machine learning"
# print(len(str))

# print("machine" in str)

str = "Welcome to Machine Learning, Machine"

print("machine" in str)

low_str = str.lower()
print("machine" in low_str)

up_str = str.upper()
print(up_str)

print(str.find("Machine"))
print(str.rfind("Machine"))
print(str.count("Machine"))
print(str.replace("Machine","AI"))
print(str) 
# string is immutable
str.replace("Machine","AI")
print(str)