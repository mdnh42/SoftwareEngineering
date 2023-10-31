
t = int(input(t))

for _ in range(t):
    n = int(input(n))
    for i in range(0, n):
        input(s, e)

    ok = True

    for i in range(1, n):
        if s[i]>s[0] and e[i] >= e[0]:
            ok = False

    if(ok == False):
       print("-1")
    continue
        
    print(s[0])


