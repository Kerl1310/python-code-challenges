# Daily Challenge - Pandemia
Inspired by: https://dev.to/thepracticaldev/daily-challenge-173-pandemia-5ae7

## Description
The world has been hit with a new virus! There is a new pandemic that humanity is struggling to fight against. The continents are separated by oceans, but some infected people have traveled before the quarantine.

You'll be given a map of the world in the form of a string:
```
s = "01000000X000X011X0X"

"0" : uninfected
"1" : infected
"X" : ocean
```

* If one person gets infected on a continent, the entire continent will get infected.
* The first and last continents are not connected.
* The virus cannot spread across the ocean.
* For maps without X, there are no oceans so the entire planet would become infected, return 0%
* For maps without 0 or 1, there are no people, return 0.

Return the percentage of the population that are infected by the virus.

## Test Cases
* 01000000X000X011X0X
* 01X000X010X011XX
* XXXXX
* 00000000X00X0000
* 0000000010
* 000001XXXX0010X1X00010
* X00X000000X10X0100