# PR. 7 Moduler & Packager — Multi-Utility Toolkit

## Overview
**Moduler & Packager** is a Python-based Multi-Utility Toolkit that integrates multiple standard built-in modules (`datetime`, `time`, `math`, `random`, `uuid`, `importlib`) along with custom modules organized into a Python package (`custom_pkg`). The application features an interactive, menu-driven Command Line Interface (CLI) designed to perform daily utility operations, mathematical computations, random data generation, file management, and dynamic module inspection.

---

## Objectives
- **Explore Built-in Modules:** Utilize `datetime`, `time`, `math`, `random`, and `uuid` for practical tasks.
- **Custom Modules & Packages:** Build modular scripts (`file_ops.py` and `math_ops.py`) grouped inside a structured package with an `__init__.py` initializer.
- **Script Organization:** Use the `if __name__ == "__main__":` paradigm to separate reusable utility logic from main program execution.
- **Dynamic Exploration:** Use Python's built-in `dir()` and `importlib` to inspect attributes and methods of any built-in or custom module at runtime.

---

## Features & Functional Requirements

### 1. Datetime and Time Operations (`datetime`, `time`)
- Display current system date and time in a formatted view (`YYYY-MM-DD HH:MM:SS`).
- Calculate the exact difference in days between two user-provided dates.
- Format the current date into custom string representations using `strftime`.
- Interactive **Stopwatch** to measure elapsed time in seconds.
- **Countdown Timer** that counts down second-by-second in real time.

### 2. Mathematical Operations (`math` & `custom_pkg.math_ops`)
- Compute factorials of non-negative integers.
- Calculate **Compound Interest** given principal amount, interest rate, and time period.
- Perform trigonometric calculations (`sin`, `cos`, `tan`) by converting degrees to radians.
- Compute the area of geometric shapes (e.g., area of a circle).

### 3. Random Data Generation (`random`, `string`)
- Generate random integers within a custom lower and upper bound.
- Generate a random list of numbers of user-defined size.
- Create secure, randomized passwords combining letters, digits, and special symbols.
- Generate 6-digit numeric One-Time Passwords (OTPs).

### 4. Unique Identifier Generation (`uuid`)
- Generate universally unique identifiers using **UUID4** (`uuid.uuid4()`) for files, database records, invoices, or user sessions.

### 5. File Operations (`custom_pkg.file_ops`)
- **Create** a new empty file.
- **Write** text data to a file.
- **Read** and display existing contents from a file (with `FileNotFoundError` handling).
- **Append** additional lines of data to an existing file.

### 6. Dynamic Module Exploration (`dir()`, `importlib`)
- Dynamically load any Python module by name at runtime and list all its available attributes, functions, and classes using `dir()`.

---

## Project Directory Structure
```text
Moduler_And_Packager/
│
├── custom_pkg/
│   ├── __init__.py          # Initializes custom_pkg and exposes file_ops and math_ops
│   ├── file_ops.py          # Custom module for file creation, reading, writing, and appending
│   └── math_ops.py          # Custom module for factorial, compound interest, trigonometry, and area
│
├── main.py                  # Main entry point with menu-driven CLI
├── setup_and_run.py         # Optional helper script to auto-generate the package structure
└── README.md                # Project documentation and user guide
```

---

## Installation & How to Run

### Prerequisites
- Python 3.7 or higher installed on your system.

### Steps to Execute
1. **Clone the repository** (or download the project files):
   ```bash
   git clone <your-github-repo-url>
   cd Moduler_And_Packager
   ```
2. **Generate the package structure** (if using `setup_and_run.py`):
   ```bash
   python setup_and_run.py
   ```
3. **Run the main application**:
   ```bash
   python main.py
   ```

---

## User Guide & Sample Console Interaction

```text
===============================
Welcome to Multi-Utility Toolkit
===============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
===============================
Enter your choice: 1

Datetime and Time Operations:
1. Display current date and time
2. Calculate difference between two dates/times
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
Enter your choice: 1
Current Date and Time: 2025-01-04 10:15:30

Enter your choice: 2
Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days
```

### Example Outputs across Modules
- **Compound Interest:** Principal = `1000`, Rate = `5%`, Time = `2 years` → Output: `1102.50`
- **Random Password (Length 8):** `Kd8@qzP!`
- **Generated UUID:** `f47ac10b-58cc-4372-a567-0e02b2c3d479`
- **Module Exploration (`math`):** `['acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'ceil', 'comb', 'copysign', 'cos', ...]`

---

## Assumptions Made
1. **Date Input Format:** Users enter dates strictly in the `YYYY-MM-DD` format when calculating date differences.
2. **Compound Interest Formula:** Compound interest is compounded annually and outputs the total accumulated amount $A = P(1 + r/100)^t$ as demonstrated in the specification's sample interaction (`1102.50` for $P=1000, r=5\%, t=2$).
3. **Geometric Area Calculation:** Circle area ($\pi r^2$) is implemented as the default geometric calculation.
4. **File Paths:** File operations read and write files in the current working directory unless a relative or absolute path is specified by the user.
