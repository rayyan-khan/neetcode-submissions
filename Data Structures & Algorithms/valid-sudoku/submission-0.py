class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # validate rows
        for row in board:
            if not self.validate_set_of_values(row):
                print(f"row {row} did not pass")
                return False

        # validate columns
        for col_idx in range(len(board)):
            col_list = self.get_col_list(board, col_idx)
            if not self.validate_set_of_values(col_list):
                print(f"column {col_list} with col_idx {col_idx} did not pass")
                return False

        # validate sub-boxes
        list_of_boxes = self.get_sub_boxes(board)
        for box in list_of_boxes:
            if not self.validate_set_of_values(box):
                print(f"sub-box {box} did not pass")
                return False
        
        return True

    def get_sub_boxes(self, board: List[List[str]]) -> List[List[str]]:
        list_of_boxes = []
        iter_ranges = [range(0,3), range(3,6), range(6,9)]

        for row_range in iter_ranges:
            for col_range in iter_ranges:
                new_sub_box = []
                for r in row_range:
                    for c in col_range:
                        new_sub_box.append(board[r][c])
                list_of_boxes.append(new_sub_box)
        return list_of_boxes

    def get_col_list(self, board: List[List[str]], c_idx) -> List[str]:
        col_list = []
        for row in board:
            col_list.append(row[c_idx])
        return col_list

    def validate_set_of_values(self, vals_list: List[str]) -> bool:
        valid_values = set(str(num) for num in range(1,10)) | {"."}
        if not set(vals_list) <= valid_values:
            return False
        
        seen_before = set()
        for value in vals_list:
            if value in seen_before and value != '.':
                return False
            else:
                seen_before.add(value)
        
        return True

    

        