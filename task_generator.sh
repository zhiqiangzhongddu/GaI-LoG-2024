#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

## Print commands and their arguments as they are executed
#set -x

# List of algorithms and tasks
#algorithms=("er" "ba" "sbm" "sfn" "complete" "star" "path")
algorithms=("er")

#tasks=(
#  "edge_existence" "node_degree" "node_count" "edge_count"
#  "connected_nodes" "cycle_check" "disconnected_nodes" "reachability"
#  "shortest_path" "maximum_flow" "triangle_counting"
#)
tasks=(
  "shortest_path" "triangle_counting"
)

text_encoders=(
  "adjacency" "incident"
)
cots=("True" "False")
bags=("True" "False")

# Loop over each algorithm
for algorithm in "${algorithms[@]}"; do
  # Loop over each task
  for task in "${tasks[@]}"; do
    for cot in "${cots[@]}"; do
      for bag in "${bags[@]}"; do
        for text_encoder in "${text_encoders[@]}"; do
          # Execute the Python script with the current algorithm and task
          python -m code.task_generator graph.algorithm "$algorithm" task.name "$task" task.cot "$cot" task.bag "$bag" task.text_encoder "$text_encoder"
        done
      done
    done
  done
done
