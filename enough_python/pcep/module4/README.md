# modulo 4

## Module 4 Summary

### 1. **Functions in Python**

- **Definition & Purpose:** Functions are blocks of code designed to perform specific tasks, allow code reuse, and
  enable isolated testing (decomposition).
- **Types:**
    - **Built-in functions:** Provided by Python (e.g., `print()`, `len()`).
    - **Pre-installed modules:** Such as `copy`, `datetime`, `math`, need to be imported.
    - **User-defined functions:** Defined with the `def` statement.
- **Naming:** Don’t use the same name for a function and a variable.

### 2. **Function Parameters and Arguments**

- **Positional arguments:** Matched by position.
- **Keyword arguments:** Explicitly specify parameter names.
- **Mixing:** Positional must come before keyword arguments.
- **Default values:** Defined in parameter list (e.g., `def intro(first_name, last_name="Perez")`).
- **Return statement:** Ends function execution and optionally sends a value back.

### 3. **Function Scope and Variable Lifetime**

- **Local scope:** Variables defined inside functions cannot be accessed outside.
- **Global scope:** Variables outside functions are accessible inside unless shadowed by a local variable.
- **Global keyword:** Used inside a function to modify a global variable.

### 4. **Mutability and Behavior with Lists**

- **Scalar variables (int, float, str):** Passed by value; changes inside functions don't affect the original variable.
- **Mutable objects (lists, dictionaries):** Passed by reference; modification inside functions can affect the original
  object.
- **Copying:**
    - **Shallow copy (`[:]`):** For flat lists.
    - **Deep copy (`copy.deepcopy()`):** For nested lists.

### 5. **Practical Function Examples**

- **Leap year calculation**
- **Calculating day of the year**
- **Prime number check**
- **Mileage and fuel efficiency conversions**
- **BMI calculation (with unit converters)**

### 6. **Tuples and Dictionaries**

- **Tuples:** Immutable sequences, allow multiple assignments, support unpacking but cannot be changed after creation.
- **Dictionaries:** Key-value pairs, mutable, not ordered in older Python versions but ordered in ≥3.6, versatile for
  storing data like translations or mappings.
- **Useful methods:** `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`, `.clear()`, `.copy()`, `.popitem()`

### 7. **Error Handling and Exceptions**

- **Common exceptions:** `NameError`, `TypeError`, `ValueError`, `KeyError`, `ZeroDivisionError`, `AttributeError`,
  `SyntaxError`.
- **Exception handling:** Use `try-except` blocks to manage expected/unexpected errors, ensuring programs don’t crash.
- **Multiple exceptions:** Can handle several exceptions in one block.

### 8. **Some Simple Algorithms**

- **Fibonacci numbers:** Both iterative and recursive versions.
- **Factorials:** Iterative and recursive examples.
- **Triangle checks:** Validity and specific types (right triangle), Heron's formula for area.

### 9. **Small Data Projects**

- **Counting elements**
- **Merging dictionaries**
- **Processing colors as tuples/lists for dictionary creation**

### 10. **Miscellaneous**

- **Type conversions:** E.g., between tuples and lists.
- **Best practices:** Test each code path, handle exceptions properly, understand mutability.

---

Let me know if you’d like a more focused summary or have any specific section you’d like further explained!