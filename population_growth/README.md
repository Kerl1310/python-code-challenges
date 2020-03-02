# Daily Challenge - Population Growth
Inspired by: https://dev.to/thepracticaldev/daily-challenge-197-population-growth-e4p

## Description
Implement a function to calculate the growth of a population of people. The function should be able to take several parameters, including `p0` (starting population), `percent`, `aug` (inhabitants coming or leaving each year), and `p` (population to surpass). This function should output `n` (number of years needed to get a population of `p`).

Don't forget to convert the `percent` parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.

## Test Cases
* calculate_population_growth(1000, 2, 50, 1200)
* calculate_population_growth(1500, 5, 100, 5000)
* calculate_population_growth(1500000, 2.5, 10000, 2000000)
* calculate_population_growth(1500000, 0.25, 1000, 2000000)
