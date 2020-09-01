# Menger Square

This project was inspired by [Menger Sponge](https://en.wikipedia.org/wiki/Menger_sponge).
I built this project for fun just to try and replicate the Menger Sponge behaior with pygame on a simple square.

## How it works

When you load start the program, pressing space will subdivide the square into 8 smaller squares (without the center one)
which produces the same look as a single side of the Menger Sponge.

![image](https://user-images.githubusercontent.com/20902250/91882556-6e159300-ec83-11ea-8831-9bf6e0bdd0b5.png)

The example image consists of 262,144 squares (6 iterations)
The number of squares grows by a factor of 8 on each iteration.

## Internal Code Structure

The code behind this is actually surprisingly simple

```py
squares = []
new_side = cube.side / 3
for i in [new_side, 0, -new_side]:
    for j in [new_side, 0, -new_side]:
        if i == 0 and j == 0:
            continue
        center = self.center + Vector(i, j)
        squares.append(Cube(center, new_side))
```

Here it's clear that for each square division this splits it into 8 smaller ones (omitting the center one) which is done in `O(n^2)` .

Apart from that everything else in the code is just to handle pygame drawing and some utility functions to make the development a little easier.
