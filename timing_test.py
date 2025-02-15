import time
import random
import string
import csv

# Generate test data
def random_string(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

secret = random_string()

def insecure_compare(user_input):
    for i in range(len(user_input)):
        if user_input[i] != secret[i]:
            return False
    return True

def constant_time_compare(user_input):
    result = 0
    for i in range(len(user_input)):
        result |= ord(user_input[i]) ^ ord(secret[i])
    return result == 0

def measure_time(func, user_input):
    start = time.perf_counter_ns()
    func(user_input)
    end = time.perf_counter_ns()
    return end - start

# Collect timing data
test_inputs = [random_string() for _ in range(100)]
data = []

for inp in test_inputs:
    insecure_time = measure_time(insecure_compare, inp)
    constant_time = measure_time(constant_time_compare, inp)
    data.append([inp, "insecure", insecure_time])
    data.append([inp, "constant", constant_time])

# Save to CSV
with open("timing_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["input", "type", "time_ns"])
    writer.writerows(data)

print("Timing data saved to timing_data.csv")
