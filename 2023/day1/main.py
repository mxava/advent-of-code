from pathlib import Path

def solve(input:str)->str:
    output = str()
    for each in range(0, len(input)):
        if input[each].isdigit():
            output1 = input[each]
            break
    for each in reversed(range(0, len(input))):
        if input[each].isdigit():
            output2 = input[each]
            break
    output = str(output1) + str(output2)
    return output

number_as_string = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solve2(line):
    # Starts on the opposite side of destination
    left_index = len(line) - 1
    right_index = 0
    left_word = None
    right_word = None

    # First finds the indices of the left-most/right-most single character digits 
    for index, char in enumerate(line):
        if char.isdigit():
            if index > right_index:
                right_index = index
            if index < left_index:
                left_index = index

    # For each word, attempts to find the left-most and right-most index,
    # and if the index is lower/higher than our current left/right indices:
         # Set the new index
         # Store the word
    for word in number_as_string:
        word_left_index = line.find(word)
        word_right_index = line.rfind(word)
        if word_left_index != -1 and word_left_index < left_index:
                left_index = word_left_index
                left_word = word
        if word_right_index != -1 and word_right_index > right_index:
            right_index = word_right_index
            right_word = word

    # If `right_word` is not None, use that
    if right_word:
        right = number_as_string[right_word]
    # Otherwise, a single character digit was the right-most index
    else:
        right = line[right_index]

    # Same for left
    if left_word:
        left = number_as_string[left_word]
    else:
        left = line[left_index]
    return int(f'{left}{right}')


input = Path.cwd() / 'day1' / 'input.txt'
f = open(input, "r")

answer = int()

for each in f:
    line_output = solve2(each)
    print(f'Adding {line_output} to {answer}!')
    answer += line_output

print(answer)