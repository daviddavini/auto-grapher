# Auto-Grapher
A Python program that auto-generates bidirected graphs, provided a function specifying node-to-node connections. It accomplishes this by treating each node in the graph as a point mass and each line as a spring, and simulating the physical forces of drag and tension.

<div>
<img src="https://user-images.githubusercontent.com/22968625/63206296-beb15280-c066-11e9-868d-c59a51440ccb.jpeg" 
height="600" class="center">

**Top**: Progression showing the process that the program goes through, starting with a random layout of the graph and 
gradually unfolding until it finds its optimal structure.
**Bottom Right**: Graph of f(x)=x^2 (mod 85).
**Bottom Left**: Graph of f(x)=x^2 (mod 86).
</div>

<p align="center">
<img src="https://user-images.githubusercontent.com/22968625/63206552-6c266500-c06b-11e9-9430-7a214a055386.jpeg" 
height="600" class="center">
 </p>

## How to use it
```Python
run_graph(function, mod, name="graph", show=True, filename=-1, wait=False)
```
  * *function*: the function you want to graph \
  * *mod*: the size of the function's domain \
  * *name (optional)*: the title to display on the top of the image \
  * *show (optional)*: whether or not to display the unfolding process \
  * *filename (optional)*: if specified, will save the image to your computer \
  * *wait (optional)*: if True, will wait for a keypress to close the image \

### Example:
```Python
run_graph(lambda x: tetration(x, 2, 87), 87, name="graph")
```
<p align="center">
<img src="https://user-images.githubusercontent.com/22968625/63206598-c2e06e80-c06c-11e9-9b75-bab01290cf12.jpg" 
height="400" class="center">
</p>

Other parameters are available as global variables (for instance, setting do_numbers to True will cause the program to print numbers on top of the graph's nodes)
