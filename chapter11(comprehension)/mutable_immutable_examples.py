"""
Mutable vs Immutable Types in Python - Practical Examples
"""

# ============================================
# IMMUTABLE TYPES
# ============================================

print("=" * 50)
print("IMMUTABLE TYPES")
print("=" * 50)

# 1. Strings (Immutable)
print("\n1. Strings:")
text = "Hello"
print(f"Original: {text}, ID: {id(text)}")
text = text + " World"  # Creates NEW string
print(f"Modified: {text}, ID: {id(text)}")
print("Different IDs = Immutable")

# 2. Integers (Immutable)
print("\n2. Integers:")
x = 5
y = x
print(f"x = {x}, y = {y}")
print(f"x ID: {id(x)}, y ID: {id(y)}")
y = 10
print(f"After y = 10: x = {x}, y = {y}")
print(f"x ID: {id(x)}, y ID: {id(y)}")
print("x unchanged, y is new object")

# 3. Tuples (Immutable)
print("\n3. Tuples:")
my_tuple = (1, 2, 3)
print(f"Original: {my_tuple}, ID: {id(my_tuple)}")
my_tuple = my_tuple + (4,)  # Creates NEW tuple
print(f"Modified: {my_tuple}, ID: {id(my_tuple)}")
print("Different IDs = Immutable")

# ============================================
# MUTABLE TYPES
# ============================================

print("\n" + "=" * 50)
print("MUTABLE TYPES")
print("=" * 50)

# 1. Lists (Mutable)
print("\n1. Lists:")
my_list = [1, 2, 3]
print(f"Original: {my_list}, ID: {id(my_list)}")
my_list.append(4)  # Modifies SAME object
print(f"After append: {my_list}, ID: {id(my_list)}")
print("Same ID = Mutable")

# 2. Lists - Reference Behavior
print("\n2. Lists - Reference Behavior:")
a = [1, 2, 3]
b = a  # Both point to same object
print(f"a = {a}, b = {b}")
print(f"a ID: {id(a)}, b ID: {id(b)}")
b.append(4)
print(f"After b.append(4):")
print(f"a = {a}, b = {b}")
print(f"Both changed! Same object: {a is b}")

# 3. Dictionaries (Mutable)
print("\n3. Dictionaries:")
my_dict = {"name": "Alice", "age": 30}
print(f"Original: {my_dict}, ID: {id(my_dict)}")
my_dict["city"] = "New York"
print(f"After adding key: {my_dict}, ID: {id(my_dict)}")
print("Same ID = Mutable")

# 4. Sets (Mutable)
print("\n4. Sets:")
my_set = {1, 2, 3}
print(f"Original: {my_set}, ID: {id(my_set)}")
my_set.add(4)
print(f"After add: {my_set}, ID: {id(my_set)}")
print("Same ID = Mutable")

# ============================================
# FUNCTION ARGUMENTS
# ============================================

print("\n" + "=" * 50)
print("FUNCTION ARGUMENTS")
print("=" * 50)

# Immutable in function
def modify_string(s):
    s = s + " modified"
    return s

text = "Hello"
print(f"\nBefore function: {text}")
result = modify_string(text)
print(f"After function: {text}")
print(f"Function returned: {result}")
print("Original unchanged (immutable)")

# Mutable in function
def modify_list(lst):
    lst.append(4)
    return lst

my_list = [1, 2, 3]
print(f"\nBefore function: {my_list}")
result = modify_list(my_list)
print(f"After function: {my_list}")
print(f"Function returned: {result}")
print("Original changed (mutable)!")

# ============================================
# DEFAULT ARGUMENTS PITFALL
# ============================================

print("\n" + "=" * 50)
print("DEFAULT ARGUMENTS PITFALL")
print("=" * 50)

# BAD: Mutable default argument
def bad_function(item, my_list=[]):
    my_list.append(item)
    return my_list

print("\nBAD Example:")
print(bad_function(1))  # [1]
print(bad_function(2))  # [1, 2] - unexpected!
print(bad_function(3))  # [1, 2, 3] - keeps growing!

