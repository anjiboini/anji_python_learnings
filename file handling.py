
f = open('abc','rb')
f1 = open('efg.xls','wb')
for data in f:
    f1.write(data)
