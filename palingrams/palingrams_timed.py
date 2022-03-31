"""
Profiling

Runs find_palingrams.

Timing performance with the time module
"""
import time
import palingrams_optimized

start_time = time.time()
palingrams = palingrams_optimized.find_palingrams()
end_time = time.time()
print(palingrams)
print(f"Runtime for this program was {end_time - start_time} seconds")
