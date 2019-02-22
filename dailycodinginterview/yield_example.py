def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
print(next(mygenerator))
print('hi')
print(next(mygenerator))
print('hi')
print(next(mygenerator))
print('hi')
print(next(mygenerator))