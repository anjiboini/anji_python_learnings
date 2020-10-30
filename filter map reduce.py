from functools import reduce
#def is_even(n):
    #return n%2==0

nums = [3,2,6,8,4,6,2,9,10,7]

evens = list(filter(lambda n:n%2==0,nums))
#print(evens)


doubles = list(map(lambda n:n*2,evens))
print(doubles)

sum = reduce(lambda a,b:a+b,doubles)
print(sum)

