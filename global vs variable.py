a = 10
print(id(a))

def something():
    a =9
    x = globals()['a']
    print(id(x))


    print("inside fun :",a)

something()

print("outside fun: ",a)

