# Map-Reduce implementation to generate word histograms from text files
## About
This project is a map-reduce algorithm implementation to generate word histograms from text files.

Python multiprocessing is implemented during the mapping phase and the file loading is done by chunks so that large data files can be loaded.

> Python 2.7 is required

## Installation
Simply clone the repository by:

``git clone https://github.com/alsis5/map_reduce.git``

To run it, type e.g.

``python mapreduce.py sample_inputs/quijote.txt``

Program also supports opening multiple files, just concatenate them on the command line.

## Letter histogram and joining multiple file results
Since version 1.3.0 you can now use these two features. To generate a character histogram simply run the program with ``-l`` flag. If you want to join the results from multiple files you just have to use the ``-j`` flag in the command line.

e.g:
> ``python mapreduce.py -l sample_inputs/quijote.txt``
>
> Will show the letter count of "El Quijote"

or

> ``python mapreduce.py -j sample_inputs/quijote.txt sample_inputs/lorem_50p_4464words.txt``
>
> Will show the word count of "El Quijote" plus 50 paragraphs of Lorem Ipsum

Both features **can be combined together**.
