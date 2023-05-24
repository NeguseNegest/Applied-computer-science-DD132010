
# Function to calculate smallest possible number with n matchsticks
def get_min(n):
    # Initialize the list with None for all indices
    if n<2 or n>100:
        raise ValueError('Invalid input: n must be within bound 2<=n<=100.')

    computed_numbers = [None for _ in range(n+1)]
  
    # The first 21 values are known directly.
    # Here, I'm using Python's zero-based indexing, so there's an offset of 2
    smallest_nums = [1, 7, 4, 2, 6, 8, 10, 18, 22, 20, 28, 68, 88, 108, 188, 200, 208, 288, 688, 888, 1088, 1888]


    for i in range(2, n+1):
        if i < len(smallest_nums):
            # We already know the answer for this
            computed_numbers[i] = str(smallest_nums[i-2])
        else:
            # Otherwise, calculate it based on previously known values
            computed_numbers[i] = computed_numbers[i-2] + '1' if 21 <= i <= 23 and int(computed_numbers[i-2] + '1') < int(computed_numbers[i-7] + '8') else computed_numbers[i-7] + '8'
    # Return the result for n
    return computed_numbers[n]



# Function to calculate largest possible number with n matchsticks
def get_max(n):
    # If n is odd, we start with '7' (requires 3 matchsticks) and then add as many '1's as possible
    if n % 2 == 1:
        return "7" + "1" * ((n - 3) // 2)
    else:
        return "1" * (n // 2)


# Function to get smallest & largest number possible
def compute(n):
    smallest = get_min(n) #return the smallest
    largest = get_max(n) #return the largest
    return f"{smallest} {largest}"

# Main function
def main():
    # Number of test cases
    val = int(input())
    cases = []

    # Read all test cases
    for _ in range(val):
        n = int(input())
        cases.append(n)

    results = [compute(n) for n in cases]

    # Print the results
    for result in results:
        print(result)

    

if __name__ == "__main__":
    main()

