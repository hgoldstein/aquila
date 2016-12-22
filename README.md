# Aquila
Automatically build and serve [reveal.js](https://github.com/hakimel/reveal.js/) presentations using [docker](https://github.com/docker/docker).

## Features
* PDF export
* [Graphviz](http://www.graphviz.org/) support (using [viz.js](https://github.com/mdaines/viz.js/))
* [MathJax](https://www.mathjax.org/) support
* [Asciinema](https://asciinema.org/) support
* Generates HTML automatically from a configuration file

## Dependencies
Aquila runs almost everything inside a docker container and uses bash and python
scripts to launch docker. All you need to run Aquila is:
* Bash
* Python 3
* Docker

## Usage
* `serve path/to/presentation`: serves the presentation at `localhost:8000`. Probably the
only command you'll need.
* `pdf path/to/presentation`: exports the presentation as a PDF file named `index.pdf` in
the directory with the presentation.
* `setup`: builds the docker image. `server` builds the image as needed, so you shouldn't have
to call this manually.
* `enter path/to/presentation`: launches an interactive shell in the docker image with the
specified presentation mounted. Used for debugging.

All commands are in the [`bin`](bin) folder.

## Markdown Syntax
### Graphs
Embed graphs within code blocks by setting the language to `graph`:
<pre lang="no-highlight"><code>```graph
graph {
  Hello -> World;
}
```
</code></pre>


See the Graphviz documentation for the synatax for making graphs:
* http://www.graphviz.org/doc/info/attrs.html
* http://www.graphviz.org/doc/info/lang.html

### Math
Inline math is delimited by `\(..\)`. Display math is delimited by `\[..\]`
or `$$..$$`. Uses LaTeX syntax. See [example/math.md](example/math.md)

## Example
The [example](example) folder contains a working example presentation with Graphviz
graphs and LaTeX equations! Run:
```bash
$ bin/serve example
```
Then, open [http://localhost:8000](http://localhost:8000) in a web browser to view
the presentation.

The example presentation has of three sections, each in a markdown file:

1. `graph.md`
1. `math.md`
1. `table.md`

It also has a title in the `title.md` file. The `config.json` file describes the
presentation's structure:
```json
{
  "presentation" : "example presentation",
  "styles" : ["css/theme/cmr.css"],
  "title" : "title.md",
  "slides" : ["graph.md", "math.md", "table.md"]
}
```
Each field in `config.json` defines a part of the presentation:
* `presentation`: the title of the presentation (shows up at in the web browser's
title bar)
* `styles`: defines an stylesheets to use in the presentation. The example presentation
uses `css/cmr/cmr.css` to change some of the default colors and font sizes.
* `title`: the markdown file which contains the title slide.
* `slides`: the rest of the markdown files in the order they should be displayed.

## Screencast
<script type="text/javascript" src="https://asciinema.org/a/bcdmrv8e8xrcdjmmvxihe4p05.js" id="asciicast-bcdmrv8e8xrcdjmmvxihe4p05" async></script>

## Contributing
Coming soon!
