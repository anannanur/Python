prompt = "What is Python ?"
tokens = prompt.split()
print(tokens)

sentence = ("_").join(tokens)
print(sentence)

name = 'Adil'
print(type(name))
age = 24
height = 5.1123445
print(f"His name is {name.upper()}. He is {age} years old. He is {height:.2} feet tall")

model_accuracy = 0.83333
print(f"The model accuracy is {model_accuracy: .3%}")