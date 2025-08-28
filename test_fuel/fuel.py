def main():
    while True:
        try:
            fraction = input("Fraction: ")
            p = convert(fraction)
            x = gauge(p)
            print(x)
            break
        except(ZeroDivisionError , ValueError):
            continue


def convert(fraction):
    if "-" in fraction:
        raise ValueError
    else:

        x,y = fraction.split("/")#1/2
        x= int(x)
        y = int(y)
        p = (x/y)*100
        return p

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
