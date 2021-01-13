import time

n, m, k = map(int, input().split())

num = list(map(int, input().split()))

#시작 시간
start_time = time.time()

for i in range(0, len(num)):
    for j in range(i+1, len(num)):
        if num[i] <= num[j]:
            num[i], num[j] = num[j], num[i]

temp1 = num[0]
temp2 = num[1]

count = 0
answer = 0

for i in range(1, m+1):
    if i % k == 0:
        answer += temp2
    else:
        answer += temp1

print(answer)

#마무리 시간
end_time = time.time()
print("WorkingTime: {} sec".format(end_time-start_time))