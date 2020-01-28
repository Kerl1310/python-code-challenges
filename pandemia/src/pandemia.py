OCEAN = 'X'
INFECTED = '1'

def calculate_percentage_infected(map_in):
    '''
    Calculate the Percentage of the Population that will be Infected.
    '''
    total_infected = 0
    total = 0
    print("Starting Map: {}".format(map_in))
    for continent in map_in.split(OCEAN):
        total += len(continent)
        if INFECTED in continent:
            result = INFECTED * len(continent)
            total_infected += len(continent)

    if total_infected > 0 and total > 0:
        print("TOTAL_INFECTED: {}".format(total_infected))
        print("TOTAL: {}".format(total))
        infected_percentage = (total_infected / total) * 100
        return infected_percentage
    return 0


print("INFECTED PERCENTAGE: {}%".format(calculate_percentage_infected("01000000X000X011X0X")))
print("INFECTED PERCENTAGE: {}%".format(calculate_percentage_infected("01X000X010X011XX")))
print("INFECTED PERCENTAGE: {}%".format(calculate_percentage_infected("XXXXX")))
print("INFECTED PERCENTAGE: {}%".format(calculate_percentage_infected("00000000X00X0000")))
print("INFECTED PERCENTAGE: {}%".format(calculate_percentage_infected("0000000010")))
print("INFECTED PERCENTAGE: {}%".format(calculate_percentage_infected("000001XXXX0010X1X00010")))
print("INFECTED PERCENTAGE: {}%".format(calculate_percentage_infected("X00X000000X10X0100")))
