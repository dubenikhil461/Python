# 📘 Number

## 1. Basic Operations
>>> x,y,z = (1,2,3)
>>> x
1
>>> y
2
>>> z
3
>>>2**3 (power)
>>>8

Almost 🙂 — not exactly "as it is", but repr() tries to show the “raw” representation of the object so that:
It includes quotes around strings.
It shows escape characters like \n, \t, \\ instead of interpreting them.
It’s meant to be unambiguous (often valid Python syntax).

s = "Hello\nWorld"

print(s)        # Hello
                # World  (newline interpreted)
print(str(s))   # Hello
                # World  (same as print)
print(repr(s))  # 'Hello\nWorld'  (keeps \n visible, adds quotes)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"  # unambiguous
    
    def __str__(self):
        return f"{self.name} has {self.marks} marks"    # readable

s = Student("Soham", 90)

print(repr(s))  # Student('Soham', 90)
print(str(s))   # Soham has 90 marks
print(s)        # Soham has 90 marks
