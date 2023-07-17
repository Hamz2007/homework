while True:
    print("playr1")
    a=int(input( "Choose a number from 1-5:"))
    import random
    b=print(random.randrange(1,6))

    if a==b:
        print("won")

    elif a!=b :
        print("lost")
    print("-"*30)    
    print("playr2")
    c=int(input(" Choose a number from 1-5:"))
    f=print(random.randrange(1,6))

    if c==f:
        print("won")

    elif c!=f:
        print("lost")
        print("-"*30)