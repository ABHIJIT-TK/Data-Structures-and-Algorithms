from itertools import product
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        if not digits:
            return []
        comb=['']
        temp=[]
        for i in digits:
            temp.append(c[i])
        return [''.join(prod) for prod in product(*temp)]

# Example usage
solution = Solution()
print(solution.letterCombinations('23'))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
