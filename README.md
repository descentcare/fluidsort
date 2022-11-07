# Fluidsort
Fluid sort terminal game written in python

![](./demo.gif)

# Requirements
python3

# Usage
1. `$ ./game.py` or `$ python3 game.py`
2. input how much fluid you want in every cup
3. input keys that you will use to choose cups(at least 3 unique keys without spaces)
for example, I use *qwerasdf*
4. Play the game! To make a move, input 2 letters(sourse of fluid then destination). To pour from or to a cup with empty name - use space.
the goal is to sort letters so in the end there will be no cup with 2 or more types of letters

5. Have fun!

# Example

From this position:
```
 [q]  [w]  [e]  [r]  [ ] 

 [r]  [ ]  [q]  [ ]  [w] 
 [r]  [r]  [e]  [ ]  [q] 
 [r]  [q]  [e]  [ ]  [w] 
 [w]  [e]  [q]  [w]  [e] 
```
input `qw` to move fluid form `q` to `w` cup
The result will be:
```
 [q]  [w]  [e]  [r]  [ ] 

 [ ]  [r]  [q]  [ ]  [w] 
 [r]  [r]  [e]  [ ]  [q] 
 [r]  [q]  [e]  [ ]  [w] 
 [w]  [e]  [q]  [w]  [e] 
```
To pour from ` ` to `r` input ` r`
The result will be:
```
 [q]  [w]  [e]  [r]  [ ] 

 [ ]  [r]  [q]  [ ]  [ ] 
 [r]  [r]  [e]  [ ]  [q] 
 [r]  [q]  [e]  [w]  [w] 
 [w]  [e]  [q]  [w]  [e] 
```
The winning position could look like this:
```
 [q]  [w]  [e]  [r]  [ ] 

 [w]  [ ]  [ ]  [r]  [e] 
 [w]  [q]  [ ]  [r]  [e] 
 [w]  [q]  [ ]  [r]  [e] 
 [w]  [q]  [q]  [r]  [e] 
```
