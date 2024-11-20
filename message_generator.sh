#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

### Print commands and their arguments as they are executed
##set -x
#
## List of algorithms and tasks
##algorithms=("er" "ba" "sbm" "sfn" "complete" "star" "path")
#algorithms=("er")
##tasks=(
##  "edge_existence" "node_degree" "node_count" "edge_count"
##  "connected_nodes" "cycle_check" "disconnected_nodes" "reachability"
##  "shortest_path" "maximum_flow" "triangle_counting"
##)
#tasks=(
#  "shortest_path" "triangle_counting"
#)
##text_encoders=(
##  "adjacency" "incident" "coauthorship" "friendship" "south_park"
##  "got" "social_network" "politician" "expert"
##)
#text_encoders=(
#  "adjacency" "incident"
#)
#cots=("True" "False")
##cots=("True")
#bags=("True" "False")
##bags=("True")
#use_texts=("True" "False")
#use_images=("True" "False")
#types=("zero_shot" "few_shot")
##types=("few_shot")
#
## Loop over each algorithm
#for algorithm in "${algorithms[@]}"; do
#  # Loop over each task
#  for task in "${tasks[@]}"; do
#    for cot in "${cots[@]}"; do
#      for bag in "${bags[@]}"; do
#        for use_text in "${use_texts[@]}"; do
#          for use_image in "${use_images[@]}"; do
#            for text_encoder in "${text_encoders[@]}"; do
#              for type in "${types[@]}"; do
#                if ! [[ "$use_text" == "$use_image" && "$use_text" == "False" ]]; then
#                  # Execute the Python script with the current algorithm and task
#                  python -m code.message_generator graph.algorithm "$algorithm" task.name "$task" task.cot "$cot" task.bag "$bag" task.use_text "$use_text" task.use_image "$use_image" task.text_encoder "$text_encoder" task.type "$type"
#                fi
#              done
#            done
#          done
#        done
#      done
#    done
#  done
#done

python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_existence task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_degree task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name node_count task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name edge_count task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name connected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name cycle_check task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name disconnected_nodes task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name reachability task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name shortest_path task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name maximum_flow task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type zero_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot False task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot True task.bag False task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot True task.bag False task.use_text True task.use_image True

python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder adjacency task.cot True task.bag True task.use_text True task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image False
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text False task.use_image True
python -m code.message_generator graph.algorithm er task.name triangle_counting task.type few_shot task.text_encoder incident task.cot True task.bag True task.use_text True task.use_image True
