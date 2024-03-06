from list_for_sort import list_digits
from insertion_sort import insertion_sort


def shell_sort(sequence):
    length = len(sequence)

    median = length // 2

    while median > 1:
        for i in range(0, length-median):
            if sequence[i] > sequence[median + i]:
                sequence[i], sequence[median + i] = sequence[median + i], sequence[i]
        median //= 2
    else:
        return insertion_sort(sequence)


if __name__ == '__main__':
    print(f'shell_sort: {shell_sort(list_digits)}')

