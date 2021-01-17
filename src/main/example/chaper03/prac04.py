import time

n, k = map(int, input().split())

start_time = time.time()
while True:
    if n % k == 0:
        n /= k
    else:
        n -= 1

    print(n)
    if n == 1:
        break

print("실행시간", start_time - time.time())