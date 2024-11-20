#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

#./llm_queryer_zeroshot_baseline_llava.sh
./llm_queryer_zeroshot_gai_llava.sh
./llm_queryer_zerocot_baseline_llava.sh
#./llm_queryer_zerocot_gai_llava.sh
#./llm_queryer_fewshot_baseline_llava.sh
./llm_queryer_fewshot_gai_llava.sh
./llm_queryer_cot_baseline_llava.sh
#./llm_queryer_cot_gai_llava.sh
#./llm_queryer_cotbag_baseline_llava.sh
./llm_queryer_cotbag_gai_llava.sh
