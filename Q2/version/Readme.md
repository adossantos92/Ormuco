## version Library

# Install 

To install the package, simply execute:

`python setup.py install`

# Test

To test the package, simply execute:

`pytest -v`

# Usage

This library implements an object Class called Version with buil-in comparators.
To compare two version, initialise two Version objects with their respective version number (as string).
You can then compare them as you would compare any other integers, floats, etc...

*Example:*

~~~~
from version.version import Version


a = Version('1.2.01')
b = Version('1.2.1')

assert a < b
~~~~
 