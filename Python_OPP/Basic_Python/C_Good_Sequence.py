n = int(input())
a = list(map(int, input().split()))

dic = {}

for num in a:
    if num not in dic:
        dic[num] = 0

    dic[num] += 1

ans = 0

for num, count in dic.items():
    if count>num:
        ans += count - num
    elif num>count:
        ans += count 
print(ans)