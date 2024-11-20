#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

## Print commands and their arguments as they are executed
#set -x

# List of algorithms and tasks
algorithms=("er" "ba" "sbm" "sfn" "complete" "star" "path")

# Loop over each algorithm
for algorithm in "${algorithms[@]}"; do
  python -m code.image_generator graph.algorithm "$algorithm"
done
