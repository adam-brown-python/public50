text = input("Input: ")
vowls = ["a","e","i","o","u"]
for i in text:
    if i.lower() in vowls:
        text = text.replace(i,"")
print(text)
