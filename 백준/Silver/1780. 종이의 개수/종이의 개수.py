n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

result = [0, 0, 0]  

def append_result(value):
    if value == -1:
        result[0] += 1
    elif value == 0:
        result[1] += 1
    elif value == 1:
        result[2] += 1

def check(x_start, y_start, length):
    sval = lst[x_start][y_start]

    if length == 1: 
        append_result(sval)
        return

    same = True

    for i in range(x_start, x_start + length):
        for j in range(y_start, y_start + length):
            if lst[i][j] != sval:
                same = False
                break
        if not same:
            break

    if same:
        append_result(sval)
    else:
        length = length // 3
        for i in range(3):
            for j in range(3):
                check(x_start + i * length, y_start + j * length, length)

check(0, 0, n)

print(result[0])
print(result[1])
print(result[2])
