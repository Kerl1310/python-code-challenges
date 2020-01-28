import sys


def compare_attack_types(first_type, second_type):
    '''
    Compare the two types and return a multiplier.
    '''
    types = ["fire", "water", "electric", "grass"]
    if first_type not in types or second_type not in types:
        raise ValueError("Must be a valid type.")

    if first_type == "fire":
        if second_type == "grass":
            return 2
        if second_type == "water":
            return 0.5
    if first_type == "grass":
        if second_type == "fire":
            return 0.5
        if second_type == "water":
            return 2
    if first_type == "electric":
        if second_type == "water":
            return 2
    if first_type == "water":
        if second_type == "fire":
            return 2
        if second_type == "grass":
            return 0.5
    return 1


def calculate_damage(base_damage, own_type, opponent_type, attack, defense):
    '''
    Calculates the damage resulting from the attack.
    '''
    try:
        base_damage = int(base_damage)
        if base_damage < 1:
            raise ValueError("Base Damage must be greater than 0.")
    except TypeError:
        raise TypeError(
            "Base Damage must be of type int. Actual type: {}".format(type(base_damage)))

    try:
        attack = int(attack)
        if attack < 1:
            raise ValueError("Attack must be greater than 0")
    except TypeError:
        raise TypeError(
            "Attack must be of type int. Actual type: {}".format(type(attack)))

    try:
        defense = int(defense)
        if defense < 1:
            raise ValueError("Defense must be greater than 0")
    except TypeError:
        raise TypeError(
            "Defense must be of type int. Actual type: {}".format(type(defense)))

    effectiveness = compare_attack_types(own_type, opponent_type)
    return base_damage * (attack / defense) * effectiveness


if len(sys.argv) > 4:
    calculate_damage(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
        sys.argv[5])
