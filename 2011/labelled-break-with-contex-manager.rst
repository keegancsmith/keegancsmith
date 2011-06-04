:Date: 2011-06-04 18:30:00

=================================================
 Labelled Breaks in Python with Context Managers
=================================================

A friend of mine who codes in Java a lot was lamenting the fact that Python
does not support labelled breaks. Labelled breaks are useful when you have
nested loops and want to break out of the outer loop based on a condition in
an inner loop.

For example say we had a list of lists containing numbers

.. code-block:: python

   import random
   lists = [[random.randint(0, 100) for i in range(10)] for i in range(10)]

We then want to check if the number 42 is in any of the lists

.. code-block:: python

   found = False
   for li in lists:
       for val in li:
           if val == 42:
               found = True
               break
       if found:
           break

For the purpose of illustration we use nested for loops instead of something
like

.. code-block:: python

   found = any(42 in li for li in lists)

The two for loops are a simple example, but in more complicated examples we
may have extremely nested loops. This usually calls for some refactoring into
classes/function, but with labelled breaks we can keep a clean code
structure. For example in Java we could write this as

.. code-block:: java

   // int lists[][] = something;
   boolean found = false;

   search:
   for (i = 0; i < lists.length; i++) {
       for (j = 0; j < lists[i].length; j++) {
           if (lists[i][j] == 42) {
               found = true;
               break search;
           }
       }
   }

There is `PEP 3136 <http://www.python.org/dev/peps/pep-3136/>`_ which proposed
labelled breaks for Python, but that was rejected. Luckily Python 2.5
introduced context managers, which give us a way to hack in labelled breaks.

.. code-block:: python

   class Label(object):
       class __break(Exception):
           def __init__(self, ctx):
               self.ctx = ctx

       def __enter__(self):
           return self

       def __exit__(self, exc_type, exc_val, exc_tb):
           return isinstance(exc_val, self.__break) and exc_val.ctx is self

       def break_(self):
           raise self.__break(self)

When a context manager's block has finished executing, the __exit__ method is
called. It is passed exception info (or None if it exited without
exception). When the block is exiting due to an exception Python will look at
the return value of __exit__. If the __exit__ method returns True the
exception is not reraised. If __exit__ returns something else then the
exception is reraised.

So we can simulate labelled breaks using exceptions and context managers. In
the above code the __exit__ method returns True only when the exception passed
is one thrown from its instance of break\_. We can now write our search code
with labelled breaks:

.. code-block:: python

   found = False
   with Label() as search:
    for li in lists:
        for val in li:
            if val == 42:
                found = True
                search.break_()
