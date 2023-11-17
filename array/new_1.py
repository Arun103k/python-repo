import array as arr1

a = arr1.array('i',[1,2,3,4,5,6,78,8])
print(type(a),a)

a1 = a[1]
print(a1)

a2 = a[6]
print(a2)

a.pop()
print(a)

