import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"([0-9][0-9]?):?([0-9][0-9])? (AM|PM) to ([0-9][0-9]?):?([0-9][0-9])? (AM|PM)",s)
        time1 = standard(match.group(1),match.group(2),match.group(3))
        time2 = standard(match.group(4),match.group(5),match.group(6))
        return f"{time1} to {time2}"
    except:
        raise ValueError

def standard(hr,min,x):
    if min == "60":
        raise ValueError
    if hr == "12":
        if x == "AM":
            hr = "00"
        else:
            hr = "12"
    else:
        if x == "AM":
            hr = f"{int(hr):02}"
        else:
            hr = f"{int(hr) + 12}"
    if min == None:
        min  = "00"

    else:
        min = f"{int(min):02}"

    return f"{hr}:{min}"

if __name__ == "__main__":
    main()
