# Understanding `encoding` in Python File Handling

In Python, **encoding** is about how text (strings) is converted to bytes and vice versa when reading or writing files.

---

## 1. Strings vs Bytes
- Python **strings** are sequences of characters (Unicode).  
- Computers store data as **bytes** (0s and 1s).  

When writing a string to a file, Python **converts the string into bytes**.  
When reading from a file, Python **converts bytes back into a string**.

---

## 2. What `encoding='utf-8'` does
It tells Python **how to perform the conversion** between strings and bytes.

### Example:
```python
text = "Hello, नमस्ते"

# Convert string to bytes using UTF-8
bytes_data = text.encode("utf-8")
print(bytes_data)
