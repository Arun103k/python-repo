import array as arr

# creating the array with the integer type
a = arr.array("i",[1,2,3,5])
print(type(a),a)

#creating the array with the char type
a = arr.array('u','UNIVERSE')
print(type(a),a)

#creating the array with the floating point
b = arr.array('f',[1.2,23,5,56.2,23,1])
print(type(b),b)
