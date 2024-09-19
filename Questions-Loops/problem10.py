import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt number:", attempts + 1, ". Your wait time is:", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempts = attempts + 1