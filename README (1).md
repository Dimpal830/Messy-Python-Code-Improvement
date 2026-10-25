# Messy Python Code Improvement

A before-and-after refactoring exercise. `messy_code.py` is a working but hard-to-read script. `improved_code.py` does the same job with clean, reusable code. Both calculate each student's total, average and grade, the class average, and the topper.

## What was improved

| Problem in the messy version | Fix in the improved version |
|---|---|
| Names like `a`, `i`, `t`, `p`, `g` | Clear names: `students`, `average`, `grade` |
| Student data stored as nested lists (`i[1]`, `i[2]`) | A `Student` dataclass with named fields |
| Everything in one long script | Small functions that each do one job |
| Average calculated twice in two loops | `average` calculated once, in one place |
| Long `if / elif` chain with hardcoded numbers | `GRADE_BOUNDARIES` constant and a `get_grade()` function |
| Manual loop to find the top scorer | Built-in `max()` with a `key` |
| Messy print output | f-string formatting with aligned columns |
| No comments or documentation | Docstrings explaining each function |
| Code runs when imported | `if __name__ == "__main__":` guard |

## How to run

```bash
python messy_code.py
python improved_code.py
```

## Technologies
Python, refactoring, clean code practices
