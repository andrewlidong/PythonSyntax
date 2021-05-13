Notes from: https://data-flair.training/blogs/python-programming-interview-questions/

Q.8. What do you mean by *args and **kwargs?

In cases when we don’t know how many arguments will be passed to a function, like when we want to pass a list or a tuple of values, we use *args.

**kwargs takes keyword arguments when we don’t know how many there will be.

Q.9. What is a closure in Python?

A closure in Python is said to occur when a nested function references a value in its enclosing scope. The whole point here is that it remembers the value.

Q.14. What is a frozen set in Python?

First, let’s discuss what a set is. A set is a collection of items, where there cannot be any duplicates. A set is also unordered.

However, a set is mutable. A frozen set is immutable. This means we cannot change its values. This also makes it eligible to be used as a key for a dictionary.

Q.15. When you exit Python, is all memory deallocated?

Exiting Python deallocates everything except:

modules with circular references
Objects referenced from global namespaces
Parts of memory reserved by the C library
Q.19. What is JSON? Describe in brief how you’d convert JSON data into Python data?

JSON stands for JavaScript Object Notation. It is a highly popular data format, and it stores data into NoSQL databases. JSON is generally built on the following two structures:

A collection of <name,value> pairs
An ordered list of values.
Python supports JSON parsers. In fact, JSON-based data is internally represented as a dictionary in Python. To convert JSON data into Python data, we use the load() function from the JSON module.

Q.22. Whenever you exit Python, is all memory de-allocated?

The answer here is no. The modules with circular references to other objects, or to objects referenced from global namespaces, aren’t always freed on exiting Python.

Plus, it is impossible to de-allocate portions of memory reserved by the C library.

Q.23. Can I dynamically load a module in Python?

Dynamic loading is where we do not load a module till we need it. This is slow, but lets us utilize the memory more efficiently. In Python, you can use the importlib module for this:

Q.28. Can you explain the filter(), map(), and reduce() functions?

Let’s see these Python Functions.

filter()- This function lets us keep the values that satisfy some conditional logic. Let’s take an example.

map()- This function applies a function to each element in the iterable.

This calculates the cube for each element in the range 0 to 6 and stores them in a set.

reduce()- This function reduces a sequence pair-wise, repeatedly until we arrive at a single value.

Q.37. What is monkey patching?

Dynamically modifying a class or module at run-time.

Q.43. Is Python call-by-value or call-by-reference? 

Python is neither call-by-value, nor call-by-reference. It is call-by-object-reference. Almost everything is an object in Python. Take this example:

Q.50. How would you perform unit-testing on your Python code?

For this purpose, we have the module unittest in Python. It has the following members:

FunctionTestCase
SkipTest
TestCase
TestLoader
TestResult
TestSuite
TextTestResult
TextTestRunner
defaultTestLoader
expectedFailure
findTestCases
getTestCaseNames
installHandler
main
makeSuite
registerResult
removeHandler
removeResult
skip
skipIf
skipUnless
Q.51. What is unit testing? How will you do it in Python?

This is the first level of software testing, and it focuses on testing individual units of source code. This is to make sure everything works as expected. A unit is the smallest testable part of a software and usually comprises of a few inputs and a single output.

For this, we have the unittest framework. This was inspired by the JUnit framework and offers support for test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of tests from the framework. unittest is about text fixtures, text cases, test suites, and test runners.


Q.53. Differentiate between Django, Pyramid, and Flask.

We can also use Django for larger applications. It includes an ORM.
Flask is a microframework for a small platform with simpler requirements. It is ready to use and you must use external libraries.
The pyramid is for larger applications. It is flexible and you can choose the database, the URL structure, the templating style, and much more. It is also heavily configurable.


Q.54. Explain the Inheritance Styles in Django.

Talking on inheritance styles, we have three possible-

Abstract Base Classes- For the parent class to hold information so we don’t have to type it out for each child model
Multi-table Inheritance- For subclassing an existing model and letting each model have its own database
Proxy Models- For modifying the model’s Python-level behavior without having to change its fields
Q.55. What is Flask- WTF? Explain its features.

Flask-WTF supports simple integration with WTForms. It has the following features-

Integration with wtforms
Global csrf protection
Recaptcha supporting
Internationalization integration
Secure form with csrf token
File upload compatible with Flask uploads
Q.56. What is Flask?

Python Flask, as we’ve previously discussed, is a web microframework for Python. It is based on the ‘Werkzeug, Jinja 2 and good intentions’ BSD license. Two of its dependencies are Werkzeug and Jinja2. This means it has around no dependencies on external libraries. Due to this, we can call it a light framework.

A session uses a signed cookie to allow the user to look at and modify session contents. It will remember information from one request to another.
However, to modify a session, the user must have the secret key Flask.secret_key.

Is there any question in this section which you are not able to answer? If yes, then you need to revise the concepts of frameworks for cracking the next Python coding interview.



Q.65. If a function does not have a return statement, is it valid?

Very conveniently. A function that doesn’t return anything returns a None object. Not necessarily does the return keyword mark the end of a function; it merely ends it when present in the function. Normally, a block of code marks a function and where it ends, the function body ends.

