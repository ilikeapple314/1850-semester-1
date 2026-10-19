
# set.intersection() method

Look up documentation on the 'intersection()' method
- how is the method described? Intersection essentially works like an AND in logic it finds the items which are in common between two sets and returns them.
- what are the inputs? two sets can be input into this method as set1.intersection(set2)
- what is the output? the output is a whole new subset containing the items found in set1 and set2
- think about the description of the data and also the type - in this case it will all be sets the values within the sets could be anything however.

Write a small program to test the method

set1 = {potato, ant, angry}
set2 = {maths, poster, law, ant}

subset = set1.intersection(set2)

subset == {ant}