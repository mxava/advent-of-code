from pathlib import Path

# Sample data structure
###


data = []

def get_numbers_and_symbols(input: str) -> tuple:
    '''
    Outputs dict containing numbers
    and their corresponding indices
    '''
    numbers = {}
    number_indices = []
    symbol_indices = []
    num_index = None
    number = None
    for idx, char in enumerate(input):
        # Checks individual digits
        if char.isdigit():
            number_indices.append(idx)
            if num_index = None:
                num_index = idx
            number = str(number) + char
        # Clears num_index once char is no longer a number
        if (not char.isdigit()) and (number != None):
            numbers.append({
                num_index: number
            })
            number = None
            num_index = None
        # Get indices of symbols
        if (not char.isdigit()) and (char != '.'):
            symbol_indices.append([idx])
        return numbers, number_indices, symbol_indices

    

def structure_data(index: int, line_contents: str) -> dict:
    '''
    Creates a dict object containing:
    -the line number
    -the line as a string
    -any occurring numbers
    -their indices
    '''
    numbers_and_symbols = get_numbers_and_symbols(line) 
    entry = {
                'line_idx': index,
                'line_contents': line_contents,
                'numbers':  numbers_and_symbols[0],
                'number_indices': numbers_and_symbols[1],
                'symbol_indices':  numbers_and_symbols[2]
            }
    return entry    

def check_symbols(dict_entry:dict) -> int:
        # Check line above
        if input['line_idx'] > 0:
            # Is symbol adjacent to a number index?
            # If so, which number is near the symbol?



if __name__ == '__main__':
    input = Path.cwd() / '2023' / 'day3' / 'input.txt'
    f = open(input, "r")

    for idx, line_contents in enumerate(f):
        data.append(structure_data(idx, line_contents))
