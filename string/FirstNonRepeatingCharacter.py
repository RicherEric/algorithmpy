'''
Sample Input
string = "abcdcaf"

Sample Output
1
'''

def firstNonRepeatingCharacter(string):
    # Write your code here.
    counts = {}
    nonReaArray = []
    result = -1
    for character in string:
        counts[character] = counts.get(character, 0) + 1
    for k,v in counts.items():
        if v == 1:
            nonReaArray.append(k)
    print('counts =', counts)
    if nonReaArray:
        nonReaArray.sort()
        print('nonReaArray = ', nonReaArray)
        result = list(string).index(nonReaArray[0])	
    return result

string = "ggyllaylacrhdzedddjsc"

a = firstNonRepeatingCharacter(string)
print('a =', a)