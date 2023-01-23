import random
import time

def quick_select(arr, n):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if n < num_less:
        return quick_select(below, n)
    elif n >= num_lessoreq:
        return quick_select(above, n-num_lessoreq)
    else:
        return pivot

n = 10000000
random_list = random.sample(range(n * 10), n)

start = time.time()
median = quick_select(random_list, n // 2)
end = time.time()

print(median)
print(end - start)
