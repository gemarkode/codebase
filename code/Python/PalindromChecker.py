def checkPalindrome(str):
    reversedStr = ''.join(reversed(str))

    if (str == reversedStr):
        return True
    return False


print(checkPalindrome("halah"))
