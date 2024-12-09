def read_input():
    with open('input.txt', 'r') as input:
        return input.readlines()

def build_matrix(raw_lines):
    return [list(line.strip()) for line in raw_lines]

# Check the row stencil: a 4x1 sub-matrix that starts at (row, col)
def row_stencil(row, col, matrix):
    end_col = col + 4
    if end_col > len(matrix[0]):
        return None
    return "".join(matrix[row][col:end_col])

# Check the col stencil: a 1x4 sub-matrix that starts at (row, col)
def col_stencil(row, col, matrix):
    end_row = row + 4
    if end_row > len(matrix):
        return None
    return "".join([matrix[r][col] for r in range(row, end_row)])

def diag_right_stencil(row, col, matrix):
    end_row = row + 3
    end_col = col + 3
    if end_row > len(matrix) or end_col > len(matrix[0]):
        return None
    
    # Wow...github copilot suggested this entire line
    return "".join([matrix[r][c] for r, c in zip(range(row, end_row), range(col, end_col))])

def diag_left_stencil(row, col, matrix):
    start_row = row + 3
    end_row = row
    end_col = col + 3
    if start_row > len(matrix) or end_col > len(matrix[0]):
        return None
    return "".join([matrix[r][c] for r, c in zip(range(start_row - 1, end_row - 1, -1), range(col, end_col))])



lines = read_input()
m = build_matrix(lines)
# cuts = [[row_stencil(r, c, m), col_stencil(r,c,m), diag_right_stencil(r,c,m), diag_left_stencil(r,c,m)] for r in range(len(m)) for c in range(len(m[0]))]
x_cuts = [[diag_right_stencil(r,c,m), diag_left_stencil(r,c,m)] for r in range(len(m)) for c in range(len(m[0]))]
# flat = [item for sublist in x_cuts for item in sublist if item is not None]
# filtered = [item for item in flat if item == "XMAS" or item == "SAMX"]
filtered = [x_item for x_item in x_cuts if (x_item[0] == "MAS" or x_item[0] == "SAM") and (x_item[1] == "MAS" or x_item[1] == "SAM")]


print(x_cuts[0])
# print(flat)
# print(len(filtered))
print(filtered)
print(len(filtered))

# print(diag_stencil(0, 0, m))