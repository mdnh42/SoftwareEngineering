

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lst)

lst.append(10)
# print(lst)

lst.extend(lst[len(lst):])
# print(lst)


lst.insert(11, 11)
# print(lst)

lst.remove(1)
# print(lst)

lst.pop()
print(lst)