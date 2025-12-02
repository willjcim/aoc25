def get_divisors(number: int):
    divisors = []
    for i in range(1, number + 1):
        # if the number divides evenly, add it to the list
        if number % i == 0: 
            divisors.append(i)

    return divisors

def get_invalid_ids(file_name: str):
    # var declaration
    invalid_ids = []
    id_list = ""
    
    # read file 
    with open(file_name, 'r') as file:
        id_list = file.readline().strip('\n')
    
    for id_range in id_list.split(','): # cycle through all id ranges
        bottom_range = int(id_range.split('-')[0])
        top_range = int(id_range.split('-')[1])

        for i in range(bottom_range, top_range+1, 1): # cycle through all ids in the range
            id = str(i)
            
            divisors = get_divisors(len(id)) # get all of the possible splits of the id 

            for divisor in divisors: 
                # split the id into equal chunks based on the current divisor
                id_blocks = []
                for j in range(0, len(id), divisor):
                    id_blocks.append(id[j:j+divisor])

                # if we're at the last element in the block, break to avoid FP
                if len(id_blocks) == 1:
                    break

                # compare each section of the id in the given split
                all_equal = True
                for element in id_blocks:
                    if element != id_blocks[0]:
                        all_equal = False
                        break
                
                if all_equal: # if the id is repeating, add it to the list and move onto the next one
                    invalid_ids.append(i)
                    break
    
    return invalid_ids

invalid_ids = get_invalid_ids("input.txt")
print(f'Invalid ID sum: {sum(invalid_ids)}')
