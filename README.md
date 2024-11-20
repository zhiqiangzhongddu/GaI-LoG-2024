# Exploring Graph Structure Comprehension Ability of Multimodal Large Language Models: Case Studies

## Instruction to execution

Before everything, you need to create ``openai_env.py`` file to indicate your ``OPENAI_API_KEY="xxx"``. 

1. Generate graphs.
   1. We generated 500 graphs for each of the following algorithms: er, ba, sbm, sfn
   2. We generated 100 graphs for each of the following algorithms: complete, star, path
   3. Generated graphs are located in (``input/generated_graphs``).
2. Generate graph images.
   1. We generate images for the graphs generated in Step-1. 
   2. Generated graph images are located in (``input/generated_graph_images``).
3. Generate task examples.
   1. We generate task examples. 
   2. Generated task examples are located in (``input/generated_examples``).
4. Generate messages. 
   1. We generate messages to query LLMs.
   2. Generated task examples are located in (``input/generated_messages``).
5. Query LLMs.
   1. We query LLMs for response.
   2. Generated responses are located in (``output/generated_responses``).
   3. Generated responses for demo test (cfg.num_sample) are located in (``output/demo_generated_responses``).

Notebook files in ``code/notebook`` are for demo test. 

## Example Execution Code

### Generate Graphs

Example: 
```
./graph_generator.sh # generate graphs following all algorithms
python -m code.graph_generator graph.algorithm er # generate graphs following the er algorithm
```

### Generate Graph Images

Example: 
```
./image_generator.sh # generate graph images following all algorithms
python -m code.image_generator graph.algorithm er # generate graph images following the er algorithm
```

### Generate Task Examples

Example: 
```
./task_generator.sh # generate task examples for grahs generated following all algorithms
python -m code.task_generator graph.algorithm er task.name cycle_check # generate cycle_check task examples for grahs generated following the er algorithm
```

### Generate Messages

Example: 
```
./message_generator.sh # generate messages for tasks of grahs generated following all algorithms
python -m code.message_generator graph.algorithm er task.name cycle_check task.text_encoder adjacency task.cot False task.bag False task.use_text True task.use_image False # generate messages for cycle_check of grahs generated following the er algorithms
```

### Query LLMs

Example:
```
python -m code.llm_queryer llm.name gpt-4o graph.algorithm er task.name cycle_check task.cot False task.bag False task.use_text True task.use_image False demo_test True
```

## Cite

Please cite our paper if it is helpful in your own work:

```bibtex
@article{zhong2024exploring,
  title={Exploring Graph Structure Comprehension Ability of Multimodal Large Language Models: Case Studies},
  author={Zhong, Zhiqiang and Mottin, Davide},
  journal={arXiv preprint arXiv:2409.08864},
  year={2024}
}
```
