"""
Profiling

Runs find_palingrams.

Timing performance with the time module
"""
import time
import palingrams

start_time = time.time()
palingrams = palingrams.find_palingrams()
end_time = time.time()
print(palingrams)
print(f"Runtime for this program was {end_time - start_time} seconds")
