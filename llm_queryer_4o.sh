#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

#./task_generator_4o.sh
#./message_generator_4o.sh
#chmod +x *_4o.sh

#./llm_queryer_zeroshot_baseline_4o.sh
#./llm_queryer_zeroshot_gai_4o.sh
#./llm_queryer_zerocot_baseline_4o.sh
#./llm_queryer_zerocot_gai_4o.sh
#./llm_queryer_fewshot_baseline_4o.sh
#./llm_queryer_fewshot_gai_4o.sh
#./llm_queryer_cot_baseline_4o.sh
#./llm_queryer_cot_gai_4o.sh
#./llm_queryer_cotbag_baseline_4o.sh
#./llm_queryer_cotbag_gai_4o.sh

# Number of times you want to run the script
times_to_run=50

## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zeroshot_baseline_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zeroshot_gai_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zerocot_baseline_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zerocot_gai_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_fewshot_baseline_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_fewshot_gai_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_cot_baseline_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_cot_gai_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done


# Loop that runs the script multiple times
for (( i=1; i<=times_to_run; i++ ))
do
    echo "Execution $i"
    ./llm_queryer_cotbag_baseline_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
done

# Loop that runs the script multiple times
for (( i=1; i<=times_to_run; i++ ))
do
    echo "Execution $i"
    ./llm_queryer_cotbag_gai_4o.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
done
