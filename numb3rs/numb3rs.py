import re
import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    try:
        a,b,c,d = ip.split(".")
        if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255:
            return False
        elif a.startswith("0"):
            return False
        elif re.search(r"^\d+\.\d+\.\d+\.\d+$",ip):
            return True
        else:
            return False
    except ValueError:
        return False



if __name__ == "__main__":
    main()
