def get_invalid_ids(file_name: str):
    # var declaration
    invalid_ids = []
    id_list = ""
    
    # read file 
    with open(file_name, 'r') as file:
        id_list = file.readline().strip('\n')
    
    # cycle through all id ranges
    for id_range in id_list.split(','):
        bottom_range = int(id_range.split('-')[0])
        top_range = int(id_range.split('-')[1])

        for i in range(bottom_range, top_range+1, 1): # cycle through all ids in the range
            id = str(i)

            first_half  = id[:len(id)//2]
            second_half = id[len(id)//2:]

            if first_half == second_half:
                invalid_ids.append(int(id))
    
    return invalid_ids

invalid_ids = get_invalid_ids("input.txt")
print(f'Invalid ID sum: {sum(invalid_ids)}')
