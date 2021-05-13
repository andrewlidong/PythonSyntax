Notes from: https://data-flair.training/blogs/python-interview-questions/

Q.4. Explain join() and split() in Python.

join() lets us join characters from a string together by a character we specify.

split() lets us split a string around the character we specify.

Q.20. So does recursion cause any trouble?

Sure does:

Needs more function calls.
Each function call stores a state variable to the program stack- consumes memory, can cause memory overflow.
Calling a function consumes time.
Q.21. What good is recursion?

With recursion, we observe the following:

Need to put in less efforts.
Smaller code than that by loops.
Easier-to-understand code.

Q.26. How would you randomize the contents of a list in-place?

For this, we’ll import the function shuffle() from the module random.


Q.27. How do you remove the leading whitespace in a string?

Leading whitespace in a string is the whitespace in a string before the first non-whitespace character. To remove it from a string, we use the method lstrip().


Q.29. What is the enumerate() function in Python?

enumerate() iterates through a sequence and extracts the index position and its corresponding value too.


Q.31. Where will you use while rather than for?

Although we can do with for all that we can do with while, there are some places where a while loop will make things easier-

For simple repetitive looping
When we don’t need to iterate through a list of items- like database records and characters in a string.

Q.34. Differentiate between deep and shallow copy.

A deep copy copies an object into another. This means that if you make a change to a copy of an object, it won’t affect the original object. In Python, we use the function deepcopy() for this, and we import the module copy. We use it like:

A shallow copy, however, copies one object’s reference to another. So, if we make a change in the copy, it will affect the original object. For this, we have the function copy(). We use it like:

Python Developer Interview Questions
Q.35. Can you make a local variable’s name begin with an underscore? (developer)

You can, but you should not. This is because:

Local variables indicate private variables of a class, and so, they confuse the interpreter.

Q.36. Is a NumPy array better than a list?

NumPy arrays have 3 benefits over lists:

They are faster
They require less memory
They are more convenient to work with

Q.42. Can I dynamically load a module in Python?

Dynamic loading is where we do not load a module till we need it. This is slow, but lets us utilize the memory more efficiently. In Python, you can use the importlib module for this:

Q.43. Which methods/functions do we use to determine the type of instance and inheritance?

Here, we talk about three methods/functions- type(), isinstance(), and issubclass().

a. type()

This tells us the type of object we’re working with.

b. isinstance()

This takes in two arguments- a value and a type. If the value is of the kind of the specified type, it returns True. Else, it returns False.

c. issubclass()

This takes two classes as arguments. If the first one inherits from the second, it returns True. Else, it returns False.

Q.44. Are methods and constructors the same thing?

No, there are subtle but considerable differences-

We must name a constructor in the name of the class; a method name can be anything.
Whenever we create an object, it executes a constructor; whenever we call a method, it executes a method.
For one object, a constructor executes only once; a method can execute any number of times for one object.
We use constructors to define and initialize non-static variables; we use methods to represent business logic to perform operations.

Q.45. What is a Python module?

A module is a script in Python that defines import statements, functions, classes, and variables. It also holds runnable Python code. ZIP files and DLL files can be modules too. The module holds its name as a string that is in a global variable.

Q.47. Explain, in brief, the uses of the modules sqlite3, ctypes, pickle, traceback, and itertools.

sqlite3- Helps with handling databases of type SQLite
ctypes- Lets create and manipulate C data types in Python
pickle- Lets put any data structure to external files
traceback- Allows extraction, formatting, and printing of stack traces
itertools– Supports working with permutations, combinations, and other useful iterables.

Q.48. Explain inheritance in Python.

When one class inherits from another, it is said to be the child/derived/sub class inheriting from the parent/base/super class. It inherits/gains all members (attributes and methods).

Single Inheritance- A class inherits from a single base class.
Multiple Inheritance- A class inherits from multiple base classes.
Multilevel Inheritance- A class inherits from a base class, which, in turn, inherits from another base class.
Hierarchical Inheritance- Multiple classes inherit from a single base class.
Hybrid Inheritance- Hybrid inheritance is a combination of two or more types of inheritance.

Q.49. Explain memory management in Python.

Objects and data structures in Python lie on a private heap. The Python memory manager internally manages this. It delegates some work to object-specific allocators while ensuring they operate only within the private heap. Actually, the interpreter manages this heap; the user has no control over it- not even if they manipulate object pointers to memory blocks inside the heap. The Python memory manager allocates heap space to objects and other internal buffers on demand.

Q.51. How would you make a Python script executable on Unix?

For this to happen, two conditions must be met:

The script file’s mode must be executable
The first line must begin with a hash(#). An example of this will be: #!/usr/local/bin/python

Q.52. What functions or methods will you use to delete a file in Python?

For this, we may use remove() or unlink().

Q.55. Explain lambda expressions. When would you use one?

When we want a function with a single expression, we can define it anonymously. A lambda expression may take input and returns a value. To define the above function as a lambda expression, we type the following code in the interpreter:

Q.56. What is a generator?

Python generator produces a sequence of values to iterate on. This way, it is kind of an iterable.
We define a function that ‘yields’ values one by one, and then use a for loop to iterate on it.

Q.57. So, what is an iterator, then?

An iterator returns one object at a time to iterate on. To create an iterator, we use the iter() function.

Q.58. Okay, we asked you about generators and iterators, and you gave us the right answers. But don’t they sound similar?

They do, but there are subtle differences:

For a generator, we create a function. For an iterator, we use in-built functions iter() and next().
For a generator, we use the keyword ‘yield’ to yield/return an object at a time.
A generator may have as many ‘yield’ statements as you want.
A generator will save the states of the local variables every time ‘yield’ will pause the loop. An iterator does not use local variables; it only needs an iterable to iterate on.
Using a class, you can implement your own iterator, but not a generator.
Generators are fast, compact, and simpler.
Iterators are more memory-efficient.


Q.59. What is a decorator?

A decorator is a function that adds functionality to another function without modifying it. It wraps another function to add functionality to it. Take an example.



Q.60. What is Monkey Patching?

Monkey patching refers to modifying a class or module at runtime (dynamic modification). It extends Python code at runtime.


Q.61. Why should we hire you?

Q.62. What personal growth did you see in yourself after your last job?

Q.63. Tell me about a situation you found yourself stuck in your previous job. How did you work your way out?

Q.64. How would you resolve a dispute with a colleague? Did you face such a situation in your previous job?

Q.65. What do you expect us to do better than your previous employer?

Q.66. Have you ever changed someone’s opinion at work?

Q.67. What are your thoughts on office gossips?

Q.68. What would be the weakest link to your performance?

Q.69. Where do you think the industry is going in the next 15 years?

Q.70. What legacy did you leave in your previous job? Did you develop an innovative solution?

Q.71. Would you prefer working alone, or in a small/large team?

