import time
from stopwatch import Stopwatch

stopwatch = Stopwatch()
stopwatch.start()
time.sleep(3.0)

stopwatch.stop()
total_time = stopwatch.elapsed

print(round(total_time,2))