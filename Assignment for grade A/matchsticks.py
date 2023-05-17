import sys

# Skip the first input line (number of test cases)
skip = input()

# Precomputed smallest numbers for matchstick counts 2 to 17
small = {
    2: 1,
    3: 7,
    4: 4,
    5: 2,
    6: 6,
    7: 8,
    8: 10,
    9: 18,
    10: 22,
    11: 20,
    12: 28,
    13: 68,
    17: 200
}

# For each line of input
for line in sys.stdin:
    # Convert the line to an integer
    n = int(line)
    # If the matchstick count is in the precomputed dictionary, print the corresponding smallest number
    if n in small:
        print(small[n], end=' ')
    # Otherwise, compute the smallest number based on the count of matchsticks
    else:
        # k is the nearest key in the dictionary that is less than or equal to the matchstick count
        k = n % 7 + 7
        # Special case: if k is 10, add 7 to it (because 10 is not a key in the dictionary)
        if k == 10:
            k += 7
        # Start with the smallest number corresponding to k
        lead = small[k]
        # The number of '8's to append to the number is the integer quotient of (n - k) / 7
        pad = (n - k) // 7
        # Append as many '8's as calculated above
        for _ in range(pad):
            lead = lead * 10 + 8
        # Print the smallest number
        print(lead, end=' ')

    # If the matchstick count is odd, print the largest number as '7' followed by (n - 3) / 2 '1's
    if n % 2:
        print('7' + '1' * ((n - 3) // 2))
    # If the matchstick count is even, print the largest number as n / 2 '1's
    else:
        print('1' * (n // 2))
