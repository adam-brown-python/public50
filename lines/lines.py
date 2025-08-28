import sys
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("not a python file")
else:
    try:
        with open(sys.argv[1],"r") as file:
            counter = 0
            for line in file:
                if line.strip() == "":
                    continue
                if line.strip().startswith("#"):
                    continue
                else:
                    counter += 1
            print(counter)
    except FileNotFoundError:
        sys.exit("File does not exist")

