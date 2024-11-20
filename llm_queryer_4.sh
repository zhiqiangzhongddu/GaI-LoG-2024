#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

#./task_generator_4.sh
#./message_generator_4.sh
#chmod +x *_4.sh

#./llm_queryer_zeroshot_baseline_4.sh
#./llm_queryer_zeroshot_gai_4.sh
#./llm_queryer_zerocot_baseline_4.sh
#./llm_queryer_zerocot_gai_4.sh
#./llm_queryer_fewshot_baseline_4.sh
#./llm_queryer_fewshot_gai_4.sh
#./llm_queryer_cot_baseline_4.sh
#./llm_queryer_cot_gai_4.sh
#./llm_queryer_cotbag_baseline_4.sh
#./llm_queryer_cotbag_gai_4.sh

# Number of times you want to run the script
times_to_run=50

## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zeroshot_baseline_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zeroshot_gai_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zerocot_baseline_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_zerocot_gai_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_fewshot_baseline_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done
#
## Loop that runs the script multiple times
#for (( i=1; i<=times_to_run; i++ ))
#do
#    echo "Execution $i"
#    ./llm_queryer_fewshot_gai_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
#done


# Loop that runs the script multiple times
for (( i=1; i<=times_to_run; i++ ))
do
    echo "Execution $i"
    ./llm_queryer_cot_baseline_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
done

# Loop that runs the script multiple times
for (( i=1; i<=times_to_run; i++ ))
do
    echo "Execution $i"
    ./llm_queryer_cot_gai_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
done


# Loop that runs the script multiple times
for (( i=1; i<=times_to_run; i++ ))
do
    echo "Execution $i"
    ./llm_queryer_cotbag_baseline_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
done

# Loop that runs the script multiple times
for (( i=1; i<=times_to_run; i++ ))
do
    echo "Execution $i"
    ./llm_queryer_cotbag_gai_4.sh || { echo "Error occurred, retrying after 10 seconds..."; sleep 10; continue; }
done
