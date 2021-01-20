#정사각형 크기
N = int(input())

X, Y = 1, 1

MOVE = input().split()

for i in MOVE:
    if i == "U":
        X -= 1
    elif i == "D":
        X += 1
    elif i == "R":
        Y += 1
    elif i == "L":
        Y -= 1

    if X == 0:
        X = 1
    elif X == N + 1:
        X = 5

    if Y == 0:
        Y = 1
    elif Y == N + 1:
        Y = 5

print(f"{X}, {Y}")