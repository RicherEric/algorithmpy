# SelectionSort

'''
Sample Input:
array = [8, 5, 2, 9, 5, 6, 3]

Sample Output:
[2, 3, 5, 5, 6, 8, 9]

絲路: 輪巡idx，從當下idx之後所有idx中取得最小的數值，將最小數值idx與當前idx數值交換 
'''

def selectionSort(array):
	currentIdx = 0
	while currentIdx < len(array) - 1:
		smallestIdx = currentIdx
		for i in range(currentIdx + 1, len(array)):
			if array[smallestIdx] > array[i]:
				smallestIdx = i
		swap(currentIdx, smallestIdx, array)
		currentIdx += 1
	return array
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]


print("result: ", selectionSort([8, 5, 2, 9, 5, 6, 3]))