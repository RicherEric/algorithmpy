# Sorted Squared Array

'''
Sample Input:
array = [1,2,3,5,6,8,9]

Sample Output:
[1,4,9,25,36,64,81]

絲路: 先相乘再做排序
'''

def sortedSquaredArray(array):
    nums = []
    for num in array:
        nums.append(num*num)
    return sorted(nums)

answer = sortedSquaredArray([1,2,3,5,6,8,9])

print('answer =', answer)