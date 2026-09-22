def checker(x, y):
    return(
        True if y in [2, 1, 0, -1, -2] and
                x in [-2, -1, 0, 1, 2] and
                str(x) + str(y) not in ['-2-2', '-1-1', '-22', '2-2'] else False
    )

print(checker(
    int(input('x: ')), 
    int(input('y: '))
))