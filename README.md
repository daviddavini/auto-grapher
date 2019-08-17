# Auto-Grapher
A Python program that auto-generates bidirected graphs, provided a function specifying node-to-node connections.

<div>
<img src="https://user-images.githubusercontent.com/22968625/63206296-beb15280-c066-11e9-868d-c59a51440ccb.jpeg" 
height="600" class="center">

**Top**: Progression showing the process that the program goes through, starting with a random layout of the graph and 
gradually unfolding until it finds its optimal structure.
**Bottom Right**: Graph of f(x)=x^2 (mod 85).
**Bottom Left**: Graph of f(x)=x^2 (mod 86).
</div>

<img src="https://user-images.githubusercontent.com/22968625/63206296-beb15280-c066-11e9-868d-c59a51440ccb.jpeg" 
height="600" class="center" hspace="10">

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