def boyerMooreSearch(pattern, text):
    textLength, patternLength = len(text), len(pattern)
    if patternLength == 0:
        # trivial search for an empty string
        return 0

    # dictionayr to store the last index of characters in the pattern
    last = {char: i for i, char in enumerate(pattern)}


    i = patternLength - 1 # index into text
    k = patternLength - 1 # index into pattern

    while i < textLength:
        if text[i] == pattern[k]:
            if k == 0:
                # match was found for all characters in pattern 
                return i
            else:
                # go the next left character in both text and pattern
                i -= 1
                k -= 1
        else:
            # if pattern and text do not match at certain index, get the next right most character in pattern
            # that matches the text character,
            j = last.get(text[i], -1)
            i += textLength -min(k, j + 1)
            k = textLength -1
    return -1


"""
+------------+----------------------+
| Input Size |   Running Time (s)   |
+------------+----------------------+
|    1000    | 0.034794159000739455 |
|    5000    | 0.03609677300119074  |
|   10000    | 0.036083359002077486 |
|   15000    | 0.03541673699510284  |
|   50000    | 0.035806776002573315 |
|   100000   | 0.03740485500020441  |
|   200000   | 0.03339349899761146  |
|   395470   | 0.03441448200464947  |
+------------+----------------------+




# Description

A relatively faster string searching algorithm since its able to skip having to making comparisons for certain alignments of the pattern relative to the text.

Its able to skip these comparisons by floowing a few rules:
1. Looking glass heuristic: checks if a pattern matches from right to left, starts at the end of the pattern.
2. Bad character rule:
    - Guides on how far right to shift the pattern when a mismatch occurs at a a particaular character, based on next last occurence of the character in the pattern.
It also makes use of a preprocessing step to generate a lookup table that is used to help faster get the  number of positions to shift the pattern.

##  Theoretical background

Time complexity

O(nm) In the worst case it might still need to exercise the whole of the text. This is however does not happen as often for language text, thus its faster than naive text search in such  a case.

Space complexity

O(m + n)

References:

1. Goodrich, M.T., Goldwasser, M.H. and Tamassia, R. (2013) Data structures and Algortihms in python. New York: Wiley. 

2. Ibsen and Archer (2023) The Collected Works of Henrik Ibsen, vol. 07 (of 11) by Henrik Ibsen, Project Gutenberg. Available at: https://www.gutenberg.org/ebooks/70566 (Accessed: April 21, 2023). 
"""

