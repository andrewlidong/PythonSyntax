Notes from: https://data-flair.training/blogs/top-python-interview-questions-answer/

Q.1. What are the key features of Python?

If it makes for an introductory language to programming, Python must mean something. These are its qualities:

Interpreted
Dynamically-typed
Object-oriented
Concise and simple
Free
Has a large community

Q.2. Differentiate between lists and tuples.

The major difference is that a list is mutable, but a tuple is immutable. Examples:

Q.3. Explain the ternary operator in Python.

[on true] if [expression] else [on false]

Q.4. What are negative indices?

A negative index, unlike a positive one, begins searching from the right.

This also helps with slicing from the back:

Q.5. Is Python case-sensitive?

Python is indeed case-sensitive.

Q.6. How long can an identifier be in Python?

According to the official Python documentation, an identifier can be of any length. However, PEP 8 suggests that you should limit all lines to a maximum of 79 characters. Also, PEP 20 says ‘readability counts’. So, a very long identifier will violate PEP-8 and PEP-20.

Apart from that, there are certain rules we must follow to name one:

It can only begin with an underscore or a character from A-Z or a-z.
The rest of it can contain anything from the following: A-Z/a-z/_/0-9.
Python is case-sensitive, as we discussed in the previous question.
Keywords cannot be used as identifiers. Python has the following keywords:
and	def	False	import	not	True
as	del	finally	in	or	try
assert	elif	for	is	pass	while
break	else	from	lambda	print	with
class	except	global	None	raise	yield
continue	exec	if	nonlocal	return

Q.7. How would you convert a string into lowercase?

We use the lower() method for this.

To convert it into uppercase, then, we use upper().

Also, to check if a string is in all uppercase or all lowercase, we use the methods isupper() and islower().

Q.8. What is the pass statement in Python?

There may be times in our code when we haven’t decided what to do yet, but we must type something for it to be syntactically correct. In such a case, we use the pass statement.

Similarly, the break statement breaks out of a loop.

Finally, the continue statement skips to the next iteration.

Q.9. Explain help() and dir() functions in Python.

The help() function displays the documentation string and help for its argument.

Q.10. How do you get a list of all the keys in a dictionary?

For this, we use the function keys().

Q.11. What is slicing?

Slicing is a technique that allows us to retrieve only a part of a list, tuple, or string. For this, we use the slicing operator [].

Q.12. How would you declare a comment in Python?

