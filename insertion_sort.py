from list_for_sort import list_digits


def insertion_sort(sequence):
    length = len(sequence)
    for i in range(1, length):
        # j = i-1
        # while j >= 0 and sequence[j] > sequence[i]:
        #     sequence[i], sequence[j] = sequence[j], sequence[i]
        #     j -= 1
        #     i -= 1

        for j in range(i, -1, -1):
            if sequence[j] > sequence[i]:
                sequence[i], sequence[j] = sequence[j], sequence[i]
                i -= 1

    return sequence


if __name__ == '__main__':
    print(f'insertion_sort: {insertion_sort(list_digits)}')
