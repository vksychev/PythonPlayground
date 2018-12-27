#lambda
x = lambda a, b: a + b
a = x(1, 2)
#print(a)

#reverse string
x = 'asdf'
#print(x[::-1])

#set
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_set= {i for i in list_a}
#print(my_set)

#flist
flist = []
for i in range(3):
    flist.append(lambda: i)
#print([f() for f in flist])

flist = []
for i in range(3):
    flist.append(lambda i=i:i)
#print([f() for f in flist])


#dir
#print(dir(list))