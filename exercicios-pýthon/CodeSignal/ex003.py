#checkPalindrome.

def solution(inputString):
    word = ''
    for letter in range(len(inputString) -1,-1,-1):
        word += inputString[letter]
    if word == inputString:
        return True
    return False