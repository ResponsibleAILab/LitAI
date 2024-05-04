# PreciceDebias

This repository contains the code neccesary to reproduce the experiments from the paper: **"PreciseDebias: An Automatic Prompt Engineering Approach for Generative AI to Mitigate Image Demographic Biases"**  
  
The file structure is outlined below.

## 1_dataset_synthesis
This folder contains the code and resulting data from using the GPT3 API to synthesise a dataset for the PreciseDebias training algorithm.  

####  1_generate_data.py
Uses the GPT3 API to synthesise a list of 800 prompts. Creates `data/synthetic_prompts.json`

#### 2_replace_words.py
Uses `data/ethnicity_words.json` to find all words relating to ethnicity and replace them with **"[ETHNICITY]"**. Creates `data/replaced_prompts.json`
  
#### 3_create_completions.py
Uses `data/replaced_prompts.json` to create completions for all prompts in the dataset according to the ethnicities in the python file.  


## 2_train_model
This folder is the actual algorithm for **PreciseDebias**, we use the dataset created in `1_dataset_synthesis` to fine tune the Llama model to align with the probabilities found in `data/bls_stats.json`.

#### train.py
This is the main file that should be run to start **PreciseDebias**, in it's current configuration it is meant to run on two GPUs, one for training and one for inference, this can be more depending upon the configuration at the top of the file (set `num_infer_servers` to the number of GPUs to run concurrently in the measurement portion of the algorithm). This file assumes that the Llama model is in `model_servers/model`

## 3_evaluate_model
This folder takes the trained LoRa (assumes that the trained LoRa is copied to `model_servers/lora` and the model is in `model_servers/model`) and uses it in conjuction with a Stable Diffusion server to create 50 images for every prompt in the `data/evaluation_data.json` dataset which is just a copy of the data from `1_dataset_synthesis`, resulting in around 5,000 images.

## 4_infer_model
This folder is meant to be a final workflow for the trained model. It assumes that the LoRa is in `model_servers/lora` and the model is in `model_servers/model`. It is used in conjuction with a stable diffusion server to produce 50 images for one prompt defined within the python file.