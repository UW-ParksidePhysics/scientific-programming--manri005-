import math

# Define the function to evaluate the Gaussian function
def gaussian_function(mean, standard_deviation, input_value):
    exponent = -((input_value - mean) ** 2) / (2 * standard_deviation ** 2)
    coefficient = 1 / (standard_deviation * math.sqrt(2 * math.pi))
    result = coefficient * math.exp(exponent)
    return result

# Define the parameters
mean = 0
standard_deviation = 1
input_value = 1

# Evaluate the Gaussian function
result = gaussian_function(mean, standard_deviation, input_value)

# Print out the inputs and the output
print(f"Mean: {mean}")
print(f"Standard Deviation: {standard_deviation}")
print(f"Input Value: {input_value}")
print(f"Output of Gaussian Function: {result}")