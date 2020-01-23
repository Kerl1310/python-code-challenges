import sys


def christmas_tree(height):
    '''
    Outputs a Christmas tree of the correct height.
    '''
    try:
        height = int(height)
    #except:
    #    raise TypeError('Height must be of type int. Actual type: {}'.format(type(height)))
    if height is None or height < 1 or height > 100:
        raise ValueError('Height must contain a value greater than 0')

    level = 0
    while level < height:
        stars = '*' * calculate_num_of_stars(level)
        stars = stars.center(height * 2)
        print(stars)
        level += 1


def calculate_num_of_stars(level):
    '''
    Calculates the correct number of stars that must be output.
    '''
    return 2 * (level + 1) - 1


if len(sys.argv) > 1:
    height = sys.argv[1]
    christmas_tree(height)
