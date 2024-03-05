import random

list_digits = [random.randint(1, 100) for _ in range(10)]

print(f'Len: {len(list_digits)}')
print('List: ', *list_digits)
