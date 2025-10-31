# Import your packages, modules, global constants first
import self_py_fun.week_08_example_fun as ef
import numpy as np
# Notes from class on 10/17:
# You NEED to impact packages etc. at the beginning, or else PyCharm will give you an error.
# You can also import your OWN function(s).
# You have two options for importing function or packages
import self_py_fun.week_08_example_fun as ef2 # here, you'll need to specify .ef2 everytime you're calling the function. If you DON'T want to do that, try the next one
from self_py_fun.week_08_example_fun import* # using this import statement, you WON'T have to specify .ef2 everytime you're calling the function


# Call variables
print(ef.alpha)

# Call your functions
print(ef.message_hello('Tianwen'))
print(ef.fn_cubic(3))
print(np.array([1.0]))

# Whenever you write a customized function