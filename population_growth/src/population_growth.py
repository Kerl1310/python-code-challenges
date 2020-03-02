import sys


def calculate_population_growth(
        starting_population,
        percentage_change,
        aug,
        population_to_surpass):
    '''
    Calculates the number of years required to surpass a given population size.
    '''
    number_of_years = 1
    percentage_change = percentage_change / 100

    while True:
        starting_population += int(starting_population * percentage_change)
        starting_population += int(aug)

        if starting_population >= population_to_surpass:
            return number_of_years
        number_of_years += 1


if len(sys.argv) > 4:
    print(
        str(calculate_population_growth(
            int(sys.argv[1]),
            float(sys.argv[2]),
            int(sys.argv[3]),
            int(sys.argv[4]))))
