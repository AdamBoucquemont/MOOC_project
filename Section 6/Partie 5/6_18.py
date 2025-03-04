def naked_single(grid):
    is_change = True
    still_blanck = True
    while is_change and still_blanck:
        is_change = False
        still_blanck = False
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    valid_numbers = set(range(1, 10))
                    line = [grid[i][row] for row in range(len(grid))]
                    colonne = [grid[col][j] for col in range(len(grid))]
                    region = []
                    for indice_row in range(3):
                        for indice_col in range(3):
                            region.append(grid[3 * (i // 3) + indice_row][3 * (j // 3) + indice_col])
                    all_numbers = set(line) | set(colonne) | set(region)
                    all_numbers.remove(0)
                    possible_numbers = valid_numbers - all_numbers
                    if len(possible_numbers) == 1:
                        grid[i][j] = possible_numbers.pop()
                        is_change = True
                    else:
                        still_blanck = True
    if not still_blanck:
        return (True, grid)
    return (False, None)
    
print(naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
              [0, 0, 2, 8, 0, 1, 0, 0, 3],
              [0, 1, 0, 0, 0, 0, 0, 0, 7],
              [0, 4, 0, 7, 0, 0, 0, 2, 6],
              [5, 0, 7, 0, 1, 0, 4, 0, 9],
              [1, 2, 0, 0, 0, 3, 0, 8, 0],
              [2, 0, 0, 0, 0, 0, 0, 7, 0],
              [7, 0, 0, 2, 0, 9, 8, 0, 0],
              [0, 6, 0, 1, 5, 0, 3, 0, 2]]))

print(naked_single([[0, 0, 6, 0, 4, 0, 1, 0, 0],
              [0, 5, 0, 0, 9, 0, 0, 6, 0],
              [8, 0, 0, 0, 0, 0, 0, 0, 5],
              [0, 0, 0, 3, 0, 4, 0, 0, 0],
              [3, 1, 0, 0, 0, 0, 0, 4, 8],
              [0, 0, 0, 8, 0, 7, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 0, 0, 9],
              [0, 2, 0, 0, 3, 0, 0, 5, 0],
              [0, 0, 1, 0, 5, 0, 7, 0, 0]]))