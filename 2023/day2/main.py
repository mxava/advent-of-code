from pathlib import Path


#def solve1(input:dict, limitations:dict):
#    r_limit = limitations[red]
#    g_limit = limitations[green]
#    b_limit = limitations[blue]
#    total_r = int()
#    total_g = int()
#    total_b = int()
#    for each in list(input.values()):
#        parse = each.split(' ')
#        if parse[1] == 'red':
#            total_r += int(parse[0])
#        if parse[1] == 'green':
#            total_g += int(parse[0])
#        if parse[1] == 'blue':
#            total_b += int(parse[0])
#    if total_r > r_limit:
#        return 0
#    elif total_g > g_limit:
#        return 0
#    elif total_b > b_limit:
#        return 0
#    else:
#        return input
    


def solve1(input:str, limitations:dict) -> int:
    # Sanitize input of newlines
    input = input.strip('\n')
    # Track game number
    game = input.split(': ')[0]
    # Separate into list of rounds
    rounds = input.split(': ')[1].split('; ')
    # Check data from each round
    for each in rounds:
        # Split rounds into data about individual colors
        sample = each.split(', ')
        # Check number and color
        for each in sample:
            count = int(each.split(' ')[0])
            color = each.split(' ')[1]
            if count > limitations[color]:
                return 0
    return int(game.strip('[\'Game ]'))

def solve2(input:str) -> int:
    # Power cannot be 0
    min_r = 1
    min_g = 1
    min_b = 1
    # Sanitize input again
    input = input.strip('\n')
    # Separate into list of rounds
    rounds = input.split(': ')[1].split('; ')
    # Check data from each round
    for each in rounds:
        sample = each.split(', ')
        for each in sample:
            count = int(each.split(' ')[0])
            color = each.split(' ')[1]
            if count > min_r and color == 'red':
                min_r = count
            if count > min_g and color == 'green':
                min_g = count
            if count > min_b and color == 'blue':
                min_b = count
    return int(min_r * min_g * min_b) 
    

limitations = {
    'red': 12,
    'green': 13,
    'blue': 14
    }

input = Path.cwd() / '2023' / 'day2' / 'input.txt'
f = open(input, "r")

answer = int()

for each in f:
    line_output = solve2(each)
    print(f'Adding {line_output} to {answer}!')
    answer += line_output

print(f'The final answer is {answer}!')
