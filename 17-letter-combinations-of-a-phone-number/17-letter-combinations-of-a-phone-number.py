class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        combinations = []
        for digit in digits:
            combinations.append(letters[digit])
        
        while len(combinations) > 1:
            combo_right = combinations.pop()
            combo_left = combinations.pop()
            
            answers = []
            
            for l1 in combo_left:
                for l2 in combo_right:
                    answers.append(l1 + l2)
            
            combinations.append(answers)
            
        return combinations[0]