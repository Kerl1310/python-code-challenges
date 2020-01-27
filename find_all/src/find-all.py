import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "list",  # name on the CLI - add `--` for optional parameters
    nargs="+",  # 0 or more values expected => creates a list
    default=[],  # default if nothing is provided
    help='list to be searched'
)
parser.add_argument(
    "value",
    help='value we are searching for'
)


def find_all(list_in, value):
    '''
    Find and Return All Instances of a Value in a List.
    '''
    position = 0
    results = []
    for element in list_in:
        try:
            element = int(element)
        except:
            pass
        if element == value:
            results.append(position)
        position += 1
    return results


args = parser.parse_args()
list_in = args.list
value_in = args.value

try:
    value_in = int(args.value)
except:
    pass
