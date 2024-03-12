from list_for_sort import list_digits


def heap_sort(sequence):
    build_max_heap(sequence)

    for last_index in range(len(sequence) - 1, -1, -1):
        swap(sequence, 0, last_index)
        heapify(sequence, 0, last_index - 1)
    return sequence


def build_max_heap(sequence):
    length = len(sequence)
    last_heap_index = (length - 2) // 2

    for current_index in range(last_heap_index, -1, -1):
        heapify(sequence, current_index, length)


def heapify(sequence, current_index, last_index):
    left_child = 2 * current_index + 1

    while left_child <= last_index:

        right_child = 2 * current_index + 2
        if right_child >= last_index:
            right_child = -1

        largest_child = left_child
        if right_child != -1 and sequence[left_child] < sequence[right_child]:
            largest_child = right_child

        if sequence[current_index] < sequence[largest_child]:
            swap(sequence, current_index, largest_child)

            current_index = largest_child
            left_child = 2 * current_index + 1
        else:
            return


def swap(sequence, i, j):
    sequence[i], sequence[j] = sequence[j], sequence[i]


if __name__ == '__main__':
    print(f'shell_sort: {heap_sort(list_digits)}')
