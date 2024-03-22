# Coordinate-Combinations

Simple script that will return a list of lists. Each returned list within the largest list contains a coordinate ranging from [0,0,0,...,0] to [a,b,c,...,n]. 

## To run
```
command: python coord-combination.py 
```
You will be prompted to enter in numbers to combine. The numbers entered are the largest coordinate.
```
Please input a list of numbers you would like combined:
```
## Output
For example, 
```
Please input a list of numbers you would like combined:

1 2 3
```
Will result in
```
The list of numbers entered: [1, 2, 3]
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 1, 3], [0, 2, 0], [0, 2, 1], [0, 2, 2], [0, 2, 3], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 0], [1, 2, 1], [1, 2, 2], [1, 2, 3]]
```
