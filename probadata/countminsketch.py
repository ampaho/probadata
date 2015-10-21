from __future__ import absolute_import

from probadata.utils import is_python_3, count_min_sketch_hash

import array

__version__ = '0.0.1'
__author__  = "Olalekan H. ABOU BAKAR <houdan@jolome.com>"

class CountMinSketch(object):
    """
    A class for counting hashable items using the Count-min Sketch strategy.
    It fulfills a similar purpose than `itertools.Counter`.
    The Count-min Sketch is a randomized data structure that uses a constant
    amount of memory and has constant insertion and lookup times at the cost
    of an arbitrarily small overestimation of the counts.
    It has two parameters:
     - `m` the size of the hash tables, larger implies smaller overestimation
     - `d` the amount of hash tables, larger implies lower probability of
           overestimation.
    An example usage:
        from countminsketch import CountMinSketch
        sketch = CountMinSketch(1000, 10)  # m=1000, d=10
        sketch.add("oh yeah")
        sketch.add(tuple())
        sketch.add(1, value=123)
        print sketch["oh yeah"]       # prints 1
        print sketch[tuple()]         # prints 1
        print sketch[1]               # prints 123
        print sketch["non-existent"]  # prints 0
    Note that this class can be used to count *any* hashable type, so it's
    possible to "count apples" and then "ask for oranges". Validation is up to
    the user.
    """

    def __init__(self, m, d):
        """ `m` is the size of the hash tables, larger implies smaller
        overestimation. `d` the amount of hash tables, larger implies lower
        probability of overestimation.
        """
        if not m or not d:
            raise ValueError("Table size (m) and amount of hash functions (d)"
                             " must be non-zero")
        self.m = m
        self.d = d
        self.n = 0
        self.tables = []
        
        #num_slices = int(ceil(log(1.0 / error_rate, 2)))
        #bits_per_slice = int(ceil(
        #    (capacity * abs(log(error_rate))) /
        #    (num_slices * (log(2) ** 2))))
        
        
        for _ in xrange(d):
            table = array.array("l", (0 for _ in xrange(m)))
            self.tables.append(table)

    def add(self, x, value=1):
        """
        Count element `x` as if had appeared `value` times.
        By default `value=1` so:
            sketch.add(x)
        Effectively counts `x` as occurring once.
        """
        self.n += value
        for table, i in zip(self.tables, count_min_sketch_hash(x, self.m, self.d)):
            table[i] += value

    def query(self, x):
        """
        Return an estimation of the amount of times `x` has ocurred.
        The returned value always overestimates the real value.
        """
        return min(table[i] for table, i in zip(self.tables, count_min_sketch_hash(x, self.m, self.d)))

    def __getitem__(self, x):
        """
        A convenience method to call `query`.
        """
        return self.query(x)

    def __len__(self):
        """
        The amount of things counted. Takes into account that the `value`
        argument of `add` might be different from 1.
        """
        return self.n