# Cherry

Cherry is a general purpose genetic algorithm. This small module lets you to apply genetic optimization to arbitrary problems.

```py
from cherry import cherry

problem = lambda x: x ** 2 # we want to minimize this function

solutions = cherry(fitness = problem, ...)
```


## parameters

### `fitness: Function`

The function you want to minimize. This function should take an instance of the object you're trying to optimize and return how "fit" that instance is.

### `animal: Function`

A function which returns a **random** instance of the object you're trying to optimize. For example, if you were simply trying to find real valued roots of a curve, then
`animal` would typically return a random float within an interval.

### `cross: Function` 

A crossover operator. This function should take two instance of the target object and return a new instance. The idea is for the new object to share features of both parents.

### `mutate: Function`

A mutation operator. This function should take an instance of the target object and return a new instance which differs in small and random ways.

### `parents: Integer`

The number of parents used for the initial population. A reasonable size is 200.

### `children: Integer`

The number of children generated each generation. This should be smaller than `parents`.

### `rounds: Integer`

How many generations the algorithm should run for.
