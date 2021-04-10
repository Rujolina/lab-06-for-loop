userinput = input("Let's party! How long until the party? (Give me a number) ")
usernum = (int(userinput), 10)
i = 0
if i in usernum < 1:
    print("PARTY NOW!!")
else:
    for i in usernum:
        if i > 1:
            i = i - 1
            print(i)
    print("PARTY TIME")
