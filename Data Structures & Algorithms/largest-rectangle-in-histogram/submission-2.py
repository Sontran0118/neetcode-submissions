class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        leftmost = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftmost[i] = stack[-1]
            stack.append(i)
        stack = []

        right_most = [len(heights)] *len(heights)

        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
               stack.pop()
            if stack:
                right_most[i] = stack[-1]
            stack.append(i)
        
        maxarea = 0
        i = 0
        for left, right in zip(leftmost,right_most):
            area = heights[i]* (right -left -1)
            if maxarea<area:
                maxarea = area
            i+=1

       
        return maxarea
            

        

                
                
            


        