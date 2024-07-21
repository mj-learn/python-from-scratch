# Note: Any module that is not part of the Python standard library must be installed separately.
# Use pip or conda to install the required packages.
# Example: `pip install package_name` or `conda install package_name`.

# basic import
import math  # this will import every thing from the module (bloated, not good to use)

# use it like this
some_number = math.ceil(55.46)

# from...import...
# All imports need to be on top of the file, NOT LIKE THIS!
# Not good practise to import everything and them import from same only something!
from random import *  # import everything, not good import style!
from random import choice  # import only choice not everything (this is correct style to import choice method)

# from...import... with many
from math import sqrt, pi, sin, cos, atan  # Style 1
from math import (  # Style 2
    sqrt,
    pi as p,  # with alias
    sin,
    cos,
)

# use it like this
random_choice = choice([1, 2, 3])
math_pi = p

# basic import with aliases
import turtle as t  # import as t and can use turtle module with alias "t"

# use it like this
tim = t.Turtle()

# from...import with aliases
from random import randrange as r, randint as i

some_range = r(1, 100)
random_integer = i(5, 50)
