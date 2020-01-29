OCEAN = 'X'
INFECTED = '1'


def calculate_percentage_infected(map_in):
    '''
    Calculate the Percentage of the Population that will be Infected.
    '''
    total_infected = 0
    total = 0
    for continent in map_in.split(OCEAN):
        total += len(continent)
        if INFECTED in continent:
            result = INFECTED * len(continent)
            total_infected += len(continent)

    if total == 0:
        return total
    return (total_infected / total) * 100


print("INFECTED PERCENTAGE: {}%".format(
    calculate_percentage_infected("01000000X000X011X0X")))
print("INFECTED PERCENTAGE: {}%".format(
    calculate_percentage_infected("01X000X010X011XX")))
print("INFECTED PERCENTAGE: {}%".format(
    calculate_percentage_infected("XXXXX")))
print("INFECTED PERCENTAGE: {}%".format(
    calculate_percentage_infected("00000000X00X0000")))
print("INFECTED PERCENTAGE: {}%".format(
    calculate_percentage_infected("0000000010")))
print("INFECTED PERCENTAGE: {}%".format(
    calculate_percentage_infected("000001XXXX0010X1X00010")))
print("INFECTED PERCENTAGE: {}%".format(
    calculate_percentage_infected("X00X000000X10X0100")))
