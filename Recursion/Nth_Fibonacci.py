'''
Nth Fibonacci

(1)
Sample Input:
n = 2

Sample Output:
1
(2)
Sample Input:
n = 6

Sample Output:
5
'''

# O(2 ^n) time| O(n) space
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

print(getNthFib(8))