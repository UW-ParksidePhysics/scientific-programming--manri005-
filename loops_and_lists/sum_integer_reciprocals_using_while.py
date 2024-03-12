# Mathod 1
# Errors:
# 1. The loop never updates the index variable, leading to an infinite loop.
# 2. The loop should start from the starting_index, not 1.
# 3. The loop should include the maximum_index value.
# 4. The loop should use the index variable to calculate the reciprocal.
# Method 2
# This should output approximately 5.187377
# Corrected script
summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index <= maximum_index:  # Include maximum_index value
    summation += 1/index
    index += 1  # Increment the index variable

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')