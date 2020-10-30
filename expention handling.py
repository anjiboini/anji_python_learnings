a = 5
b = int(input("enter the b value: "))

#print(a/b)


#print("Thanu")
## you got error division by zero

# you can not print

#....................

try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("you can not divide by zero")
finally:
    print("resources closed")



