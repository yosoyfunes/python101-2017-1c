result = reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(result)

result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# calcula: ((((1+2)+3)+4)+5).
print(result)


# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         try:
#             initializer = next(it)
#         except StopIteration:
#             raise TypeError('reduce() of empty sequence with no initial value')
#     accum_value = initializer
#     for x in it:
#         accum_value = function(accum_value, x)
#     return accum_value
