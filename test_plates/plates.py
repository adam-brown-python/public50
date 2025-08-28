def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not (s[0].isalpha() or s[1].isalpha()):
        return False

    for i in s:
        if i == "0" and s[s.index(i)-1].isalpha():
            return False
        elif i.isdigit() and not s[s.index(i):].isdigit():
            return False
        elif not i.isalnum():
            return False
    else:
        return True
if __name__ == "__main__":
    main()

