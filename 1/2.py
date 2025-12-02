import math

def get_code(file_name: str):
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

            # if it looped, get the number of times 
            if dial > 99 or dial < 0:
                divisor = abs(dial // 100) # 201 we will increase by 2
                code = code + divisor 

            # update the dial to a range within 100
            dial = math.remainder(dial, 100)

            if dial < 0: # if dial went negative, loop it back around
                dial = dial + 100

    print(f'Code: {code}')
    
get_code("input.txt")
