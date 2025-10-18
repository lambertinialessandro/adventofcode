# Commands Manual

## Table of Contents

| Command | Parameters | Description |
| --- | --- | --- |
| `download_input.py` | `<year>` `<day>` | Downloads the input data for the specified year and day, and saves it to the corresponding folder. |
| `download_problem.py` | `<year>` `<day>` | Downloads the problem statement for the specified year and day, and writes it to the respective folder. |
| `create_solution.py` | `<year>` `<day>` | Creates two new solution files (`part1.py` and `part2.py`) in the corresponding year/day folder. |
| --- | --- | --- |
| `start_problem.py` | `<year>` `<day>` | Write the problem statement in the respective year/day folder. Create 2 new files for the solution. |

## Example

```
python ./commands/start_problem.py 2025 01
```

This command will:
1. Download the problem statement for Day 1 of 2025.
1. Create two solution files (part1.py and part2.py) inside the folder for that day.

