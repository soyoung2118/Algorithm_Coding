k = int(input())

def func(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num % 2 == 0:
        return func(num//2)
    else:
        return 1 - func(num//2)
    
print(func(k-1))