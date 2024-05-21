#Time Complexity : O(2n)
#Space Complexity : O(n)
#Any problem you faced while coding this : -

#The approach is to use monotonic decreasing stack to store the intermediate elements. The temperatures would be stacked up until the next warmer(lesser) temperature is found.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return list()
        result = [0 for _ in range(len(temperatures))]
        stack = list()

        for i in range(len(temperatures)):
            while(len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]):
                popped = stack.pop()
                result[popped] = i - popped

            stack.append(i)

        return result