# TwoNumberSum

'''
Sample Input-
[3, 5, -4, 8, 11, 1, -1, 6], target: 10

Sample Output-
[-1, 11]

絲路: 將array中每個值取出來存在x中，將每個x存在hashMap中，
      y = target - x, 檢查y 是否在Map中，如果沒有則繼續檢查下一個值
      如果有則返回 [y, x]
'''

# O(n) time | O(n) time
def twoNumberSum(array, targetSum):
    nums = {}
    answer_array = []
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            answer_array = [potential_match, num]
            return answer_array
        else:
            nums[num] = True
    return answer_array

answer = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
print('answer =' , answer)