import time

start_time=time.time()

for a in range(0,10000):
    for b in range(0,10000):
        pass
end_time=time.time()
print("How long did it take?")
print(f"It took: {end_time - start_time:.3f} seconds")







