import re

expr = re.sub(r'\b0+(\d+)', r'\1', input())
lst = expr.split('-')
for i in range(len(lst)):
    lst[i] = str(eval(lst[i]))  

expr = '-'.join(map(str, lst))
result = eval(expr)

print(result)