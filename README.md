# Debug Logger

A lightweight Python logging utility with colorful console output.
Includes timestamped log levels (INFO, DEBUG, WARNING, ERROR, SUCCESS) for easy debugging in the terminal.

**Note:** This project was primarily created for **learning how to publish Python packages on PyPI** and experimenting with Python development workflows.

---

## Features

* Colored log levels (green, cyan, yellow, red, magenta)
* 12-hour timestamp format
* File and line number shown in readable format (e.g., `[in main.py at line 10]`)
* Simple static methods for each log type
* Test function to preview all colors
* **Visual hierarchy**: the log level is colored and the print statement is bright, while the rest of the message (timestamp, file info) is dimmed for easier scanning.

---

## Limitations

* Primarily **console-based**; limited support for file or remote logging
* No built-in **log rotation**—large logs can become unmanageable
* Not fully **production-ready**; better suited for **development and small scripts**
* Color/visual hierarchy may **not render properly on all terminals** or IDE consoles
* Custom log level (`SUCCESS`) is non-standard and may not integrate with logging frameworks or monitoring systems

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Bhargavxyz738/debug.git
```

Or install via pip:

```bash
pip install debugger-log
```

And import:

```python
from debug import Debug
```

---

## Usage

```python
from debug import Debug

Debug.info("Program started")
Debug.debug("Loop iteration 1")
Debug.warn("This might be risky")
Debug.err("Something went wrong!")
Debug.succ("All good now")
```

---

### Output Example

```
[08:20:01 PM INFO]    [in test_debug.py at line 5] Program started
[08:20:01 PM DEBUG]   [in test_debug.py at line 6] Loop iteration 1
[08:20:01 PM WARNING] [in test_debug.py at line 7] This might be risky
[08:20:01 PM ERROR]   [in test_debug.py at line 8] Something went wrong!
[08:20:01 PM SUCCESS] [in test_debug.py at line 9] All good now
```

---

## Preview

![Preview](images/image.png)

* Notice how the **log level stands out visually** while the rest of the message is dimmed, allowing you to focus on important events first.
