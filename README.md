# Smart Travel Planner Using Python

## Program Understanding

Smart Travel Planner is a beginner-friendly Python console program. It collects
basic travel details, calculates the estimated cost of a trip, and prints a
formatted travel summary.

Run it from this folder with:

```text
python smart_travel_planner.py
```

## Information Collected

- Traveler name
- Destination
- Number of travelers
- Number of travel days
- Transportation cost per traveler
- Hotel cost per day
- Activity cost per traveler

## Calculations

The program uses a separate function for each major calculation:

- Total transportation cost = travelers x transportation cost per traveler
- Total hotel cost = travel days x hotel cost per day
- Total hotel food cost = travelers x travel days x $25
- Total activity cost = travelers x activity cost per traveler
- Overall trip cost = transportation + hotel + hotel food + activities
- Cost per traveler = overall trip cost / number of travelers
- Average daily cost = overall trip cost / travel days

The hotel food estimate uses a fixed assumption of `$25 per traveler per day`
because no food-cost input was requested.

## Python Concepts Demonstrated

- Variables and appropriate data types: strings, integers, and floating-point numbers
- `input()` and type conversion with `int()` and `float()`
- Dictionaries for organizing travel information and calculated costs
- Functions with parameters and return values
- Arithmetic operations
- Input validation using loops and `try`/`except`
- Formatted output using f-strings

The program uses only Python's built-in features. It does not use a database,
files, APIs, external libraries, or classes.

## Validation Rules

- Number of travelers must be greater than zero.
- Number of travel days must be greater than zero.
- Costs cannot be negative.
- Traveler name and destination cannot be empty.