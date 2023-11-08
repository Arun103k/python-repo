import array as arr

a = arr.array('i',[1,3,4,5,7])
b = arr.array('i',[6,8,9,2,0])
for j in range (len(b)):
    a.append(b[j])
    print(a,b)


a.extend(b)
print(a)  

sorted(b)
print(b)

c = arr.array('i', [12,34,24,21,46])
d = arr.array('i',[38,24,34,21,56])
x = c.tolist()
y = d.tolist()
z = x+y
c = arr.array('i')
c.fromlist(z)
print(c)