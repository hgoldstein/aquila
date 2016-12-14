# aquila
Automatically build and serve reveal.js presentations using Docker.

# Running

* Generate an `index.html` using `bin/generate-index.py`
```bash
$ bin/generate-index.py example/example.json example/index.template \
  -o example/index.html
```
* Launch the `reveal.js` server
```bash
$ bin/serve example/
```