Unlike languages like C++, Python does not have multiline comments. All it has is octothorpe (#). Anything following a hash is considered a comment, and the interpreter ignores it.

Q.13. How will you check if all characters in a string are alphanumeric?

For this, we use the method isalnum().

Q.14. How will you capitalize the first letter of a string?

Simply using the method capitalize().

Q.15. We know Python is all the rage these days. But to be truly accepting of a great technology, you must know its pitfalls as well. Would you like to talk about this?

Python’s interpreted nature imposes a speed penalty on it.
While Python is great for a lot of things, it is weak in mobile computing, and in browsers.
Being dynamically-typed, Python uses duck-typing (If it looks like a duck, it must be a duck). This can raise runtime errors.
Python has underdeveloped database access layers. This renders it a less-than-perfect choice for huge database applications.
And then, well, of course. Being easy makes it addictive. Once a Python-coder, always a Python coder.

Q.16. With Python, how do you find out which directory you are currently in?

To find this, we use the function/method getcwd(). We import it from the module os.

Q.17. How do you insert an object at a given index in Python?

Now, we use the method insert. The first argument is the index at which to insert, the second is the value to insert.

Q.18. And how do you reverse a list?

Using the reverse() method.

You can also do it via slicing from right to left:

Q.19. What is the Python interpreter prompt?


Q.20. How does a function return values?

A function uses the ‘return’ keyword to return a value. Take a look:

Q.21. How would you define a block in Python?

For any kind of statements, we possibly need to define a block of code under them. However, Python does not support curly braces. This means we must end such statements with colons and then indent the blocks under those with the same amount.

Q.22. Why do we need break and continue in Python?

Both break and continue are statements that control flow in Python loops. break stops the current loop from executing further and transfers the control to the next block. continue jumps to the next iteration of the loop without exhausting it.

Q.23. Will the do-while loop work if you don’t end it with a semicolon?

Trick question! Python does not support an intrinsic do-while loop. Secondly, to terminate do-while loops is a necessity for languages like C++.

Q.24. In one line, show us how you’ll get the max alphabetical character from a string.

For this, we’ll simply use the max function.


Q.25. What is Python good for?

Python is a jack of many trades, check out Applications of Python to find out more.

Meanwhile, we’ll say we can use it for:

Web and Internet Development
Desktop GUI
Scientific and Numeric Applications
Software Development Applications
Applications in Education
Applications in Business
Database Access
Network Programming
Games, 3D Graphics
Other Python Applications

Q.26. Can you name ten built-in functions in Python and explain each in brief?

complex()- Creates a complex number.

eval()- Parses a string as an expression.

filter()- Filters in items for which the condition is true.

format()- Lets us format a string.

hash()- Returns the hash value of an object.

hex()- Converts an integer to a hexadecimal.

input()- Reads and returns a line of string.

len()- Returns the length of an object.

locals()- Returns a dictionary of the current local symbol table.

open()- Opens a file.



Q.28. How will you convert a list into a string?

We will use the join() method for this.

Q.29. How will you remove a duplicate element from a list?

We can turn it into a set to do that.

Q.30. Can you explain the life cycle of a thread?

To create a thread, we create a class that we make override the run method of the thread class. Then, we instantiate it.
A thread that we just created is in the new state. When we make a call to start() on it, it forwards the threads for scheduling. These are in the ready state.
When execution begins, the thread is in the running state.
Calls to methods like sleep() and join() make a thread wait. Such a thread is in the waiting/blocked state.
When a thread is done waiting or executing, other waiting threads are sent for scheduling.
A running thread that is done executing terminates and is in the dead state.

Q.31. What is a dictionary in Python?

A python dictionary is something I have never seen in other languages like C++ or Java programming. It holds key-value pairs.


A dictionary is mutable, and we can also use a comprehension to create it.

Q.32. Explain the //, %, and ** operators in Python.

The // operator performs floor division. It will return the integer part of the result on division.

Similarly, ** performs exponentiation. a**b returns the value of a raised to the power b.

Finally, % is for modulus. This gives us the value left after the highest achievable division.

Q.33. What do you know about relational operators in Python.

Less than (<) If the value on the left is lesser, it returns True.

Greater than (>) If the value on the left is greater, it returns True.

This is because of the flawed floating-point arithmetic in Python, due to hardware dependencies.

Less than or equal to (<=) If the value on the left is lesser than or equal to, it returns True.

Greater than or equal to (>=) If the value on the left is greater than or equal to, it returns True.

Equal to (==) If the two values are equal, it returns True.

Not equal to (!=) If the two values are unequal, it returns True.

Q.34. What are assignment operators in Python?

We can combine all arithmetic operators with the assignment symbol.

Q.35. Explain logical operators in Python.

We have three logical operators- and, or, not.

Q.36. What are membership operators?

With the operators ‘in’ and ‘not in’, we can confirm if a value is a member in another.

Q.37. Explain identity operators in Python.

The operators ‘is’ and ‘is not’ tell us if two values have the same identity.

Q.38. Finally, tell us about bitwise operators in Python.

These operate on values bit by bit.

AND (&) This performs & on each bit pair.

OR (|) This performs | on each bit pair.

XOR (^) This performs an exclusive-OR operation on each bit pair.

Binary One’s Complement (~) This returns the one’s complement of a value.

Binary Left-Shift (<<) This shifts the bits to the left by the specified amount.

Binary Right-Shift (>>)

Q.39. What data types does Python support?

Python provides us with five kinds of data types:

Numbers – Numbers use to hold numerical values.

Strings – A string is a sequence of characters. We declare it using single or double quotes.

Lists – A list is an ordered collection of values, and we declare it using square brackets.

Tuples – A tuple, like a list, is an ordered collection of values. The difference. However, is that a tuple is immutable. This means that we cannot change a value in it.

Dictionary – A dictionary is a data structure that holds key-value pairs. We declare it using curly braces.

We can also use a dictionary comprehension:

Q.40. What is a docstring?

A docstring is a documentation string that we use to explain what a construct does. We place it as the first thing under a function, class, or a method, to describe what it does. We declare a docstring using three sets of single or double-quotes.

To get a function’s docstring, we use its __doc__ attribute.

A docstring, unlike a comment, is retained at runtime.

Q.41. How would you convert a string into an int in Python?

If a string contains only numerical characters, you can convert it into an integer using the int() function.

Q.42. How do you take input in Python?

For taking input from the user, we have the function input(). In Python 2, we had another function raw_input().

Q.43. What is a function?

When we want to execute a sequence of statements, we can give it a name. Let’s define a function to take two numbers and return the greater number.

Q.44. What is recursion?

When a function makes a call to itself, it is termed recursion. But then, in order for it to avoid forming an infinite loop, we must have a base condition.

Q.45. What does the function zip() do?

One of the less common functions with beginners, zip() returns an iterator of tuples.

Here, it pairs items from the two lists and creates tuples with those. But it doesn’t have to be lists.

Q.46. How do you calculate the length of a string?

This is simple. We call the function len() on the string we want to calculate the length of.

Q.47. Explain Python List Comprehension.

The list comprehension in python is a way to declare a list in one line of code. Let’s take a look at one such example.

Q.48. How do you get all values from a Python dictionary?

We saw previously, to get all keys from a dictionary, we make a call to the keys() method. Similarly, for values, we use the method values().

Q.49. What if you want to toggle case for a Python string?

We have the swapcase() method from the str class to do just that.

Q.54. What is a control flow statement?

A Python program usually starts to execute from the first line. From there, it moves through each statement just once and as soon as it’s done with the last statement, it transactions the program. However, sometimes, we may want to take a more twisted path through the code. Control flow statements let us disturb the normal execution flow of a program and bend it to our will.

Q.55. Create a new list to convert the following list of number strings to a list of numbers.

nums=[‘22’,’68’,’110’,’89’,’31’,’12’]

We will use the int() function with a list comprehension to convert these strings into integers and put them in a list.

Q.56. Given the first and last names of all employees in your firm, what data type will you use to store it?

I can use a dictionary to store that. It would be something like this-

Q.57.  How would you work with numbers other than those in the decimal number system?

With Python, it is possible to type numbers in binary, octal, and hexadecimal.

Binary numbers are made of 0 and 1. To type in binary, we use the prefix 0b or 0B.

To convert a number into its binary form, we use bin().

Octal numbers may have digits from 0 to 7. We use the prefix 0o or 0O.

Hexadecimal numbers may have digits from 0 to 15. We use the prefix 0x or 0X.

Q.59.  How many arguments can the range() function take?

The range() function in Python can take up to 3 arguments. Let’s see this one by one.

a. One argument

When we pass only one argument, it takes it as the stop value. Here, the start value is 0, and the step value is +1.

b. Two arguments

When we pass two arguments, the first one is the start value, and the second is the stop value.

c. Three arguments

Here, the first argument is the start value, the second is the stop value, and the third is the step value.

Q.60. What is PEP 8?

PEP 8 is a coding convention that lets us write more readable code. In other words, it is a set of recommendations.

Q.61. How is Python different from Java?

Following is the comparison of Python vs Java –

Java is faster than Python
Python mandates indentation. Java needs braces.
Python is dynamically-typed; Java is statically typed.
Python is simple and concise; Java is verbose
Python is interpreted
Java is platform-independent
Java has stronger database-access with JDBC

Q.62. What is the best code you can write to swap two numbers?

I can perform the swapping in one statement.

Q.63. How can you declare multiple assignments in one statement?

This is one of the most asked interview questions for Python freshers –

There are two ways to do this:

First – 

>>> a,b,c=3,4,5 #This assigns 3, 4, and 5 to a, b, and c respectively
Second – 

>>> a=b=c=3 #This assigns 3 to a, b, and c

Q.64. If you are ever stuck in an infinite loop, how will you break out of it?

For this, we press Ctrl+C. This interrupts the execution. Let’s create an infinite loop to demonstrate this.


Q.65. How do we execute Python?

Python files first compile to bytecode. Then, the host executes them.

Q.66. Explain Python’s parameter-passing mechanism.

To pass its parameters to a function, Python uses pass-by-reference. If you change a parameter within a function, the change reflects in the calling function. This is its default behavior. However, when we pass literal arguments like strings, numbers, or tuples, they pass by value. This is because they are immutable.

Q.69. What makes Python object-oriented?

Again the frequently asked Python Interview Question

Python is object-oriented because it follows the Object-Oriented programming paradigm. This is a paradigm that revolves around classes and their instances (objects). With this kind of programming, we have the following features:

Encapsulation
Abstraction
Inheritance
Polymorphism
Data hiding

Q.70. How many types of objects does Python support?

Objects in Python are mutable and immutable. Let’s talk about these.

Immutable objects- Those which do not let us modify their contents. Examples of these will be tuples, booleans, strings, integers, floats, and complexes. Iterations on such objects are faster.

Mutable objects – Those that let you modify their contents. Examples of these are lists, sets, and dicts. Iterations on such objects are slower.

Q.71 Why do you want to work for this company?

Q.72 Where do you see yourself in 10 years?

Q.73 What will you bring to the table if we hire you?

Q.74 Tell me about your best personal project. What challenges did you face, and how did it change the way you work?

Q.75 Would you have a problem with menial tasks?

Q.76 What makes you like Python over other languages? (The most commonly asked Python interview questions)

