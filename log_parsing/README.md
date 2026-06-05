# Log Parsing

A Python script that reads stdin line by line and computes metrics.

## Usage

```bash
./0-generator.py | ./0-stats.py
```

## Description

- Reads stdin line by line
- Computes total file size
- Counts occurrences of each status code
- Prints stats every 10 lines and on keyboard interruption (CTRL+C)