# Sum of first n natural number
n = int(input('Enter any number: '))
sum = 0
while(n>0):
    sum += n
    n = n - 1
print(sum)    