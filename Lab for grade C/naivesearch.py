def naiveSearch(pattern, text):
    textLength, patternLength = len(text), len(pattern)
    # outer loop checks all possible index offsets on text
    for i in range(textLength-patternLength + 1):
        idx = 0
        # inner loop checks if pattern matches corresponding sequence of text
        while (idx < 0 and text[i + idx] == pattern[idx]):
            idx += 1
        if(idx == patternLength):
            return i
    return -1




"""
+------------+---------------------+
| Input Size |   Running Time (s)  |
+------------+---------------------+
|    1000    | 0.32957540699862875 |
|    5000    |  1.7782515319995582 |
|   10000    |  3.816336906995275  |
|   15000    |  7.147996501997113  |
|   50000    |  22.178338282996265 |
|   100000   |   44.6754735229988  |
|   200000   |  92.59192246900056  |
|   395470   |  163.68538311600423 |
+------------+---------------------+


Description:

Naive text search tests all possible offsets of the pattern relative to the text untill a match is either found or not.


THEORETICAL BACKGROUND

Time complexity

Taking that n = length of text T, and m = length of pattern P.
The naive text search makes use of 2 lopos, where one is nested. The outer loop indexes through all possible offset of 
the pattern on text T, while the inner loop checks that the next sequence of characters of length m, do match the pattern.

The outer loop is executed n-m+1 tmes and the inner loop is executed m times. This gives the 
worst case running time of O(nm).

Space Complexity

space requirements is (n + m), where n is space proportional to the length of text, and m is space proportional to te length of patterh

"""
