# Debug Logger

A lightweight Python logging utility with colorful console output.  
Includes timestamped log levels (INFO, DEBUG, WARNING, ERROR, SUCCESS) for easy debugging in the terminal.

## Features
- Colored log levels (green, cyan, yellow, red, magenta)
- 12-hour timestamp format
- File and line number shown in readable format (e.g. `[in main.py at line 10]`)
- Simple static methods for each log type
- Test function to preview all colors

## Installation
Clone the repository:

```bash
git clone https://github.com/Bhargavxyz738/debug.git
````

And just import it using:

```python
from debug import Debug
```
OR

Just download it by runnning this on terminal `pip install debugger-log`
## Usage

```python
from debug import Debug

Debug.info("Program started")
Debug.debug("Loop iteration 1")
Debug.warn("This might be risky")
Debug.err("Something went wrong!")
Debug.succ("All good now")
```

### Output Example

```
[08:20:01 PM INFO]    [in test_debug.py at line 5] Program started
[08:20:01 PM DEBUG]   [in test_debug.py at line 6] Loop iteration 1
[08:20:01 PM WARNING] [in test_debug.py at line 7] This might be risky
[08:20:01 PM ERROR]   [in test_debug.py at line 8] Something went wrong!
[08:20:01 PM SUCCESS] [in test_debug.py at line 9] All good now
```

## Preview

![Preview](images/image.png)
