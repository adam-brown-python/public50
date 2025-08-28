def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowls = ["a","e","i","o","u"]
    for i in word:
        if i.lower() in vowls:
            word = word.replace(i,"")
    return word


if __name__ == "__main__":
    main()
