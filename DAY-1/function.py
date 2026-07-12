# Fnx to calculate avg of 3 number
# PS-1
def avg(a, b, c):
    ans = (a + b+ c)/3
    return ans

print(avg(1,2,3))

# PS-2
def sum(a, b = 0):  # Default value of b is 0
    return a+b
print(sum(2, 4))