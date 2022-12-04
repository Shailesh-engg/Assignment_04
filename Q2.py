# Write a Python program to triple all numbers of a given list of integers. Use Python map.

lst = []
length = int(input("Enter length of the list: "))
for i in range(length):
    Element = int(input("Enter element: "))
    lst.append(Element)
print(lst)

def tri(data):
    return data * 3
result = list(map(tri,lst))
print(result)
