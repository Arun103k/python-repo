a = [1,2,3,4,5]
print(type(a))

b = [1,2,3,4,5,6] + [5,6,7,8,9,1]
print(b)

c = [2] * 5
print(c)

d = 4 in [1,2,3,5]
print(d)

print("enter the values of index:", a[-4])
print("enter the values of index:", a[2: -1])

e = ["ralph","sandra",22.09,234]
print("enter the value of index:", e[0:3])

f = 1+3j
print(type(f))

g = ["frank","tony stark", 13, 3+5j, 20.90]
print("enter the value of index:", g[1:-1])

a[2] = "arun"
print(a)

g[3] = "shane"
print(g)

h = ["a","b","c","d","e"]
print("original set:", h)
x = ["z","y"]
h[1:3] = x
print("change the value in the list in h:",h )

#add lsit items
j = [12,324,2446,2435]
j.append(13)
j.insert(-3, 99)
j.append("name")
j.insert(4,"rock")
j.insert(-1, 1000)
j.insert(2,"milady")


# remove the items in the list
j.remove(99)
j.remove("milady")
j.pop(2)
j.pop(4)
del j[1]
del j[4]
print(j)

#loop practices with list
lst = [21,24,56,44,-55,98]
for num in lst:
    print(num, end = '')

indices = range(len(lst))
for i in indices:
    print("lst[{}]:".format(i),lst[i])   

# self testing with the loops in list
lst1 = [13,35,67,90,-45,98] 
for num in lst1:
    print(num, end = "")    

indexes = range(len(lst1))
for j in indexes:
    print("lst1:".format(j), lst1[j])    
# list comprehension method
chars = []
for ch in 'VantagePoint':
    if ch not in 'aeiou':
        chars.append(ch)
        print(chars)

car = [car for car in "TutorialPoint" if car not in "aeiou"]
print(car)        

squares = [x*x for x in range(1,12)]
print(squares)

cubes = [y*y*y for y in range(1,10)]
print(cubes)

lst3 = [1,2,3]
lst4 = [7,8,9]
ComLst = [(x,y) for x in lst3 for y in lst4]
print(ComLst)

lst7 = [z for z in range(1,51) if z%2==0]
print(lst7)

lst8 = [v for v in range(1,91) if v%2==0]
print(lst8)

lst9 = ["a","b","c"]
lst0 = ["d","e","f"]
CobList = [(x,y) for x in lst9 for y in lst0]
print(CobList)

# list sort method
lst10 = ["fluid dynamics","solid mechanics","engineering mechanics","hydraulics","aerodynamics"]
lst10.sort()
print("list10 after sorted:", lst10)

lst11 = ["Industrial engineering","Motorsport engineering", "remote sensing and GIS", "4g engineering"]
lst11.sort(key=str.lower)
print(lst11)

def myfunction(s):
    return s%10
lst14 = [28,46,58,97,108,460]
lst14.sort(key=myfunction)
print("afetr sort:", lst14)

# copy lists

print("id(a):", id(a))


