import csv
import sys
table = []
try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            for i in reader:
                l,f = i["name"].split(", ")
                table.append({"first":f,"last":l,"house":i["house"]})
        with open(sys.argv[2],"w") as file:
            writer = csv.DictWriter(file,fieldnames= ["first","last","house"])
            writer.writeheader()
            for i in table:
                writer.writerow(i)
except(FileNotFoundError):
    sys.exit(f"could not read {sys.argv[1]}")
    




