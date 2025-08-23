# 📘 Python Data Types

| Category        | Data Type    | Description                          | Example Code |
|-----------------|--------------|--------------------------------------|--------------|
| **Numeric**     | `int`        | Whole numbers                        | `x = 10` |
|                 | `float`      | Decimal numbers                      | `y = 10.5` |
|                 | `complex`    | Real + imaginary part                | `z = 3 + 4j` |
| **Text**        | `str`        | String (sequence of characters)      | `name = "Nikhil"` |
| **Sequence**    | `list`       | Ordered, mutable collection          | `fruits = ["apple", "banana"]` |
|                 | `tuple`      | Ordered, immutable collection        | `coords = (10, 20)` |
|                 | `range`      | Sequence of numbers                  | `nums = range(5)` → `[0,1,2,3,4]` |
| **Mapping**     | `dict`       | Key-value pairs                      | `student = {"name": "Nikhil", "age": 21}` |
| **Set Types**   | `set`        | Unordered, unique items              | `colors = {"red", "green"}` |
|                 | `frozenset`  | Immutable set                        | `fs = frozenset([1,2,3])` |
| **Boolean**     | `bool`       | Logical values `True` / `False`      | `is_active = True` |
| **Binary**      | `bytes`      | Immutable byte sequence              | `b = b"hello"` |
|                 | `bytearray`  | Mutable byte sequence                | `ba = bytearray(5)` |
|                 | `memoryview` | View of memory of another object     | `mv = memoryview(b"abc")` |
| **Special**     | `NoneType`   | Represents “no value”                | `data = None` |

---
✅ **Note**: Everything in Python is an **object**, even numbers and functions.

name = "Nikhil"
varaible does not have to be declared with any specific type, and can even change type after it has been set.
memory has reference to the object and its types, not the value
mutable and immutable:
mutable: list, dict, set
immutable: tuple, string, int, float, bool, complex
mutable objects can be changed after they are created, immutable objects cannot be changed after they are created.






