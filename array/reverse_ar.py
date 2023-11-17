#reverse arrays
import array as arr1

a = arr1.array('i',[1,4,5,7,8,2])
b = arr1.array('i')
for w in range(len(a)-1, -1, -1):
    b.append(a[w])
    print(a,b)


c = arr1.array('i', [10,5,15,4,6,20,9])
d = c.tolist()
d.reverse()
c = arr1.array('i')
c.fromlist(d)
print (c)    

e = arr1.array('i',[23,45,67,35,21])
f = e.tolist()
f.reverse()
e = arr1.array('i')
e.fromlist(f)
print(e)


