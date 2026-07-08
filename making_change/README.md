# Making Change

## About
This project solves the classic "coin change" problem: given a list of coin denominations and a target total, determine the fewest number of coins needed to reach that total using dynamic programming.

## Tasks

### 0. Change comes from within
File: `0-making_change.py`

Determines the fewest number of coins needed to meet a given amount.

- Returns `0` if `total` is `0` or less
- Returns `-1` if the `total` cannot be met with the given coins
- Uses a dynamic programming approach for efficiency