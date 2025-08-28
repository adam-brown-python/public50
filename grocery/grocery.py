grocery = {}
while True:
    try:
        item = input().upper()
        if not item in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
    except EOFError:
        break
for i in sorted(grocery):
    print(grocery[i], i)

