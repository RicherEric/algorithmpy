'''
Sample Input:
intervals = [[1,2], [3,5], [4,7], [6,8], [9,10]]

Sample Output:
[[1,2], [3,8], [9,10]]

絲路: 

'''
intervals = [[1,2], [3,5], [4,7], [6,8], [9,10]]
sortedIntervals = sorted(intervals, key=lambda x: x[0])
mergedIntervals = []
currentInterval = sortedIntervals[0]
mergedIntervals.append(currentInterval)
for nextInterval in sortedIntervals:
    _, currentIntervalEnd = currentInterval
    print('_ =', _)
    print('currentIntervalEnd =', currentIntervalEnd)