def main():
    #ctrl + shift + v = paste
    time = input("what time is it? ")
    x = convert(time)
    if 7<= x <= 8:
        print("breakfast time")
    elif 12 <= x <=13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")

def convert(time):
    hour,min = time.split(":")
    hour = float(hour)
    min = float(min)/60
    return hour+min

if __name__ == "__main__":
    main()