# GOOD: Use None as default
def good_function(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print("\nGOOD Example:")
print(good_function(1))  # [1]
print(good_function(2))  # [2] - correct!
print(good_function(3))  # [3] - correct!

# ============================================
# COPYING OBJECTS
# ============================================

print("\n" + "=" * 50)
print("COPYING OBJECTS")
print("=" * 50)

# Shallow copy
original = [1, 2, [3, 4]]
shallow_copy = original.copy()

print(f"\nOriginal: {original}")
print(f"Shallow copy: {shallow_copy}")
print(f"Same object? {original is shallow_copy}")

shallow_copy.append(5)
print(f"\nAfter appending to copy:")
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# Nested objects still shared
shallow_copy[2].append(5)
print(f"\nAfter modifying nested list in copy:")
print(f"Original: {original}")  # Changed!
print(f"Shallow copy: {shallow_copy}")

# Deep copy
import copy
deep_copy = copy.deepcopy(original)
deep_copy[2].append(6)
print(f"\nAfter modifying nested list in deep copy:")
print(f"Original: {original}")  # Unchanged
print(f"Deep copy: {deep_copy}")

# ============================================
# MUTABLE CONTAINING IMMUTABLE
# ============================================

print("\n" + "=" * 50)
print("MUTABLE CONTAINING IMMUTABLE")
print("=" * 50)

# List containing immutable types
print("\n1. List (mutable) containing immutable types:")
my_list = [1, 2, 3, "hello", (4, 5), True]
print(f"List: {my_list}")
print(f"List ID: {id(my_list)}")
my_list.append(6)  # Can modify the list
print(f"After append: {my_list}")
print(f"List ID: {id(my_list)} (same - list is mutable)")
print("✅ Mutable container can hold immutable elements")

# Dictionary with immutable keys
print("\n2. Dictionary (mutable) with immutable keys:")
my_dict = {
    "name": "Alice",
    "age": 30,
    (1, 2): "tuple_key"
}
print(f"Dict: {my_dict}")
my_dict["city"] = "NYC"  # Can modify the dict
print(f"After adding key: {my_dict}")
print("✅ Dictionary keys must be immutable (hashable)")

# Set containing immutable elements
print("\n3. Set (mutable) containing immutable elements:")
my_set = {1, 2, 3, "hello", (4, 5), frozenset([6, 7])}
print(f"Set: {my_set}")
my_set.add(8)  # Can modify the set
print(f"After add: {my_set}")
print("✅ Set elements must be immutable (hashable)")

# ============================================
# IMMUTABLE CONTAINING MUTABLE
# ============================================

print("\n" + "=" * 50)
print("IMMUTABLE CONTAINING MUTABLE")
print("=" * 50)

# Tuple containing mutable objects
print("\n1. Tuple (immutable) containing list (mutable):")
my_tuple = (1, 2, [3, 4], "hello")
print(f"Tuple: {my_tuple}")
print(f"Tuple ID: {id(my_tuple)}")

# Cannot modify tuple structure
print("\nTrying to modify tuple directly:")
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"❌ Error: {e}")

# But can modify mutable object inside
print("\nModifying list inside tuple:")
my_tuple[2].append(5)  # This works!
print(f"After modifying list: {my_tuple}")
print(f"Tuple ID: {id(my_tuple)} (same - tuple is still immutable)")
print("⚠️ Tuple structure is immutable, but mutable elements inside can change!")

# Demonstrating the behavior
print("\n2. Demonstrating tuple with mutable elements:")
nested_tuple = ([1, 2], [3, 4])
print(f"Original: {nested_tuple}")
nested_tuple[0].append(5)
print(f"After modifying first list: {nested_tuple}")
print("The tuple 'appears' to change, but it's the list inside that changed")

# Frozenset - can only contain immutable
print("\n3. Frozenset (immutable) - can only contain immutable elements:")
frozen = frozenset([1, 2, 3, "hello", (4, 5)])
print(f"Frozenset: {frozen}")
print("✅ Frozenset can contain immutable elements")
print("❌ Frozenset cannot contain mutable elements (not hashable)")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 50)
print("QUICK REFERENCE")
print("=" * 50)

print("\nImmutable Types:")
print("  - int, float, str, tuple, bool, frozenset, bytes")
print("  - Cannot be modified after creation")
print("  - Operations create new objects")

print("\nMutable Types:")
print("  - list, dict, set, bytearray")
print("  - Can be modified after creation")
print("  - Changes affect the same object")

print("\nKey Points:")
print("  1. Immutable types are safer for concurrent programming")
print("  2. Immutable types can be used as dictionary keys")
print("  3. Mutable types require careful handling with assignments")
print("  4. Never use mutable default arguments in functions")
print("  5. Use copy() or deepcopy() when you need independent copies")

