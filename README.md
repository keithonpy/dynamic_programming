# Dynamic Programming

## Memoization

**Brute-force**

1. Visualise the problem as tree
2. implement the tree using recursion (brute force solution)
3. test it
   
**Make it more efficient**

4. Add a memo object
5. add a base case to return memo values
6. Store return values into the memo

## Tabulation

1. Visualise the problem as a table
2. Size the table based on the inputs#
3. Initialize the table with default values (eg. [0] * (length+1) at fibonacci)
4. Seed the trivial answer into the table (eg. dp[1] = 1 at fibonacci)
5. Iterate throught the table
6. Fill further positions based on the current position