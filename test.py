def add_items(item, lst= []):
    lst.append(item)
    return lst

print(add_items(1))
print(add_items(2))


def mystery(x, y = 2):
    return x * y 

print(mystery(3,mystery(2)))

x = "10"
print(x.lower())