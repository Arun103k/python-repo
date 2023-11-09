#reverse method
import array as arr1

a = arr1.array('i',[1,2,4,5,3])
a.reverse()
print(a)

c = a.count(3)
print(c)

d = a.index(4)
print(d)

lst = [2,3,4,5,6,7,8]
e = a.fromlist(lst)
print(a)

f = open('list.txt','wb')
arr1.array('i',[1,2,3,4,5]).tofile(f)
f.close()

s = open('list.txt','rb')
a.fromfile(s,4)
print(a)
