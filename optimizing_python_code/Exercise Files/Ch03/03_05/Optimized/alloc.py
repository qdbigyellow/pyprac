"""Fixed list allocation"""


def allocz(size):
    """Alloc zeros with range"""
    # When create a list and append to it, python need reallocate for the list.
    # The list grows in fixed sized, 0 , 4, 16, 64, 256.... 
    return [0 for _ in range(size)]


def allocz_fixed(size):
    """Alloc zeros with *"""
    # Create a list in muplication,, python knows the size, create the list in one allocation.
    # The initial value is duplicated, in Python, everything is a reference, this has a suprising effect. 
    # e.g
    # In [32]: arr = [[]] * 6
    # In [33]: arr[0].append(1)
    # In [34]: arr
    # Out[34]: [[1], [1], [1], [1], [1], [1]]    # Everything refer to the first element.

    # If knows the size in advance, consider to use 
    # Either 1)  Fix allocation
    # or     2)  numpy:     e.g  numpy.zeros(1000)
    return [0] * size
