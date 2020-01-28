# Daily Challenge - Pokemon Battle
Inspired by: https://dev.to/thepracticaldev/daily-challenge-170-pokemon-damage-calculator-97d

## Description
For this challenge, you'll be thrown into a Pokemon battle!
Calculate the damage that a particular move would do using the following formula:

`total damage = base damage * (attack / defense) * effectiveness`

`base damage` = the original power of the attack
`attack` = your attack stat
`defense` = the opponent's defense stat
`effectiveness` = the effectiveness of the attack based on the type matchup

Attacks can be super effective, neutral, or not very effective depending on the matchup.

`super effective` : 2x damage
`neutral` : 1x damage
`not very effective` : 0.5x damage

To prevent the challenge from being too tedious, you'll only deal with four types: fire, water, grass, and electric. Here are the matchups:

```
fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric
```

Any type against itself is not very effective.

Overall, the function you implement must take in...
* your type
* the opponent's type
* attack power
* the opponent's defense
... and must output the total damage of the attack.

## Test Cases:
"grass", "electric", 57, 19
"grass", "water", 40, 40
"grass", "fire", 35, 5
"fire", "electric", 10, 2