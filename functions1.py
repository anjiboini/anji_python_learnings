def person(name,**data):
    print(name)

    for i,j in data.items():
        print(i,j)



person('anji',age=39,city='hyderabad',mob=9866618573)
