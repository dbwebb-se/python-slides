import random
import time


n = 10000000
random_list = random.sample(range(n * 10), n)

start = time.time()
median = sorted(random_list, reverse=True)[n // 2]
end = time.time()

print(median)
print(end - start)
