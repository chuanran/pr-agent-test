def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

# Test the function
test_numbers = [1, 2, 3, 4, 16, 17, 18]
results = {number: is_prime(number) for number in test_numbers}
print(results)

