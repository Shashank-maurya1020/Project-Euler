n1 = 0
n2 = 1
nth = 0
lis = []

while n2 < 4000000:
    if n2 % 2 == 0:
        lis.append(n2)
    print(n2)
    nth = n1 + n2
    n1 = n2
    n2 = nth

print()
print('sum=', sum(lis))
# ans 4613732
