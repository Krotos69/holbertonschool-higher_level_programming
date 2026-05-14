

---

# **Python – Test‑Driven Development**

```markdown
# Python – Test‑Driven Development (TDD)

## Project Description

### Project Purpose
This project introduces the principles and practical workflow of Test‑Driven Development (TDD) using Python. It is designed to help developers write cleaner, more reliable, and maintainable code by creating tests before implementing functionality.

### Problem Solved
Traditional development often leads to untested code, hidden bugs, and difficult refactoring. TDD solves these issues by ensuring that every feature is backed by automated tests, reducing regressions and improving long‑term code quality.

### General Context
TDD is a development methodology based on a short, repetitive cycle:
1. **Write a failing test**
2. **Write the minimal code to make the test pass**
3. **Refactor while keeping tests green**

This project demonstrates how to apply this cycle using Python’s testing tools such as `unittest`, `pytest`, and `doctest`.

### Definition and Commands
- **Unit Test**: A small, isolated test for a single function or behavior.
- **Doctest**: Tests embedded in docstrings.
- **Pytest**: A powerful testing framework for Python.
- **TDD Cycle**: Red → Green → Refactor.

Common commands:
```bash
python -m unittest
pytest -v
python -m doctest your_module.py -v
```

---

## Usage

### Command Examples
Run all tests:
```bash
pytest
```

Run a specific test file:
```bash
pytest tests/test_math.py
```

Run doctests:
```bash
python -m doctest -v module.py
```

### How to Implement
1. Write a test describing the expected behavior.
2. Run the test and confirm it fails.
3. Implement the minimal code required.
4. Run tests again until they pass.
5. Refactor the code while keeping tests green.

---

## Credits / Authors

**Author:**  
Eugenio Martínez
