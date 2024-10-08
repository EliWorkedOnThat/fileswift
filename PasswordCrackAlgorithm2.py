import time


def brute_force_counting(correct_password):
    password_length = len(correct_password)
    max_value = 10 ** password_length - 1  # Maximum value for the given number of digits

    start_time = time.perf_counter()  # Start time for performance measurement

    for i in range(1, max_value + 1):
        guess = str(i).zfill(password_length)  # Fill leading zeros to match password length
        print(f"Trying: {guess}")
        if guess == correct_password:
            end_time = time.perf_counter()  # End time
            total_time = end_time - start_time
            print(f"Password {guess} is correct!")
            print(f"Time taken: {total_time:.6f} seconds")
            return guess

    print("Failed to find the password.")
    return None


# Example usage
correct_password = '123456789'
brute_force_counting(correct_password)
