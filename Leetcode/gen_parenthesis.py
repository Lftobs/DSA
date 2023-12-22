'''
Link to challenge: https://leetcode.com/problems/generate-parentheses/
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        outcomes = []
        def generate_parentheses(arrangement, left_count, right_count, n):

            if left_count == n and right_count == n:
                outcomes.append(arrangement)
                return 

            if left_count < n:
                generate_parentheses(arrangement + '(', left_count + 1, right_count, n)

            if right_count < left_count:
                generate_parentheses(arrangement + ')', left_count, right_count + 1, n)
        generate_parentheses('', 0, 0, n)
        return outcomes
