#Time Complexity : O(2n)
#Space Complexity : O(n)
#Any problem you faced while coding this : -

#The approach is to use monotonic increasing stack to store the intermediate elements. The elements would be stacked up until the next greater element is found. As the array is circular, there would be two rotations.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1 for _ in range(n)]
        stack = list()

        for i in range(2*n):
            while len(stack) != 0 and nums[i%n] > nums[stack[-1]]:
                popped = stack.pop()
                result[popped] = nums[i%n]

            if i < n:
                stack.append(i)

        return result