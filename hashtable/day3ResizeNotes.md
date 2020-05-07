Lots of collisions:

0 |-> D -> M -> Q
1 |-> H
2 |-> A -> I
3 |-> C -> J -> L -> N
4 |-> G 
5 |-> B -> O
6 |-> E -> K -> P
7 |-> F

Load Factor
-----------

  number of elements in the list
  ------------------------------
         number of slots


  17
----- = 2.125  "really bad"
  8

1.0 = exactly full
0.5 = half full
0.0 = empty


Resize
------

Step 1: make a new, bigger table/array
Step 2: go through all the old elements, and hash into the new list

Rule of thumb:
If you resize bigger, double the size
If you resize smaller, halve the size



Existing table:
0 |-> D -> M -> Q
1 |-> H
2 |-> A -> I
3 |-> C -> J -> L -> N
4 |-> G 
5 |-> B -> O
6 |-> E -> K -> P
7 |-> F

New table:
0 |
1 |
2 | -> D
3 |
4 |
5 | -> Q
6 |
7 |
8 |
9 | -> M
10|
11|
12|
13|
14|
15|

Automatic resizing
------------------

When you put(): 
	if the load > 0.7:
		double the size of the hashtable

When you delete():
	if the load < 0.2:
		if size > minimum (8):
			halve the size of the hashtable down (to the minimum, at most)


