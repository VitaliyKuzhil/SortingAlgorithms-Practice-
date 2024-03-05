from list_for_sort import list_digits


def marge_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    index = sequence.index(sequence[len(sequence)//2])

    left_digits = sequence[:index]
    right_digits = sequence[index:]

    left = marge_sort(left_digits)
    right = marge_sort(right_digits)

    return marge(left + right)


def marge(sequence):
    result = list()

    while len(sequence) > 0:
        min_element = min(sequence)
        index_min_element = sequence.index(min_element)

        result.append(min_element)
        sequence = sequence[:index_min_element] + sequence[index_min_element+1:]

    return result


if __name__ == '__main__':
    print(f'marge_sort: {marge_sort(list_digits)}')
