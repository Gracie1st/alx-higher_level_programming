doctest — Testing Through Documentation

Purpose:	Write automated tests as part of the documentation for a module.

doctest tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. Many developers find doctest easier to use than unittest because, in its simplest form, there is no API to learn before using it. However, as the examples become more complex the lack of fixture management can make writing doctest tests more cumbersome than using unittest.



Getting Started

The first step to setting up doctests is to use the interactive interpreter to create examples and then copy and paste them into the docstrings in the module. Here, my_function() has two examples given:



doctest_simple.py

def my_function(a, b):

    """

    >>> my_function(2, 3)

    6

    >>> my_function('a', 3)

    'aaa'

    """

    return a * b

To run the tests, use doctest as the main program via the -m option. Usually no output is produced while the tests are running, so the next example includes the -v option to make the output more verbose.



$ python3 -m doctest -v doctest_simple.py



Trying:

    my_function(2, 3)

Expecting:

    6

ok

Trying:

    my_function('a', 3)

Expecting:

    'aaa'

ok

1 items had no tests:

    doctest_simple

1 items passed all tests:

   2 tests in doctest_simple.my_function

2 tests in 2 items.

2 passed and 0 failed.

Test passed.

Examples cannot usually stand on their own as explanations of a function, so doctest also allows for surrounding text. It looks for lines beginning with the interpreter prompt (>>>) to find the beginning of a test case, and the case is ended by a blank line or by the next interpreter prompt. Intervening text is ignored, and can have any format as long as it does not look like a test case.



doctest_simple_with_docs.py

def my_function(a, b):

    """Returns a * b.



    Works with numbers:



    >>> my_function(2, 3)

    6



    and strings:



    >>> my_function('a', 3)

    'aaa'

    """

    return a * b

The surrounding text in the updated docstring makes it more useful to a human reader. Because it is ignored by doctest, the results are the same.



$ python3 -m doctest -v doctest_simple_with_docs.py



Trying:

    my_function(2, 3)

Expecting:

    6

ok

Trying:

    my_function('a', 3)

Expecting:

    'aaa'

ok

1 items had no tests:

    doctest_simple_with_docs

1 items passed all tests:

   2 tests in doctest_simple_with_docs.my_function

2 tests in 2 items.

2 passed and 0 failed.

Test passed.

Handling Unpredictable Output

There are other cases where the exact output may not be predictable, but should still be testable. For example, local date and time values and object ids change on every test run, the default precision used in the representation of floating point values depend on compiler options, and string representations of container objects like dictionaries may not be deterministic. Although these conditions cannot be controlled, there are techniques for dealing with them.



For example, in CPython, object identifiers are based on the memory address of the data structure holding the object.



doctest_unpredictable.py

class MyClass:

    pass





def unpredictable(obj):

    """Returns a new list containing obj.



    >>> unpredictable(MyClass())

    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]

    """

    return [obj]

These id values change each time a program runs, because it is loaded into a different part of memory.



$ python3 -m doctest -v doctest_unpredictable.py



Trying:

    unpredictable(MyClass())

Expecting:

    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]

****************************************************************

File ".../doctest_unpredictable.py", line 17, in doctest_unpredi

ctable.unpredictable

Failed example:

    unpredictable(MyClass())

Expected:

    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]

Got:

    [<doctest_unpredictable.MyClass object at 0x1047a2710>]

2 items had no tests:

    doctest_unpredictable

    doctest_unpredictable.MyClass

****************************************************************

1 items had failures:

   1 of   1 in doctest_unpredictable.unpredictable

1 tests in 3 items.

0 passed and 1 failed.

***Test Failed*** 1 failures.

When the tests include values that are likely to change in unpredictable ways, and where the actual value is not important to the test results, use the ELLIPSIS option to tell doctest to ignore portions of the verification value.



doctest_ellipsis.py

class MyClass:

    pass





def unpredictable(obj):

    """Returns a new list containing obj.



    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS

    [<doctest_ellipsis.MyClass object at 0x...>]

    """

    return [obj]

The “#doctest: +ELLIPSIS” comment after the call to unpredictable() tells doctest to turn on the ELLIPSIS option for that test. The ... replaces the memory address in the object id, so that portion of the expected value is ignored and the actual output matches and the test passes.



$ python3 -m doctest -v doctest_ellipsis.py



Trying:

    unpredictable(MyClass()) #doctest: +ELLIPSIS

Expecting:

    [<doctest_ellipsis.MyClass object at 0x...>]

ok

2 items had no tests:

    doctest_ellipsis

    doctest_ellipsis.MyClass

1 items passed all tests:

   1 tests in doctest_ellipsis.unpredictable

1 tests in 3 items.

1 passed and 0 failed.

Test passed.

There are cases where the unpredictable value cannot be ignored, because that would make the test incomplete or inaccurate. For example, simple tests quickly become more complex when dealing with data types whose string representations are inconsistent. The string form of a dictionary, for example, may change based on the order the keys are added.



doctest_hashed_values.py

keys = ['a', 'aa', 'aaa']



print('dict:', {k: len(k) for k in keys})

print('set :', set(keys))

Because of hash randomization and key collision, the internal key list order may be different for the dictionary each time the script runs. Sets use the same hashing algorithm, and exhibit the same behavior.



$ python3 doctest_hashed_values.py



dict: {'aa': 2, 'a': 1, 'aaa': 3}

set : {'aa', 'a', 'aaa'}



$ python3 doctest_hashed_values.py



dict: {'a': 1, 'aa': 2, 'aaa': 3}

set : {'a', 'aa', 'aaa'}

The best way to deal with these potential discrepancies is to create tests that produce values that are not likely to change. In the case of dictionaries and sets, that might mean looking for specific keys individually, generating a sorted list of the contents of the data structure, or comparing against a literal value for equality instead of depending on the string representation.



doctest_hashed_values_tests.py

import collections





def group_by_length(words):

    """Returns a dictionary grouping words into sets by length.



    >>> grouped = group_by_length([ 'python', 'module', 'of',

    ... 'the', 'week' ])

    >>> grouped == { 2:set(['of']),

    ...              3:set(['the']),

    ...              4:set(['week']),

    ...              6:set(['python', 'module']),

    ...              }

    True



    """

    d = collections.defaultdict(set)

    for word in words:

        d[len(word)].add(word)

    return d
