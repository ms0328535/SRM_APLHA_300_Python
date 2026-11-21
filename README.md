# Python Programming Repository

A collection of Python examples covering beginner programming, intermediate Python concepts, and object-oriented programming (OOP). The repository is organized by topic and contains small programs that demonstrate syntax, data structures, reusable functions, concurrency, and class design.

## Table of Contents

- [Repository Structure](#repository-structure)
- [1. Python for Beginners](#1-python-for-beginners)
- [2. Intermediate Python Programming](#2-intermediate-python-programming)
- [3. Object-Oriented Programming](#3-object-oriented-programming)
- [Time and Space Complexity](#time-and-space-complexity)
- [How to Run](#how-to-run)
- [Notes](#notes)

## Repository Structure

```text
Python-main/
├── Python for beginners/
│   ├── Projects/
│   │   ├── Black_Jack.py
│   │   └── rsp.py
│   └── beginner topic scripts
├── Intermediate_Python_Programming/
│   └── intermediate topic scripts
├── Intermediate/
│   ├── Intermediate.py
│   ├── helper.py
│   └── example.json
└── Object_Oriented_Programming/
    ├── item.py
    ├── phone.py
    ├── keyboard.py
    └── OOP topic scripts
```

---

## 1. Python for Beginners

These programs introduce the basic building blocks of Python. They are intended to show how a particular language feature works, rather than solve a single large problem.

| File / Topic | What the program demonstrates | Problem / objective | Reason for the approach | Time complexity | Auxiliary space |
|---|---|---|---|---|---|
| `Hello.py` | Printing text to the console | Display a basic message | `print()` is the simplest way to produce console output | O(1) | O(1) |
| `Variables.py` | Variables, values, and basic operations | Store and work with different kinds of data | Variables give readable names to values and allow values to be reused | O(1) per operation | O(1) |
| `User_inputs.py` | Reading input from a user | Accept data while the program is running | `input()` makes a program interactive; conversion functions turn text into numeric values when needed | O(1) per input operation, excluding input length | O(L), where L is input length |
| `if_statements.py` | `if`, `elif`, and `else` | Choose an action based on a condition | Conditional branching ensures that only the matching block is executed | O(1) for a fixed number of conditions | O(1) |
| `Loops.py` | Iteration using loops | Repeat instructions or process a sequence | A loop avoids writing the same instruction repeatedly | O(n) for n iterations | O(1), excluding stored output |
| `Functions.py` | Defining and calling functions | Reuse a named block of logic | Functions divide a program into smaller, reusable units | Depends on the function body; a simple call is O(1) | Depends on local variables |
| `Lists.py` | Creating, indexing, and modifying lists | Store an ordered collection of values | Lists are useful when values need to be grouped and updated | Indexing O(1); searching O(n); append amortized O(1) | O(n) for n stored elements |
| `Tuples.py` | Tuple creation, indexing, and slicing | Store an ordered collection that should not be modified | Tuples provide an immutable sequence | Indexing O(1); searching O(n); slicing O(k) for k selected elements | O(1) for indexing; O(k) for a new slice |
| `Dictionaries.py` | Key-value storage and lookup | Retrieve values using meaningful keys | Dictionaries provide average O(1) key lookup and make related data easy to access | Average lookup/insert/delete O(1); worst case can be O(n) | O(n) for n entries |
| `Strings.py` | String creation, indexing, slicing, and methods | Process text data | String methods make common text operations concise; strings are immutable | Indexing O(1); scanning/searching O(n); concatenation depends on result length | O(n) for newly created strings |
| `Recursion.py` | A function calling itself (factorial example) | Solve a problem by reducing it to smaller instances | Factorial naturally reduces from n! to n × (n−1)! until the base case | O(n) | O(n) call-stack space |
| `Libraries.py` | Importing and using Python libraries | Reuse functionality provided by modules | Libraries avoid reimplementing common operations | Depends on the library function used | Depends on the function used |
| `Other_topics.py` | Additional language features (including lambda and recursion examples) | Demonstrate compact functions and related Python concepts | Small examples make individual features easier to understand | Lambda call O(1) for a constant-size expression; factorial example O(n) | O(1) for lambda; O(n) stack for recursive factorial |
| `Class_and_Objects.py` | Basic class and object concepts | Group data and behavior into objects | Classes provide a reusable blueprint for creating objects | Object creation and simple attribute access O(1) | O(1) per object, excluding referenced data |

### Beginner projects

| File | Project explanation | Reason for the approach | Time complexity | Auxiliary space |
|---|---|---|---|---|
| `Projects/Black_Jack.py` | A console-based Blackjack game. It models cards, player/computer turns, scoring, and game decisions. | Separating card handling, scoring, and turn logic makes the game easier to follow and maintain. | Depends on the number of cards/actions in a round; typically O(c) for c processed cards. | O(c) for the cards held/processed |
| `Projects/rsp.py` | A Rock-Paper-Scissors game in which the user plays against a computer choice. | Conditional statements compare the two choices and decide win, loss, or tie. | O(1) per round | O(1) |

---

## 2. Intermediate Python Programming

This section demonstrates built-in data structures and features that help write more expressive and maintainable Python programs.

| File / Topic | What the program demonstrates | Problem / objective | Reason for the approach | Time complexity | Auxiliary space |
|---|---|---|---|---|---|
| `Intermediate.py` | Lists, tuples, dictionaries, sets, strings, `collections`, and `timeit` | Compare and practice commonly used Python data structures | Each structure is suited to a different need: ordered mutable data, immutable sequences, key-value lookup, uniqueness, or specialized collection behavior | Depends on the operation: list append amortized O(1), list search O(n), dictionary/set average lookup O(1), string traversal O(n) | O(n) for collections containing n elements; operations may allocate additional copies |
| `Asterisk.py` | `*args`, `**kwargs`, unpacking, and iterable expansion | Pass a flexible number of positional and keyword arguments | Argument unpacking allows functions to accept and forward variable amounts of data | O(k) to process k supplied arguments | O(k) when arguments are collected into a tuple or dictionary |
| `Collections.py` | Specialized containers from the `collections` module | Use tools such as `Counter`, `namedtuple`, `defaultdict`, `deque`, and `OrderedDict` | Specialized containers provide convenient behavior for counting, structured records, default values, and efficient operations at both ends | `Counter` construction O(n); dictionary-like average lookup O(1); deque append/pop at either end O(1) | O(u) for u distinct counted values, or O(n) for n stored elements |
| `Context managers.py` | The `with` statement and resource management | Safely acquire and release resources | A context manager runs cleanup logic automatically, including when an exception occurs | Depends on the resource operation; context entry/exit is generally O(1) | Usually O(1), excluding the resource itself |
| `Decorators.py` | Functions that wrap other functions | Add behavior to a function without changing its main implementation | A decorator separates reusable extra behavior from the original function | Usually O(1) extra overhead per call, excluding the wrapped function | Usually O(1) wrapper state, excluding captured data |
| `Dictionary.py` | Dictionary creation, access, update, deletion, and iteration | Store information as key-value pairs | A dictionary provides direct access through keys | Average lookup/insert/delete O(1); iteration O(n); worst-case lookup O(n) | O(n) |
| `Exceptions.py` | `try`, `except`, `else`, and `finally` | Handle runtime errors without abruptly terminating the program | Exception handling provides a controlled response to invalid operations or unexpected conditions | Normal execution depends on the statements; exception handling adds work when an exception occurs | Usually O(1), excluding exception data and traceback |
| `Function arguments.py` | Positional, keyword, default, and variable-length arguments | Understand how values are passed into functions | Different argument styles make functions flexible and easier to call | O(k) when processing k arguments; otherwise depends on the function body | O(k) if variable arguments are collected |
| `Generators.py` | `yield` and generator iteration | Produce values one at a time instead of building an entire result list | Lazy evaluation can reduce memory use when processing large sequences | O(n) to consume n generated values, plus the cost of producing each value | Often O(1) generator state, excluding values retained by the generator |
| `IterTools.py` | Iterator tools such as product, permutations, combinations, accumulation, and grouping | Process combinations and sequences without manually implementing iterator logic | `itertools` provides efficient iterator-based building blocks | Depends on the operation and number of generated results; producing r results costs at least O(r) | Often O(1) iterator state, but materializing results requires O(r) |
| `JSON.py` | Reading, writing, and converting JSON data | Exchange structured data between Python and JSON files/text | JSON is a common, language-independent data-interchange format | O(n) in the size of the JSON data for encoding/decoding | O(n) for the parsed or serialized representation |
| `Lambda.py` | Anonymous functions using `lambda` | Define a short function in a single expression | A lambda is convenient for small functions passed as arguments | Depends on the expression; a simple arithmetic lambda is O(1) | O(1) for a simple expression |
| `Lists.py` | List operations, comprehensions, and transformations | Create and process ordered collections | List comprehensions express simple transformations clearly and compactly | O(n) for one pass over n elements; sorting O(n log n) | O(n) when a new list of n elements is created |
| `Logging.py` | Logging messages at different severity levels | Record program events and errors | Logging provides configurable output and is more useful than scattered debugging prints in larger applications | O(1) per message before formatting/output; actual I/O depends on the handler | O(1) per active record, excluding buffers and log files |
| `Multiprocessing .py` | Processes, shared values/arrays, locks, queues, and process pools | Run work in separate processes and coordinate shared data | Multiprocessing can use multiple CPU cores for CPU-bound work; locks protect shared updates | For n tasks, total work depends on each task; parallel runtime also depends on process startup, communication, and synchronization | O(p) process-management overhead plus shared data and queued results |
| `RandomNumbers.py` | Generating random values and selecting/shuffling data | Produce pseudo-random values for simulations or games | The `random` module provides ready-made random operations | Generating one value O(1); shuffling n elements O(n) | O(1) for one value; shuffle is generally in-place |
| `Sets.py` | Sets, uniqueness, membership, and set operations | Store distinct values and compare collections | Sets automatically remove duplicates and provide efficient average membership tests | Average membership/add/remove O(1); union/intersection typically O(n+m) for set sizes n and m | O(n) for n unique elements; a new set operation may allocate O(n+m) |
| `Strings.py` | String methods, formatting, splitting, joining, and manipulation | Process and format text | Built-in string methods reduce manual character processing | Usually O(n) for operations that scan or create a string of length n | O(n) when a new string/list is produced |
| `Threading in Python.py` | Creating threads, starting/joining them, and sharing data | Perform multiple tasks within one process | Threads are useful for overlapping I/O-bound work; shared state requires care | Depends on task workload; thread creation and coordination add overhead | O(t) thread-stack/management overhead for t threads |
| `Threading vs Multiprocessing.py` | Comparing threads and processes | Choose a concurrency model for a workload | Threads share process memory; processes have separate memory and can execute CPU-bound Python work across cores | Depends on workload and coordination overhead | Threads: O(t) overhead; processes: O(p) process overhead plus inter-process data |

---

## 3. Object-Oriented Programming

OOP organizes programs around classes and objects. The examples below use an `Item` class and related classes to demonstrate object creation, attributes, methods, inheritance, and encapsulation.

| File / Topic | What the program demonstrates | Problem / objective | Reason for the approach | Time complexity | Auxiliary space |
|---|---|---|---|---|---|
| `Intro_to_OOP.py` | Creating a class, creating objects, assigning attributes, and calling a method | Calculate the total price using price × quantity for different items | A class groups related data and behavior; multiple objects can use the same method | O(1) per calculation | O(1) per object, excluding referenced data |
| `Constructor_and,__init__.py` | The `__init__` constructor and attribute validation | Initialize each item with a name, price, and quantity | Constructors establish a valid initial object state; assertions check the supplied values | O(1) per object initialization | O(1) per object |
| `Class_attribute.py` | Class attributes, instance attributes, a shared list, and `__repr__` | Share a discount rate and track created items | Class attributes store data shared by instances, while instance attributes store object-specific data | O(1) per item creation; appending to `all` is amortized O(1) | O(n) for n tracked objects |
| `Class_inheritence.py` | Inheritance and `super()` using `Item` and `Phone` | Reuse common item behavior while adding phone-specific information | Inheritance avoids duplicating common attributes and methods | O(1) for constructing one object, excluding external work | O(1) per object |
| `Class_vs_static_method.py` | Instance methods, class methods, static methods, and loading records from CSV | Demonstrate methods that work with an object, a class, or independent input | Each method type communicates what data it needs; the class method can construct objects from CSV records | O(n) to read and instantiate n CSV records; simple methods O(1) | O(n) because the CSV rows are first stored in a list |
| `Getters_and_setters.py` | Accessing and changing an object's attribute | Demonstrate controlled attribute access through properties in the `Item` class | A property can validate a value before updating the underlying attribute | O(1) for the shown getter/setter, excluding the length of the assigned name | O(1) |
| `OOP_principle.py` | Using an inherited `Keyboard` class and an inherited discount method | Apply shared item behavior to a specialized keyboard object | The subclass reuses the parent class implementation and can define its own discount rate | O(1) for the shown discount calculation | O(1) per object |
| `item.py` | Encapsulation, properties, validation, class methods, static methods, and object representation | Build a reusable base `Item` class with controlled name access and common item operations | Private-style attributes and property setters protect data; class/static methods provide class-level and utility behavior | Total price and discount O(1); CSV loading O(n) for n rows | O(1) per item; CSV loading O(n) |
| `phone.py` | A `Phone` subclass derived from `Item` | Add phone-specific data such as the number of broken phones | Inheritance reuses the common item fields and behavior while extending the object | O(1) per object creation | O(1) per object |
| `keyboard.py` | A `Keyboard` subclass with its own class-level discount rate | Represent a keyboard as a specialized item | The subclass inherits common item functionality and overrides a class attribute | O(1) per object creation | O(1) per object |
| `helper.py` | Example definitions of static and class methods | Explain when a method needs the class reference and when it does not | Static methods do not receive an automatic class/instance reference; class methods receive `cls` | O(1) for the shown method calls | O(1) |

### Main OOP ideas covered

- **Class:** A blueprint used to create objects.
- **Object:** An instance of a class with its own data.
- **Constructor (`__init__`):** Initializes an object when it is created.
- **Instance attributes:** Data belonging to an individual object.
- **Class attributes:** Data shared by instances of a class.
- **Encapsulation:** Controls how internal data is accessed or modified.
- **Inheritance:** Allows a child class to reuse and extend a parent class.
- **Class method:** Receives the class as `cls`.
- **Static method:** Does not receive an automatic instance or class reference.
- **Polymorphism:** Allows the same operation or interface to work with different object types. The `poly_explain.py` file illustrates the built-in `len()` working with both a string and a list.

---

## Time and Space Complexity

Complexity describes how an algorithm's resource requirements grow as its input grows.

### Common time complexities

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Accessing a list element by index |
| O(log n) | Logarithmic | Binary search on sorted data |
| O(n) | Linear | Traversing a list once |
| O(n log n) | Linearithmic | Efficient comparison-based sorting |
| O(n²) | Quadratic | Two nested loops over the same n elements |

### Common space complexities

| Complexity | Meaning | Example |
|---|---|---|
| O(1) | Constant auxiliary memory | Using a fixed number of variables |
| O(n) | Memory grows linearly | Creating a new list containing n values |
| O(n²) | Memory grows quadratically | Creating an n-by-n matrix |

### How to interpret the tables in this README

- `n` means the number of input elements or records.
- `k` means the number of arguments, generated results, or selected elements, as specified in the row.
- `t` means the number of threads; `p` means the number of processes.
- Auxiliary space means extra memory used by the operation, not necessarily the memory occupied by the original input.
- Complexity is stated for the operation demonstrated, not for every possible use of the Python feature.
- For built-in operations, average-case complexity is given where appropriate. Actual performance can depend on Python implementation, input size, and data distribution.
- For concurrency examples, wall-clock time depends on scheduling, CPU availability, task size, and communication overhead; Big-O alone does not describe the speed-up.

---

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the repository folder in VS Code or a terminal.
4. Run an individual Python file:

```bash
python "Python for beginners/Hello.py"
```

For a file in another folder:

```bash
python "Intermediate_Python_Programming/Generators.py"
python "Object_Oriented_Programming/Intro_to_OOP.py"
```

Some OOP examples import `item.py`, `phone.py`, or `keyboard.py`. Run them from the `Object_Oriented_Programming` folder so that the local imports can be found.

For multiprocessing examples, run the script as a normal `.py` file rather than relying on an interactive notebook. The `if __name__ == "__main__":` guard is important, particularly on Windows.

## Notes

- This repository is a learning collection of Python demonstrations and small projects; many files are examples rather than standalone problem statements.
- Some scripts intentionally demonstrate errors or invalid operations (for example, assigning to a tuple element). Such a script may stop when it reaches the demonstrated error.
- Complexity values are explanatory estimates based on the operations in the source files. Where a program does not define a single input-driven algorithm, the complexity is described per operation or in terms of the number of records processed.
- `__pycache__`, temporary runner files, generated logs, and sample JSON/CSV data are supporting files rather than separate programming questions.
