x = "Mohammed"

y = 130

try:

    print(x + y)

except TypeError as error:

    x = 188
    print(f"x has changed error = ({error})")
    print(x + y)
else:
    print("printed successfully")













x= "fifa 24"
y = 1

try:

    print(x / y)

except Exception as error:

    x = 11

    print(f"x = 11, error = ({error})")

    print(x / y)

else:


    print("printed successfully")