import os

TEST = False

def process(f):
    array = []
    with open(f, "r") as file:
        for line in file:
            array.append(line.split("\n")[0])
    return array

if __name__ == '__main__':
    if TEST:
        input_file = 'puzzle-1/{}_test_input.txt'.format(os.path.basename(__file__).split(".")[0])
    else:
        input_file = 'puzzle-1/{}_input.txt'.format(os.path.basename(__file__).split(".")[0])
    lines = process(input_file)

    cost = 0

    for line in lines:
        rm_line = line
        num_char = len(rm_line)
        num_byte = len(rm_line.encode('utf-8'))

        print(num_char, num_byte)

        if num_byte <= 160:  # yes SMS
            if num_char <= 140:  # yes SMS yes TWEET, 13
                cost += 13
            else:  # yes SMS no TWEET, 11
                cost += 11
        else:  # no SMS
            if num_char <= 140:  # no SMS yes TWEET, 7
                cost += 7
            else:  # no SMS no TWEET, 0
                cost += 0
        print(cost)

    print("Total cost is: {}".format(cost))