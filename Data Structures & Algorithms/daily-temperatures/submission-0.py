class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        temp_stack = []

        for i, temp in enumerate(temperatures):
            while len(temp_stack) > 0 and temp > temp_stack[-1][0]:
                t, k = temp_stack.pop()
                output[k] = i-k
            temp_stack.append((temp, i))
        
        return output

        