import random
while True:
    try:
        n = int(input("level: "))
        if n > 0:
            number = random.randint(1,n)
    except ValueError:
        continue
    else:
        break
while True:
    try:
        user_input = int(input("Guess: "))
    except ValueError:
        continue
    if user_input < number:
        print("Too small!")
        continue
    elif user_input > number:
        print("Too large!")
        continue
    else:
        print("Just right!")
        break


