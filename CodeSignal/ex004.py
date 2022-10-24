#adjacentElementsProduct

def solution(inputArray):
    greater = inputArray[0] * inputArray[1]
    for index in range(len(inputArray)):
        if not index == len(inputArray) - 1:
            n1 = inputArray[index]
            n2 = inputArray[index+1]
            result = n1 * n2
            if result > greater:
                greater = result
    return greater