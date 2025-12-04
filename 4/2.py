def print_map(map):
    for row in map:
        print("".join(row))
    print('\n\n')

def deep_copy(v): # i regret doing this year in python
    if isinstance(v, list):
        return [deep_copy(e) for e in v]
    return v

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

    display_map = deep_copy(map)
    print_map(display_map)
    
    forkable_rolls = 0
    while True:
        forkable_rolls_tmp = int(f"{forkable_rolls}") 

        # cycle through map
        for i in range(0, len(map), 1):
            for j in range(0, len(map[i]), 1):
                if map[i][j] == '@':
                    adj_rolls = get_adj_rolls(map, j, i)
                    if adj_rolls < 4:
                        forkable_rolls_tmp += 1
                        display_map[i][j] = 'x'
        
        if forkable_rolls_tmp == forkable_rolls:
            break
        else:
            forkable_rolls = int(f'{forkable_rolls_tmp}')
            map = deep_copy(display_map) # redo but with the display map (since it covered the @'s in x's)
    
    print_map(display_map)
    return forkable_rolls

forkable_rolls = find_forkable_rolls("input.txt")
print(f'forkable rolls: {forkable_rolls}')