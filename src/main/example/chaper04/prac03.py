import time

match = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

order = input()
order = [match[order[0]], int(order[1])]

move = [[-2, 1], [-2, -1], [2, 1], [2, -1],
        [-1, 2], [1, 2], [1, -2], [-1, -2]]

count = 8

for i in range(len(match)):
        for j in range(len(move[i])):
                if order[j] + move[i][j] < 1 or order[j] + move[i][j] > 8:
                        count -= 1
                        break

print(count)

