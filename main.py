class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = []
        return sum(
            [num for i in range(len(arr)) for j in range(i + 1, len(arr) + 1) if len(arr[i:j]) % 2 != 0 for num in
             arr[i:j]])
