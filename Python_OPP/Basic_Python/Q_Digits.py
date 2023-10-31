s = input()
n = len(s)

str_list = []
ans = ""
l = 0
r = 0

for i in range(n):
    if s[i]=='L':
        l += 1
        ans += s[i]
    if s[i]=='R':
        r += 1
        ans += s[i]
    if l==r:
        str_list.append(ans)
        ans = ""
        l = 0
        r = 0

sz = len(str_list)
print(sz)
for item in str_list:
    print(item)