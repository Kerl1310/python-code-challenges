import sys
import random


def zombie_shootout(num_of_zombies, distance, num_of_bullets):
    '''
    Work out if you survive the zombie's assault
    '''
    zombie_speed = 0.5
    num_of_zombies_shot = 0
    probability_of_missing = 0.05
    num_of_zombies_remaining = num_of_zombies

    for bullet in range(num_of_bullets):
        if distance == 0:
            return "You shot {} zombie(s) before being eaten: overwhelmed.".format(
                num_of_zombies_shot)
        if num_of_zombies_remaining == 0:
            return "You shot all {} zombies.".format(
                num_of_zombies)

        distance -= zombie_speed
        shot_chance = random.randint(0, 100)

        if shot_chance >= probability_of_missing:
            num_of_zombies_shot += 1
            num_of_zombies_remaining -= 1
    return "You shot {} zombie(s) before being eaten: ran out of ammo.".format(
        num_of_zombies_shot)


if len(sys.argv) > 3:
    print(zombie_shootout(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
