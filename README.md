<div align="center">

#  Python Basics — 25BCON1800

### A structured collection of Python programs, problem-solving exercises, and beginner-to-intermediate programming concepts.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Learning%20Project-2ea44f?style=for-the-badge)](#-project-overview)
[![Repository](https://img.shields.io/badge/GitHub-python--basics--25bcon1800-181717?style=for-the-badge&logo=github)](https://github.com/bhakharhimanshu-svg/python-basics-25bcon1800)

**Author:** [@bhakharhimanshu-svg](https://github.com/bhakharhimanshu-svg)

</div>

---

##  Project Overview

**Python Basics** is an educational repository focused on building a strong foundation in Python programming through small, practical programs. Each script demonstrates a specific concept and can be run independently.

The repository is suitable for learners who want to practise core syntax, logic building, collections, loops, functions, and input validation.

> **Learning approach:** Understand the logic → Run the program → Test edge cases → Improve the implementation.

##  Objectives

- Strengthen Python fundamentals through hands-on coding.
- Practise problem-solving with reusable functions.
- Learn to validate user input and handle common errors.
- Build a clean, readable GitHub project that can grow over time.
- Create a foundation for larger Python, automation, and data-oriented projects.

##  Repository Structure

```text
python-basics-25bcon1800/
├── dictionary.py       # Dictionary-based student management program
├── factorial.py        # Factorial calculator
├── fibonacci.py        # Fibonacci sequence generator
├── list_program.py     # Interactive list operations
├── multiplication.py   # Custom multiplication table generator
└── README.md           # Project documentation
```

> **Filename tip:** `list_program.py` is recommended instead of `list.py`. A file named `list.py` can shadow Python's built-in `list` type and cause confusing import errors.

##  Programs & Features

### 1. `dictionary.py` — Student Management System
- Add a student using a roll number, name, and marks.
- Search for a student by roll number.
- Update marks and display student records.
- Reject duplicate roll numbers and marks outside the 0–100 range.
- **Current limitation:** Records are stored in memory and are cleared when the program exits.

### 2. `factorial.py` — Factorial Calculator
- Calculates factorials of non-negative integers.
- Uses Python's `math.factorial()` for reliable integer calculation.
- Displays the number of digits in the result.
- Handles invalid input and applies a practical input limit.

### 3. `fibonacci.py` — Fibonacci Generator
- Generates a requested number of Fibonacci terms.
- Uses an iterative approach rather than recursion.
- Supports a configurable number of terms and validates the input.

### 4. `list_program.py` — Interactive List Manager
- Add and remove items.
- Search for an item and show its index.
- Sort items and display the current list.
- Uses a menu-driven interface.

### 5. `multiplication.py` — Multiplication Table Generator
- Creates a multiplication table for a chosen number.
- Lets the user select the starting and ending multipliers.
- Supports ascending and descending output.
- Validates the selected range.

##  Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| Python standard library | Built-in utilities; no third-party packages required |
| Git & GitHub | Version control and project hosting |
| Markdown | Project documentation |

##  Prerequisites

- Python 3.8 or newer installed
- A terminal or command prompt
- Git, if you want to clone the repository

Check your Python installation:

```bash
python --version
```

If your system uses the `python3` command:

```bash
python3 --version
```

##  Installation & Setup

### Option 1: Clone with Git

```bash
git clone https://github.com/bhakharhimanshu-svg/python-basics-25bcon1800.git
cd python-basics-25bcon1800
```

### Option 2: Download ZIP

1. Open the repository on GitHub.
2. Select **Code → Download ZIP**.
3. Extract the ZIP file.
4. Open a terminal inside the extracted folder.

##  Run the Programs

Run each script independently:

```bash
python dictionary.py
python factorial.py
python fibonacci.py
python list_program.py
python multiplication.py
```

On systems where Python is invoked with `python3`, replace `python` with `python3`.

##  Example Output

### Fibonacci Generator

```text
Enter number of terms (0-10000): 7
Fibonacci Sequence:
0, 1, 1, 2, 3, 5, 8
```

### Multiplication Table

```text
Enter number: 5
Starting multiplier: 1
Ending multiplier: 5
Reverse order? (yes/no): no

Multiplication Table of 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
```

*Example output may vary slightly depending on the version of each script in your repository.*

##  Concepts Demonstrated

- Variables, data types, and operators
- Dictionaries and lists
- Conditional statements and loops
- Functions and modular programming
- Input validation and exception handling
- Iterative algorithms
- Menu-driven command-line programs
- Basic code organisation and readability

##  Development Roadmap

The following are planned improvements, not features currently guaranteed by the scripts:

- [ ] Persist student records using JSON or SQLite.
- [ ] Add automated tests using `unittest` or `pytest`.
- [ ] Add logging and more consistent error handling.
- [ ] Split larger programs into reusable modules.
- [ ] Add a Tkinter graphical user interface.
- [ ] Add type hints and docstrings.
- [ ] Set up a GitHub Actions workflow to run tests automatically.
- [ ] Add screenshots or short demos for interactive programs.

##  Contributing

This is a learning project. To suggest an improvement:

1. Fork the repository.
2. Create a branch for your change.
3. Make your changes and test the script.
4. Open a pull request with a clear description.

For personal practice, you can also create a new `.py` file for each exercise and document its purpose here.

##  Reliability & Limitations

- These programs are educational examples, not production software.
- Test scripts with normal inputs, boundary values, and invalid inputs.
- Student records are not saved between runs unless persistent storage is added.
- The README describes the intended scripts; ensure the filenames match the actual files uploaded to GitHub.

##  Author

**Himanshu Bhakhar**  
GitHub: [@bhakharhimanshu-svg](https://github.com/bhakharhimanshu-svg)

##  License

No license has been specified yet. If you want others to reuse, modify, or distribute this project, consider adding a license file.

---

<div align="center">

**Built with Python • Documented with Markdown • Improved through practice**

 If this repository helps you learn, consider starring it on GitHub.

</div>
#  Advanced Python Programs

A collection of Python programs designed to practice programming fundamentals, problem-solving, functions, data structures, and basic software development concepts.

##  Author

**Himanshu Bhakhar**

- GitHub: [@bhakharhimanshu-svg](https://github.com/bhakharhimanshu-svg)
- Repository: [python-basics-25bcon1800](https://github.com/bhakharhimanshu-svg/python-basics-25bcon1800)

##  Project Overview

This project contains Python programs with input validation, reusable functions, error handling, and practical features. It is designed for students who want to improve their Python programming skills and maintain their work on GitHub.

##  Features

- Factorial calculator with iterative and recursive approaches
- Fibonacci sequence generator and analyzer
- Student management system with search and grade calculation
- Even and odd number checker
- Multiplication table generator
- Prime number checker
- CSV export for student records
- Input validation and error handling
- Clear program structure and documentation

##  Project Structure

```text
python-basics-25bcon1800/
│
├── factorial.py
├── fibonacci.py
├── student_record.py
├── even_odd.py
├── multiplication_table.py
├── prime_checker.py
├── README.md
├── AUDIT.md
└── .gitignore
```

##  Technologies Used

- **Language:** Python
- **Concepts:** Functions, loops, conditionals, classes, dictionaries, recursion, exception handling
- **Data Export:** CSV
- **Version Control:** Git and GitHub

##  Requirements

- Python 3.10 or later recommended
- No third-party packages are required for the listed programs.

Check your Python installation:

```bash
python --version
```

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/bhakharhimanshu-svg/python-basics-25bcon1800.git
```

2. Open the project folder:

```bash
cd python-basics-25bcon1800
```

3. Run any program:

```bash
python factorial.py
```

Other examples:

```bash
python fibonacci.py
python student_record.py
python even_odd.py
python multiplication_table.py
python prime_checker.py
```

If your computer uses `python3`, replace `python` with `python3`.

##  Program Details

| Program | Description |
|---|---|
| `factorial.py` | Calculates factorials and compares calculation methods. |
| `fibonacci.py` | Generates Fibonacci terms and displays sequence statistics. |
| `student_record.py` | Manages student records, calculates grades, searches records, and exports CSV data. |
| `even_odd.py` | Determines whether a number is even or odd. |
| `multiplication_table.py` | Generates multiplication tables. |
| `prime_checker.py` | Checks whether a number is prime. |

##  Example Output

For `factorial.py`, entering `5` produces:

```text
Number             : 5
Factorial          : 120
Number of digits   : 3
Built-in verified  : True
```

##  Learning Objectives

- Understand Python functions and modular programming.
- Practice loops, conditionals, and recursion.
- Work with lists, dictionaries, and classes.
- Handle invalid user input.
- Organize code into separate files.
- Learn GitHub repositories and meaningful commit messages.

##  Documentation and Quality Checks

The `AUDIT.md` file is intended to document README claim verification, commit-message comparisons, and peer-review notes. Claims should be marked verified only after checking the actual code and running the relevant tests.

##  Future Improvements

- Add automated unit tests.
- Save and load student records automatically.
- Add a graphical user interface.
- Improve reporting and data analysis.
- Set up continuous integration with GitHub Actions.

##  License

No license has been added yet. Reuse and redistribution permissions should not be assumed unless a suitable license is added.

---

**Developed by Himanshu Bhakhar**  
*Learning Python, building projects, and improving one commit at a time.*
