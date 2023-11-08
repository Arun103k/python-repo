import array as arr2

a = arr2.array('i',[99,24,26,67,89,76])
b=a.tolist()
b.sort()
a = arr2.array('i')
a.fromlist(b)
print(a)

c = arr2.array('i',[24,89,45,67,10,20,998])
d = c.tolist()
d.sort()
c = arr2.array('i')
c.fromlist(d)
print(c)

sorted(c)
print(c)