# empty_set = set()
# print(type(empty_set))

set = {1,3,4,4,4,7,("Tanu", 6, "Deepak")}
print(set)
print(type(set))

#-------------Methods----------------#
set.add(76)
print(set)
set.pop()
print(set)

#-------Union and Intersection-----------#
set1 = {4,6,9,0,33}
set2 = {4,9,77,1,8}
print(set1.union(set2))
print(set1.intersection(set2))