# Python-Pathfinder

A pathfinding algorithm I designed completely by myself using Python!
### Note: 
This is NOT a shortest pathfinding algorithm, just a correct path. I am working on finding the shortest path, and hope to add it soon.

## USAGE:

### Input:
The map is stored in file called *map.txt* stored in the same directory as *main.py*. The walls can be made with any character, preferably # or █, but the paths have to be whitespaces. The start and end points are denoted by O and X respectively. 

To easily make mazes, you can use https://www.dcode.fr/maze-generator. Make sure that the *Path Design* option is set to empty space and *Display* option is set to single character.

The *Samples* folder contains various sample maps with different sizes and designs. If using them, make sure to drag the file to the root directory and rename it to *map.txt*. Feel free to move the start and end points to see different paths formed.

### Output:
There are two ways in which a suitable output can be recieved:
  1. In the form of steps taken
  2. In the form of a completed map (Prefered for larger maps)

#### Steps taken:
At the end, use the statement: ```print(final)``` to get a series on moves leading from start to finish.
<img width="1137" alt="Screen Shot 2022-03-19 at 12 46 28 PM" src="https://user-images.githubusercontent.com/75612147/159114366-67234699-3063-40a4-83f8-f0318ccb9167.png">

#### Completed map:
At the end, use the statement: ```print("\n".join(map))``` to get a completed map with the path highlighted.

<img width="122" alt="Screen Shot 2022-03-19 at 12 48 14 PM" src="https://user-images.githubusercontent.com/75612147/159114395-0a106bf1-6346-4075-9b15-c10325a4da17.png">
