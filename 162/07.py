# as666
# 0 0 -> []

a = input()
n = int(input())
m = int(input())

#print(a, n, m)

s = 0

#print(a[n:m])
#print([x for x in a[n:m]])

z = [x for x in a[n:m]]

for i in range(len(z)):
    if z[i] == '6':
        s += 1
        if s == 3:
            print('yes')
            break
    else:
        print('no')

# fsj sdlk666jfk lskkjf  => fsj sdlk666jfk => f s j s d l k 6 6 6 j f k
