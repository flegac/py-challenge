with open('bad_case.txt', 'w') as _:
    _.write(f'{50000}')
    for i in range(1, 50000):
        _.write(f'\n{i}')

    for i in [200001, 200002, 200003, 400005]:
        _.write(f'\n{i}')

with open('bad_case2.txt', 'w') as _:
    _.write(f'{50000}')
    for i in [1, 2, 3, 5]:
        _.write(f'\n{i}')

    for i in range(1, 50000):
        _.write(f'\n{10 + i}')
