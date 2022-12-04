# Write a Python program to square the elements of a list using map() function.

lst = []
length = int(input("Enter lenghth of the list: "))

for i in range(length):
    element = int(input("Enter element: "))
    lst.append(element)
print(lst)

def square(data):
    return data ** 2
result = list(map(square,lst))
print(result)
