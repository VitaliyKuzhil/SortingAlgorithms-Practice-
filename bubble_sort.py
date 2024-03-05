from list_for_sort import list_digits


def bubble_sort(sequence):

    length_list = len(sequence)

    for i in range(length_list):
        for j in range(1, length_list - i):
            if sequence[j-1] > sequence[j]:
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]

    return sequence


if __name__ == '__main__':
    print(f'bubble_sort: ', bubble_sort(list_digits))
