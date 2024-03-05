from list_for_sort import list_digits


def selection_sort(sequence):

    for i in range(0, len(sequence) - 1):

        current_sequence = sequence[i+1:]
        min_digit = min(current_sequence)

        if sequence[i] > min_digit:
            min_index_digit = current_sequence.index(min_digit) + i + 1
            sequence[i],  sequence[min_index_digit] = sequence[min_index_digit], sequence[i]

    return sequence


print(f'selection_sort: {selection_sort(list_digits)}')
