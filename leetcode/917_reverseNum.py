class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        originalList = list(s)
        n = len(originalList)
        newList = list()
        letterOnlyList = list()
        for letter in originalList:
            if letter.isalpha():
                letterOnlyList.append(letter)

        for letter in originalList:
            if not letter.isalpha():
                newList.append(letter)
            else:
                newList.append(letterOnlyList.pop())
        return ''.join(newList)


if __name__ == '__main__':
    s = "ab-cd"
    a = Solution()
    s = a.reverseOnlyLetters(s)
    print(s)