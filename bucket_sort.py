from list_for_sort import list_digits
from quick_sort import quick_sort


def bucket_sort(sequence):
    length = len(sequence)

    buckets = [[] for _ in range(length + 1)]

    for i in range(length):
        elem = sequence[i] // 10
        if elem < length:
            buckets[elem].append(sequence[i])
        else:
            buckets[-1].append(sequence[i])

    result = list()

    for bucket in buckets:
        if len(bucket) > 1:
            result += quick_sort(bucket)
        else:
            result += bucket

    return result


if __name__ == '__main__':
    print(f'bucket_sort: {bucket_sort(list_digits)}')
