README
======

The `sample-n-files` command randomly selects `N` files from a source directory, printing the names and/or copying to a destination directory.

It requires Python 3 (tested with 3.6.5).

The build procedure creates a [pex](https://pex.readthedocs.io/en/stable/),
which embeds all the dependencies in a single executable, and that can then be installed wherever you see fit.

## Building and installing

To build:

```bash
$ make build
```

To install:

```bash
$ make install
```

## Using

```bash
$ sample-n-files --help
Usage: sample_n_files [OPTIONS] SRC DST

  Sample `count` files, copying them from `src` to `dst`

Options:
  --count INTEGER      Number of file to sample.
  --prefix TEXT        Prefix of the files to consider
  --printonly BOOLEAN  Print only instead of copying
  --verbose BOOLEAN    Be verbose
  --help               Show this message and exit.

$ sample-n-files --count 25 --prefix "dog" --verbose yes cat_vs_dog/ dogs_selection/
...
```
