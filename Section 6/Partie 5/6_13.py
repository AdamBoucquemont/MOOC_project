def next_line(line):
    new_line = []
    if line == []:
        new_line = [1]
    else:
        i = 0
        while i < len(line):
            same_number = 1
            while i + same_number < len(line) and line[i] == line[i + same_number]:
                same_number += 1
            new_line.append(same_number)
            new_line.append(line[i])
            i += same_number
    return new_line

print(next_line([1, 2, 1, 1]))