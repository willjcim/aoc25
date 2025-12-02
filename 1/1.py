def get_code(file_name):
    # starting values 
    dial = 50
    code = 0
    with open(file_name, 'r') as file:
        for line in file:
            # rotate the dial
            direction, rotation = line[0], int(line[1:])
            if direction == 'L':
                dial = dial - rotation
            elif direction == "R":
                dial = dial + rotation
            else:
                raise Exception(f'Incompatible direction: {line}')
            
            # if the dial looped, bring it back within 100
            if dial > 99:
                while dial > 99:
                    dial = dial - 100 
            if dial < 0:
                while dial < 0:
                    dial = dial + 100
            
            # if the dial is 0, increase the code
            if dial == 0:
                code = code + 1

    print(f'Code: {code}')
    
get_code("input.txt")
