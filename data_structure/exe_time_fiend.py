import time


def dominant(n: int):
    return sum(range(n))  # upper limit false so n + 1 is current value


start_time = time.time()
print(dominant(100))
end_time = time.time()

print("Script execution time", end_time - start_time)
