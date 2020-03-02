# Daily Challenge - Blackjack
Inspired by: https://dev.to/thepracticaldev/daily-challenge-198-21-blackjack-31mg

## Description
Implement a function that determines the score of a hand in the card game Blackjack.

The function will receive an array filled with strings that represent each card in the hand. Your function should return the score of the hand as an integer.
Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.
Return the highest score of the cards that is less than or equal to 21. If there is no score less than or equal to 21 return the smallest score more than 21.

## Test Cases
* ["A"]
* ["5", "4", "3", "2", "A", "K"]
* ["A", "J"]
* ["A", "10", "A"]
* ["5", "3", "7"]
