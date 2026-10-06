class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l = 0
        m = len(matrix)
        n = len(matrix[0])
        r = m*n-1
        d=0
        i,j=0,0
        while l <= r:
            d = l+((r-l)//2)
            middle = self.convert_1D_to_2D(d,m,n,matrix)
            if middle > target :
                r = d-1
            elif middle < target:
                l = d+1
            elif middle == target:
                return True   
        return False
    def convert_1D_to_2D(self,d:int,m:int,n:int,matrix:List[List[int]]):
        i = d//n
        j=d%n
        return matrix[i][j]



                

        