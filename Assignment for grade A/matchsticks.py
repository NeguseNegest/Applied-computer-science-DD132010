# Dictionary for memoization
computed_numbers = {}

# Function to calculate smallest possible number with n matchsticks
def get_min(n):
    # If we have previously computed this, return the stored value
    if n in computed_numbers:
        return computed_numbers[n]

    # Array of smallest numbers that can be made with 2 to 20 matchsticks
    sol = [1, 7, 4, 2, 6, 8, 10, 18, 22, 20, 28, 68, 88, 108, 188, 200, 208, 288, 688, 888]

    # If n is less than or equal to 20, we can directly index into the array
    if n <= 20:
        result = str(sol[n - 2])
        computed_numbers[n] = result
        return result

    # For n > 20, we need to calculate the number of '8's and the leading number
    digits = (n // 7) - 3
    index = (n % 7) + 12

    res = str(sol[index])

    # Append '8's to the leading number
    for _ in range(digits + 1):
        res += "8"

    # Store the result in the dictionary for future reference
    computed_numbers[n] = res
    return res

# Function to calculate largest possible number with n matchsticks
def get_max(n):
    res = ""

    # If n is odd, we start with '7' (requires 3 matchsticks) and then add as many '1's as possible
    if n % 2 == 1:
        res += "7"
        n -= 3

    # If n is even, we add as many '1's as possible
    for _ in range(n // 2):
        res += "1"

    return res

# Function to solve a single case
def solve_case(n):
    smallest = get_min(n)
    largest = get_max(n)
    return f"{smallest} {largest}"

# Main function
def main():
    # Number of test cases
    t = int(input())
    cases = []

    # Read all test cases
    for _ in range(t):
        n = int(input())
        cases.append(n)

    # Solve all test cases
    results = [solve_case(n) for n in cases]

    # Print the results
    for result in results:
        print(result)

# Entry point of the script
if __name__ == "__main__":
    main()
