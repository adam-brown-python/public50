while True:
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split("/")
        u = (int(x)/int(y)) * 100
        if u <= 1 and u >= 0:
            print("E")
            break
        elif u >= 99 and u <=100:
            print("F")
            break
        elif u > 100:
            continue
        elif u < 99 and u > 1:
            print(f"{round(u)}%")
            break
    except(ValueError,ZeroDivisionError):
        continue


