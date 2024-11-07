def median(z):

    rendezett = sorted(z)

    n = len(rendezett)

    middle = n // 2

    if n % 2 == 1:
        return rendezett[middle]

    else:

        return (rendezett[middle - 1] + rendezett[middle]) / 2


print(median([1, 2, 3, 4, 5]))
print(median([3, 1, 2, 5, 3]))  #
print(median([1, 300, 2, 200, 1]))
print(median([3, 6, 20, 99, 10, 15]))
