# Validate Subsequence

'''
Sample Input-
array:
[5, 1, 22, 25, 6, -1, 8, 10]
sequence
[1, 6, -1, 10]

Sample Output-
True

絲路: 以seq_idx作為指向，逐一檢查array中

'''

#  O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seq_idx = 0
    for num in array:
        # edge case
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == num:
            seq_idx += 1
    return seq_idx == len(sequence)


anwser = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 25, 6, -1, 8, 10])
print('anwser =', anwser)

