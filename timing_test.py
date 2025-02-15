import time
import random
import string

# Generate test data
def random_string(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

secret = random_string()

# Insecure function (early exit on first mismatch)
def insecure_compare(user_input):
    for i in range(len(user_input)):
        if user_input[i] != secret[i]:
            return False
    return True

# Constant-time function (compares all characters)
def constant_time_compare(user_input):
    result = 0
    for i in range(len(user_input)):
        result |= ord(user_input[i]) ^ ord(secret[i])  # XOR comparison
    return result == 0

# Measure execution time
def measure_time(func, user_input):
    start = time.perf_counter_ns()  # High-precision timer
    func(user_input)
    end = time.perf_counter_ns()
    return end - start

# Test runs
test_inputs = [random_string() for _ in range(100)]

insecure_times = [measure_time(insecure_compare, inp) for inp in test_inputs]
constant_times = [measure_time(constant_time_compare, inp) for inp in test_inputs]

# Output results
print(f"Avg Insecure Time: {sum(insecure_times) / len(insecure_times)} ns")
print(f"Avg Constant-Time: {sum(constant_times) / len(constant_times)} ns")
