# Mutable vs Immutable Types in Python

## Overview
In Python, objects are classified as either **mutable** (can be changed after creation) or **immutable** (cannot be changed after creation).

## Immutable Types

Immutable types cannot be modified after they are created. Any operation that appears to modify them actually creates a new object.

### Examples of Immutable Types:

1. **int** - Integers
2. **float** - Floating point numbers
3. **str** - Strings
4. **tuple** - Tuples
5. **bool** - Booleans
6. **frozenset** - Frozen sets
7. **bytes** - Byte sequences

### Example with Strings (Immutable):
```python
# Strings are immutable
text = "Hello"
print(id(text))  # Memory address of 'text'

text = text + " World"  # Creates a NEW string object
print(id(text))  # Different memory address!

# This won't work:
# text[0] = "h"  # TypeError: 'str' object does not support item assignment
```

### Example with Tuples (Immutable):
```python
# Tuples are immutable
my_tuple = (1, 2, 3)
print(id(my_tuple))

# This creates a new tuple
my_tuple = my_tuple + (4,)  # Note: comma makes it a tuple
print(id(my_tuple))  # Different address

# This won't work:
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

## Mutable Types

Mutable types can be modified after creation. Changes are made to the same object in memory.

### Examples of Mutable Types:

1. **list** - Lists
2. **dict** - Dictionaries
3. **set** - Sets
4. **bytearray** - Mutable byte sequences
5. **Custom classes** - User-defined classes (by default)

### Example with Lists (Mutable):
```python
# Lists are mutable
my_list = [1, 2, 3]
print(id(my_list))  # Memory address

my_list.append(4)  # Modifies the same object
print(my_list)     # [1, 2, 3, 4]
print(id(my_list)) # Same memory address!

my_list[0] = 10    # Can modify elements
print(my_list)     # [10, 2, 3, 4]
```

### Example with Dictionaries (Mutable):
```python
# Dictionaries are mutable
my_dict = {"name": "Alice", "age": 30}
print(id(my_dict))

my_dict["city"] = "New York"  # Modifies the same object
print(my_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(id(my_dict))  # Same memory address
```

### Example with Sets (Mutable):
```python
# Sets are mutable
my_set = {1, 2, 3}
print(id(my_set))

my_set.add(4)  # Modifies the same object
print(my_set)  # {1, 2, 3, 4}
print(id(my_set))  # Same memory address
```

## Important Implications

### 1. Variable Assignment
```python
# Immutable: Creates new object
x = 5
y = x
y = 10
print(x)  # 5 (unchanged)
print(y)  # 10

# Mutable: Both reference same object
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] (changed!)
print(b)  # [1, 2, 3, 4]
print(a is b)  # True (same object)
```

### 2. Function Arguments
```python
# Immutable: Changes don't affect original
def modify_string(s):
    s = s + " modified"
    return s

text = "Hello"
modify_string(text)
print(text)  # "Hello" (unchanged)

# Mutable: Changes affect original
def modify_list(lst):
    lst.append(4)
    return lst

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] (changed!)
```

### 3. Default Arguments (Common Pitfall!)
```python
# BAD: Using mutable default arguments
def add_item(item, my_list=[]):  # ⚠️ Dangerous!
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - unexpected!
print(add_item(3))  # [1, 2, 3] - keeps growing!

# GOOD: Use None as default
def add_item_safe(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item_safe(1))  # [1]
print(add_item_safe(2))  # [2] - correct!
```

### 4. Copying Objects
```python
# Shallow copy (mutable types)
original = [1, 2, [3, 4]]
shallow_copy = original.copy()  # or list(original) or original[:]

shallow_copy.append(5)
print(original)      # [1, 2, [3, 4]] - not affected
print(shallow_copy)  # [1, 2, [3, 4], 5]

# But nested objects are still shared!
shallow_copy[2].append(5)
print(original)      # [1, 2, [3, 4, 5]] - nested list changed!
print(shallow_copy)  # [1, 2, [3, 4, 5], 5]

# Deep copy (for nested structures)
import copy
deep_copy = copy.deepcopy(original)
deep_copy[2].append(6)
print(original)   # [1, 2, [3, 4, 5]] - unchanged
print(deep_copy)  # [1, 2, [3, 4, 5, 6]]
```

## Checking Mutability

You can check if an object is mutable by trying to modify it or using the `id()` function:

```python
# Check with id()
x = "hello"
print(id(x))
x = x + " world"  # Creates new object
print(id(x))  # Different ID = immutable

y = [1, 2, 3]
print(id(y))
y.append(4)  # Modifies same object
print(id(y))  # Same ID = mutable
```

## Summary Table

| Type | Mutable? | Example |
|------|----------|---------|
| int | ❌ Immutable | `x = 5` |
| float | ❌ Immutable | `x = 3.14` |
| str | ❌ Immutable | `x = "hello"` |
| tuple | ❌ Immutable | `x = (1, 2, 3)` |
| bool | ❌ Immutable | `x = True` |
| frozenset | ❌ Immutable | `x = frozenset([1, 2, 3])` |
| list | ✅ Mutable | `x = [1, 2, 3]` |
| dict | ✅ Mutable | `x = {"a": 1}` |
| set | ✅ Mutable | `x = {1, 2, 3}` |
| bytearray | ✅ Mutable | `x = bytearray(b'hello')` |

## Key Takeaways

1. **Immutable types** are safer for concurrent programming and can be used as dictionary keys
2. **Mutable types** are more flexible but require careful handling with assignments and function arguments
3. Always be aware of whether you're modifying an object or creating a new one
4. Use `copy()` or `deepcopy()` when you need independent copies of mutable objects
5. Never use mutable default arguments in function definitions






