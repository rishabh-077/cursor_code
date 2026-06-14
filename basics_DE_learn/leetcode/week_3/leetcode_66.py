class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if i == -1:
            digits.insert(0, 1)
        return digits

# Time: O(n) because we are iterating through the list once
# Space: O(1) because we are not using any extra space

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits  

        return [1] + digits

# Time: O(n) because we are iterating through the list once
# Space: O(1) because we are not using any extra space