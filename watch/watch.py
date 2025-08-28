import re
import sys


def main():
    print(parse(input("HTML: ")))
    #lin = input("HTML: ")
    #print(parse(lin))


def parse(s):
    link = re.search(r".+src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\".+",s)
    if link:
        return f"https://youtu.be/{link.group(2)}"
    else:
        return None
if __name__ == "__main__":
    main()
