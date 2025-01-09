# Collections in Python:

#     Python provides several built-in collection types that are used to store and manage groups of data. Here are the most commonly used collections:

# Lists:
#     Ordered, mutable, and allows duplicate elements.
#     Example: my_list = [1, 2, 3, 4]

# Tuples:
#     Ordered, immutable, and allows duplicate elements.
#     Example: my_tuple = (1, 2, 3, 4)

# Sets:
#     Unordered, mutable, and does not allow duplicate elements.
#     Example: my_set = {1, 2, 3, 4}

# Dictionaries:
#     Unordered, mutable, and stores key-value pairs. Keys must be unique.
#     Example: my_dict = {'key1': 'value1', 'key2': 'value2'}


#     --Other collection--

# Strings:
#     Ordered, immutable, and stores sequences of characters.
#     Example: my_string = "Hello, World!"

# Frozensets:
#     Unordered, immutable version of a set.
#     Example: my_frozenset = frozenset([1, 2, 3, 4])

# Deques (from collections module):
#     Double-ended queue, optimized for fast appends and pops from both ends.
#     Example: from collections import deque; my_deque = deque([1, 2, 3])

# Named Tuples (from collections module):
#     Immutable and named fields, similar to a lightweight object.
#     Example: from collections import namedtuple; Point = namedtuple('Point', ['x', 'y']); p = Point(1, 2)

# Counters (from collections module):
#     A dictionary subclass for counting hashable objects.
#     Example: from collections import Counter; my_counter = Counter([1, 1, 2, 3])

# OrderedDict (from collections module):
#     A dictionary subclass that remembers the order entries were added.
#     Example: from collections import OrderedDict; my_ordered_dict = OrderedDict([('a', 1), ('b', 2)])

# Defaultdict (from collections module):
#     A dictionary subclass that provides default values for missing keys.
#     Example: from collections import defaultdict; my_defaultdict = defaultdict(int); my_defaultdict['key'] += 1


# These collections are part of Python's standard library and are widely used for various data manipulation tasks.