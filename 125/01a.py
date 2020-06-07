def a(a):
    b = len(str(a))
    o = 1
    u = 10
    p = 0
    fyf = 0
    m = []
    for i in range(b):
        p = a % u // o
        a = a - (a % u)
        u *= 10
        o *= 10
        m.append(p)
    for i in range(b):
        if m[0] == m[i]:
            fyf += 1
        else:
            break
    if fyf == b:
        return '+'
    else:
        return '-'

        
print(a(555))
print(a(42))
print(a(4))