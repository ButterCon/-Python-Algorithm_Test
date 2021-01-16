n, m = map(int, input().split())

count = 0

for i in range(n):
    data = list(map(int, input().split()))
    if i == 0:
        count = min(data)
    elif min(data) > count:
        count = min(data)

print(count)
