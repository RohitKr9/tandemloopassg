
# Tandem Loop Assignment Solutions

This repository contains solutions to four distinct programming problems, implemented in Python.

## Problems Solved

### Problem 1: Basic Calculator Class

A Python class for a calculator that performs addition, subtraction, multiplication, and division.
* **Inputs:** Two numbers (double) and a string for the operation ("add", "subtract", "multiply", "divide").
* **Output:** The result of the operation.

### Problem 2: Odd Number Series (Up to Nth Term)

Generates a series of odd numbers based on a single integer input `a`.
* **Input:** An integer `a`.
* **Output:** A comma-separated series of odd numbers (1, 3, 5, ..., up to `a` terms).
    * Example: `a = 4` -> `1, 3, 5, 7`

### Problem 3: Odd Number Series (Conditional Generation)

Generates a series of odd numbers based on a single integer input `a`, with a slight variation on Problem 2.
* **Input:** An integer `a`.
* **Output:** A comma-separated series of odd numbers. If `a` is even, it generates the series up to `a-1` terms; if `a` is odd, it generates up to `a` terms.
    * Example: `a = 4` -> `1, 3, 5` (only 3 terms)
    * Example: `a = 5` -> `1, 3, 5, 7, 9` (5 terms)

### Problem 4: Multiple Counter

Counts how many numbers in a given list are multiples of integers from 1 to 9.
* **Input:** A list of integers (e.g., `[1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]`).
* **Output:** A dictionary where keys are integers (1-9) and values are the counts of numbers in the input list that are multiples of that key.
    * Example Output: `{1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}`

## Technologies Used

* **Python**

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RohitKr9/tandemloopassg.git](https://github.com/RohitKr9/tandemloopassg.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd tandemloopassg/
    ```

## How to Run

Each problem likely has its own Python file (e.g., `problem1.py`, `problem2.py`, etc.). You can run them individually:

```bash
python3 problem1.py
python3 problem2.py
python3 problem3.py
python3 problem4.py
