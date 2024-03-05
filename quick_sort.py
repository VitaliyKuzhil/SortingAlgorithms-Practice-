from list_for_sort import list_digits


def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    pivot = sequence[len(sequence)//2]

    array_left = [elem for elem in sequence if elem < pivot]
    array_right = [elem for elem in sequence if elem > pivot]

    return quick_sort(array_left) + [pivot] + quick_sort(array_right)


if __name__ == '__main__':
    print(f'quick_sort: {quick_sort(list_digits)}')
