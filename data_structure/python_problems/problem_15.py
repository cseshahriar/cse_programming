# inputs
n = int(input("Please enter a number "))

S = list(map(int, input("Enter numbers ").strip().split()))[:n] 
S.sort()

Q = list(map(int, input("Enter numbers ").strip().split()))[:n] 
Q.sort()

data = []
for i in S:
    if i not in Q:
        data.append(i)

print(data)