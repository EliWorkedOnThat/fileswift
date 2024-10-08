import time


def brute_force_partial_match_chunks(correct_pin, chunk_size=2):
    pin_length = len(correct_pin)
    guess = ['0'] * pin_length  # Initialize the guess as a list of '0's

    start_time = time.perf_counter()  # Record the start time with higher precision

    # Iterate through the pin in chunks
    for chunk_start in range(0, pin_length, chunk_size):
        chunk_end = min(chunk_start + chunk_size, pin_length)  # End of the chunk (ensures no overflow)

        for position in range(chunk_start, chunk_end):
            for digit in range(10):  # Digits from 0 to 9
                guess[position] = str(digit)  # Try the current digit in the correct position
                print(f"Trying combination: {''.join(guess)}")
                # Only compare up to the current position within the chunk
                if ''.join(guess[chunk_start:position + 1]) == correct_pin[chunk_start:position + 1]:
                    # Move to the next position if this part of the guess is correct
                    break
            else:
                # If no break happens, we failed to find the right digit for this position
                print("Failed to find the combination.")
                return None

        # Print the correct chunk after it's fully guessed
        print(f"Correct chunk {chunk_start // chunk_size + 1}: {''.join(guess[chunk_start:chunk_end])}")

    end_time = time.perf_counter()  # Record the end time with higher precision
    total_time = end_time - start_time  # Calculate the total time taken

    print(f"Combination {''.join(guess)} is correct!")
    print(f"Time taken: {total_time:.6f} seconds")  # Display time with more precision
    return ''.join(guess)


# Example usage
correct_pin = '12345678987654321'
brute_force_partial_match_chunks(correct_pin)
