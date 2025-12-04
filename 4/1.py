def get_adj_rolls(map,  col,    row):
    adj_rolls = 0
    # left col
    if col != 0:    
        if row != 0: # top
            if map[row-1][col-1] == '@':
                adj_rolls += 1
        if map[row][col-1] == '@': # middle
            adj_rolls +=1
        if row != len(map)-1: # bottom
            if map[row+1][col-1] == '@':
                adj_rolls += 1
                
    # middle col
    if row != 0: # top
        if map[row-1][col] == '@':
            adj_rolls += 1
    if row != len(map)-1: # bottom
        if map[row+1][col] == '@':
            adj_rolls += 1
            
    # right col
    if col != len(map[row])-1:
        if row != 0: # top
            if map[row-1][col+1] == '@':
                adj_rolls +=1
        if map[row][col+1] == '@': # middle
            adj_rolls += 1
        if row != len(map)-1: # bottom
            if map[row+1][col+1] == '@':
                adj_rolls += 1
                
    return adj_rolls
    
    
def find_forkable_rolls(input_file):
    map = []
    with open(input_file,'r') as file:
        for row in file:
            map.append(list(row.strip('\n')))
        
    forkable_rolls = 0
    for i in range(0, len(map), 1):
        for j in range(0, len(map[i]), 1):
            if map[i][j] == '@':
                adj_rolls = get_adj_rolls(map, j, i)
                if adj_rolls < 4:
                    forkable_rolls += 1
                
    return forkable_rolls

print(f'forkable_rolls: {find_forkable_rolls("sample_input.txt")}')