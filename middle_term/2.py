lst = ['H', 'e', 'l', 'l', 'o', ' ', 'I', 'a', 'T']

del(lst[7])
lst.insert(7, 'o')
print(lst)
lst.append("?")
print(lst)
print(len(lst))
print("".join(lst))
lst.sort(reverse=True)
print(lst)