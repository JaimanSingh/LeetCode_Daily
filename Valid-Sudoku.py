1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        # board is a 9x9 Sudoku grid
4        # Each cell contains '1'-'9' or '.' (empty cell)
5        # We must check if the board is valid according to Sudoku rules
6        
7        # ---------------- DATA STRUCTURES ----------------
8        
9        rows = [set() for x in range(9)]
10        # Create a list of 9 sets
11        # rows[i] will store numbers already seen in row i
12        # Using set because:
13        # - Fast lookup (O(1))
14        # - Automatically prevents duplicates
15        
16        columns = [set() for x in range(9)]
17        # Create a list of 9 sets
18        # columns[j] will store numbers already seen in column j
19        
20        squares = [[set() for x in range(3)] for y in range(3)]
21        # Create a 3x3 grid of sets
22        # Each set represents one of the 9 small 3x3 Sudoku boxes
23        # squares[i][j] corresponds to a specific 3x3 box
24        
25        # ---------------- TRAVERSE THE BOARD ----------------
26        
27        for x in range(9):
28            # Loop through rows (0 to 8)
29            
30            for y in range(9):
31                # Loop through columns (0 to 8)
32                
33                cell_value = board[x][y]
34                # Get the current cell value
35                
36                if cell_value == ".":
37                    # If the cell is empty, skip it
38                    continue
39                
40                # Check if number already exists in:
41                # - same row
42                # - same column
43                # - same 3x3 square
44                if (cell_value in rows[x] or 
45                    cell_value in columns[y] or 
46                    cell_value in squares[x//3][y//3]):
47                    
48                    # If number already exists in any of them,
49                    # Sudoku rule is violated
50                    return False
51                
52                # If no violation, add number to tracking sets
53                
54                rows[x].add(cell_value)
55                # Add number to current row set
56                
57                columns[y].add(cell_value)
58                # Add number to current column set
59                
60                squares[x//3][y//3].add(cell_value)
61                # Add number to correct 3x3 square
62                # x//3 gives square row index (0,1,2)
63                # y//3 gives square column index (0,1,2)
64        
65        # If no duplicates found after full traversal
66        return True
67        # Sudoku board is valid
68