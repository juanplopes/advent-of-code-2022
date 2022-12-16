#!/bin/bash
PYTHON_EXECUTABLE=pypy3
FILES=${1:-day*.py}

for f in $FILES
do
    echo "------------------"
    echo "Running $f"
    filename="${f%.*}"
    time $PYTHON_EXECUTABLE $f < in/$filename.in
done