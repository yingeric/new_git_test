L = []
count=7
for c in range(count):
    L.append(2**c)
print L
i=0

if 32 in L:
    i=L.index(32)
    print L.index(32),L[i]
else:

    print ('not found')

print map(lambda x: 2 ** x, range(7))
