def isAlternating(list):
    for index in range(1, len(list)):
        if(list[index] == list[index-1]):
            return False
    return True

def paintArray(a):
    for d in range(1, max(a)+1):
        temp = a.copy()
        for index in range(len(temp)):
            temp[index] = 1 if temp[index]%d==0 else 0
        if isAlternating(temp):
            return d
    return 0

testCases = input()
out = []
for i in range(int(testCases)):
	arrayLen = input()
	arrayInput = input().split()
	array = [int(i) for i in arrayInput]
	out.append(paintArray(array))
for num in out:
	print(num)
