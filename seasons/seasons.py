from datetime import date
import inflect
import sys
p = inflect.engine()
#pip install inflect
def main():
    try:
        birthday = input("Date of birth: ")
        y,m,d = birthday.split("-")
        bday = date(int(y),int(m),int(d))
        tday = date.today()
        age = tday - bday
        min = age.days*1440
        age = convert(min)
        print(age,"minutes")

    except:
        sys.exit("invalid date")


def convert(min):
    word  = p.number_to_words(min,andword="").capitalize()
    return word

if __name__ == "__main__":
    main()
