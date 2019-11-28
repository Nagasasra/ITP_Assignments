def histogram(lst):
    for numbers_stars in lst:
        iteration = 0
        while iteration < numbers_stars:
            print('*', end='')
            iteration = iteration + 1
        print()
list = [4,9,7]
histogram(list)