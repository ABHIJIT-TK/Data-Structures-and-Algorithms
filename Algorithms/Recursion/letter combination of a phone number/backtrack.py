from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        c = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append(''.join(path))
                return
            for letter in c[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations

# Example usage
solution = Solution()
print(solution.letterCombinations('23'))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
