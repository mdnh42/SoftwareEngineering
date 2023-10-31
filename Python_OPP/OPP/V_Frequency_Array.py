MAX_SIZE = 10**5 + 10
frequency = [0] * MAX_SIZE

n, k = map(int, input().split())
arr = list(map(int, input().split()))

for num in arr:
    frequency[num] += 1

for i in range(1, k + 1):
    print(frequency[i])