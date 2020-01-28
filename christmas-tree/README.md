# Daily Challenge - Christmas Tree
Inspired by: https://dev.to/thepracticaldev/daily-challenge-169-christmas-tree-4dea

## Description
Create a function christmas_tree(height) that returns a Christmas tree of the correct height.

christmas_tree(5) should return:
     *
    ***
   *****
  *******
 *********
 
Height passed is always an integer between 0 and 100.
Use \n for newlines between each line.
Pad with spaces so each line is the same length. The last line having only stars, no spaces.

## Test Cases:
christmas_tree(5)
christmas_tree('five')
christmas_tree(-1)
christmas_tree(101)