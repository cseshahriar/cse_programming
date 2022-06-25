import time


def dominant(n: int):
    # result = 0
    # for i in range(n):
    #     result += i
    # return result       # 0.04031062126159668
    return sum(range(n))  # 0.010517120361328125


start_time = time.time()
print(dominant(1000000))  # 499999500000
end_time = time.time()

print("Script execution time", end_time - start_time)
