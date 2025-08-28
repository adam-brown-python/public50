import csv
import os
def main():
    print("1.add")
    print("2.delete")
    print("3.show")
    command = input()
    if command == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        gp = input("Enter group: ")
        add(name,age,gp)
    elif command == "2":
        student_delete = input("Enter student info (separate by space): ")
        name,age,gp = student_delete.split(" ")
        delete(name,age,gp)

    elif command == "3":
        gp = input("which group do you want to check: ")
        show(gp)

def add(name,age,gp):
    if not os.path.exists("students.csv"):
        with open("students.csv","a",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["name","age","group"])
            writer.writeheader()
            writer.writerow({"name":name,"age":age,"group":gp})
            return "student_add"
    else:
        with open("students.csv","a",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["name","age","group"])
            writer.writerow({"name":name,"age":age,"group":gp})
            return "student_add"

def delete(name,age,gp):
    table = []
    with open("students.csv","r") as file:
        reader = csv.DictReader(file)
        for i in reader:
            table.append(i)
    for i in table:
        if i["name"] == name and i["age"] == age and i["group"] == gp:
            table.remove(i)
    with open("students.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["name","age","group"])
        writer.writeheader()
        for i in table:
            writer.writerow(i)
        return "student_delete"


def show(gp):
    with open("students.csv","r") as file:
        reader = csv.DictReader(file)
        for i in reader:
            if i["group"] == gp:
                print(f"name: {i["name"]}")
                print(f"age: {i["age"]}")
                print(f"group: {i["group"]}")
                print("***************************")
        return "student_show"

if __name__ == "__main__":
    main()
