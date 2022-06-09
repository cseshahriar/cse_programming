n, choose = map(int, input().split())

result = 0
data = []

if choose == 1:
    for i in range(n+1):
        data.append(i)

    result = sum(data)
elif choose == 2:
    for i in range(n):
        data.append(i)

    result = 1
    for i in data:
        result += result * i

print("The result is ", result)