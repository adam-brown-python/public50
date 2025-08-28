import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\b(um|Um)\b",s)
    return len(match)

if __name__ == "__main__":
    main()
