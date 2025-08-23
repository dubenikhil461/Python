# 📘 Python Basic

## Simple Analogy

- CPU = Brain of the computer 🧠 (handles everything, but limited hands)
- GPU = Muscle with many hands 💪 (can do lots of small repetitive work in parallel)

## Python is a high-level language

- High-level language: closer to human language, easier to understand and write
- Low-level language: closer to machine language, harder to understand and write

🔹 Example in Python

Let’s say we want to add two arrays:

CPU (sequential-ish):

import numpy as np
a = np.arange(1000000)
b = np.arange(1000000)
c = a + b   # runs on CPU

GPU (parallel with CUDA or libraries like CuPy):

import cupy as cp
a = cp.arange(1000000)
b = cp.arange(1000000)
c = a + b   # runs on GPU