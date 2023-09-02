number=0
while number <3:
    import random
    s=["hamza","abdullah","Ali"]
    e=random.choice(s)
    print(e)
    x=print(random.randrange(40,100))
    c=int(input("student score:"))
    if 90<c:
        print("excellent")

    elif 80<c:
        print("very good")

    elif 70<c:
        print("good")

    elif 50<c:
        print("passed")

    else:
        print("failed")

