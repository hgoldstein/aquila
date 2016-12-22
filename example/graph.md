# Graph
* You can include Graphviz diagrams in Aqualia presentations
* Put the `dot` graph in a code block labled with `graph`:
````markdown
```graph
graph {
  Hello -> World;
}
```
````


# Example
```graph
graph {
  layout="circo";
  bgcolor="transparent";
  node [color=white];
  node [fontcolor="white"];
  edge [color="white"];
  a -- b;
	b -- c;
	c -- d;
	d -- e;
	e -- f;
	a -- f;
	a -- c;
	a -- d;
	a -- e;
	b -- d;
	b -- e;
	b -- f;
	c -- e;
	c -- f;
	d -- f;
}
```
