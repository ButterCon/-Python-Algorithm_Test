import time

N = int(input())

count = 0

first = time.time()

for i in range(N+1):
    for j in range(0, 60):
        for k in range(0, 60):
           #if str(i).count("3") > 0 or str(j).count("3") > 0 or str(k).count("3") > 0:
           if '3' in str(i) + str(j) + str(k):
                print(f"{i}시 {j}분 {k}초")
                count += 1

print(count)

print(f"실행 시간 : {time.time() - first}")