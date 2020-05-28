a = input().split()


b = ['или']
o = 0
for i in range(len(a)):
    if a[i] in b:
        o += 1
print(o)
