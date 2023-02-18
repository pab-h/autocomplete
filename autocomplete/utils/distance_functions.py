from typing import Callable

distance_function = Callable[[str, str], int]

def hamming(x: str, y: str) -> int:
    x_length = len(x)
    y_length = len(y)

    if x_length > y_length:
        y = y.ljust(x_length)
    
    if x_length < y_length:
        x = x.ljust(y_length)

    difference = 0

    for i in range(x_length):
        if x[i] != y[i]:
            difference += 1

    return difference

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
def levenshtein(source: str, target: str) -> int:
    if len(source) < len(target):
        return levenshtein(target, source)

    # len(source) >= len(target)
    if len(target) == 0:
        return len(source)

    previous_row = range(len(target) + 1)
    for i, c1 in enumerate(source):
        current_row = [i + 1]
        for j, c2 in enumerate(target):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than target
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]
