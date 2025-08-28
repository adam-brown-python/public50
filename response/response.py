from validator_collection import validators,checkers,errors
#pip install validator-collection
#pip install validators
x = input("What's your email address? ")
try:
    email_address = validators.email(x)

except errors.EmptyValueError:
    print("invalid")

except errors.InvalidEmailError:
    print("invalid")

else:
    print("valid")
