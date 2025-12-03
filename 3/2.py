def get_largest_joltage(file_name: str, cell_count: int):
    # var declaration
    total_joltage = 0

    # read file 
    with open(file_name, 'r') as batteries:
        for battery_bank in batteries:
            battery_bank_list = list(battery_bank.strip('\n'))

            # start with just the first n battery cells in the bank 
            strongest_cells = battery_bank_list[:cell_count]

            # go through all of the cells in the battery bank
            for cell in range(cell_count, len(battery_bank_list), 1): 
                # go through each of the cells in the strongest cells list 
                for strong_cell in range(0, cell_count, 1):
                    # test with each item in the strongest_cells list removed and the next item in the bank added at the tail
                    tmp_list = strongest_cells[:]
                    del tmp_list[strong_cell]
                    tmp_list.append(battery_bank[cell])

                    # if tmp_list is greater than what we currently have as the strongest batteries, overwrite it 
                    if int("".join(strongest_cells)) < int("".join(tmp_list)):
                        strongest_cells = tmp_list
                        break

            joltage = int("".join(strongest_cells))

            total_joltage = total_joltage + joltage
    return total_joltage

joltage = get_largest_joltage("sample_input.txt", 12)
print(f'joltage: {joltage}')
