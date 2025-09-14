import random
while True:
    try:
        n = int(input("level: "))
        if n > 0:
            number = random.randint(1,n)
            break
    except ValueError:
        continue

while True:
    try:
        user_input = int(input("Guess: "))
    except ValueError:
        continue
    if user_input <= 0:
        continue
    elif user_input < number:
        print("Too small!")
        continue
    elif user_input > number:
        print("Too large!")
        continue
    else:
        print("Just right!")
        break


