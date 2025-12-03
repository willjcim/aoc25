def find_largest_battery(battery_bank: str, starting_index: int, ending_index: int, restart: bool):
    # var declaration
    highest_battery_index = 0
    battery_val = -1
    
    # go through all cells in the battery bank, given the provided range
    for cell in range(starting_index, ending_index, 1):
        if int(battery_bank[cell]) > battery_val:
            battery_val = int(battery_bank[cell])
            highest_battery_index = cell

    # if we the highest battery is at the end of the battery bank and we allow recursion, run again for the lower range 
    if highest_battery_index+1 == len(battery_bank) and restart:
        battery_val, highest_battery_index = find_largest_battery(battery_bank, starting_index, highest_battery_index, restart = False)
    
    return battery_val, highest_battery_index

def get_largest_joltage(file_name: str):
    # var declaration
    total_joltage = 0

    # read file 
    with open(file_name, 'r') as batteries:
        for battery_bank in batteries:
            battery_bank = battery_bank.strip('\n')

            battery_one, battery_one_index = find_largest_battery(battery_bank, 0, len(battery_bank), restart=True)
            battery_two, battery_two_index = find_largest_battery(battery_bank, battery_one_index+1, len(battery_bank), restart=False)

            total_joltage = total_joltage + battery_one*10 + battery_two
    return total_joltage

joltage = get_largest_joltage("input.txt")
print(f'joltage: {joltage}')
