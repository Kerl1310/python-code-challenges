# Daily Challenge - Find All
Inspired by: https://dev.to/thepracticaldev/daily-challenge-172-find-all-in-an-array-3nob

## Description
Implement a function that will accept an array and a value n. Find all occurrences of n in the given array and return another array containing all the index positions of n in the array.

If n is not in the given array, return an empty array [].

## Test Cases
find_all([6, 9, 3, 4, 3, 82, 11], 2)
find_all([6, 9, 3, 4, 3, 82, 11], 3)
find_all([10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16)
find_all([20, 20, 10, 13, 15, 2, 7, 2, 20, 3,
                18, 2, 3, 2, 16, 10, 9, 9, 7, 5, 15, 5], 20)
find_all(["happy", "birthday", "to", "you",
                "happy", "birthday", "to", "me"], "happy")