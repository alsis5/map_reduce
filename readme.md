# Map-Reduce aproach to generate word histograms from text files
## About
This project is a map-reduce algorithm aproach to generate word histograms from text files.

Python multiprocessing is implemented during the mapping phase and the file loading is done by chunks so that large data files can be loaded.

> Python 2.7 is required

## Installation
Simply clone the repository by:

``git clone https://github.com/alsis5/map_reduce.git``

To run it, type e.g.

``python mapreduce.py sample_inputs/quijote.txt``

Program also supports opening multiple files, just concatenate them on the command line.
