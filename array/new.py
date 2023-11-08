import array as arr

a = arr.array('i',[1,2,3,4,5,5])
print(type(a),a)

b = arr.array('u','BART')
print(type(b),b)

c = arr.array('f',[12.4,24.7,222.1,398.6])
print(type(c),c)

d = arr.array('i',[2,6,7,8,9,34])
print(type(d),d)

#other topics in array
print(c[1])

#assignment
a[2]= 10
print(a)

#add array items
a.append(30)
print(a)

#insert the values to array
a.insert(1,23)
print(a)

#extending the array with the same type
a.extend(d)
print(a)


#---------------------------------------------------------------------------------------------
#deleting the array
a.remove(23)
print(a)

a.remove(34)
print(a)

#alternate method
d.pop(2)
print(d)

d.pop(0)
print(d)

#---------------------------------------------------------------------------------------
#loop arrays
#for loops example
e = arr.array('i',[23,34,56,67])
for x in e:
    print(x)

f = arr.array('d',[12.4,24.5,24.6,65.6])    
for j in f:
    print(j)

#while loops example
l = len(f)
idx = 0
while idx<1:
    print(f[idx])
    idx+=1

p = arr.array('d',[1,2,3])
l = len(p)
idx =0
while idx>1:
    print(p[idx])
    idx+=2

#for loop with array index
v = len(c)
for k in range (v):
    print(c[k])  

z = len(a)
for s in range (z):
    print(a[s])    

#-------------------------------------------------------------------------------------------
#copy of array
d=a
print(id(a),id(d)) 

d[2]=100
print(a,d)

# importing copy from the python library
import copy
d = copy.deepcopy(a)
print(id(a),id(d))

d[0] = 500
print(a,d)
#-------------------------------------------------------------------------------------
#reverse arrays
for w in range(len(d)-1, -1, -1):
    d.append(d[w])