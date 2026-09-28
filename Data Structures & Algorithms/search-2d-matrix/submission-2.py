class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check the start of every row to determine which row it is in
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # then binary search the row it is in
                return self.binsearch(matrix[mid], target)
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        return False 

    def binsearch(self, row: List[int], target: int) -> bool:
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid+1
            else:
                r = mid-1 
        return False
        