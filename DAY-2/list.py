list = [23,34,45,26,77]
print(list)
print(type(list))

# List are mutable
list[0] = 00
print(list)

#-------------Methods---------------------#
l = [23,1,55,8,98]
l.sort(reverse=True)
print(l)

l.insert(2, 999)
print(l)

l.reverse()
print(l)


#-------------Loop In list-------------#
marks = [34,78,3,88,65]
idx = 0
found = False

# Check index of 88
for val in marks:
    if val == 88:
        found = True
        break
    idx+=1 
if found:
    print(f"Index of 88 is {idx}")