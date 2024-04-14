import os, sys, requests, argparse
import torch
import t2v_metrics
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from utils import *
from prompts import *
from llm import *

def get_3d(code_model, reasoning_model, error_iter, refine_iter, code_temp, reasoning_temp, 
           code_api_key, reasoning_api_key, mode, vqa_model, vqa_threshold):
    
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    # Load the Captions and VQA model initially to avoid loading it repeatedly

    processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xxl")
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-xxl", torch_dtype=torch.float16)
    
    vqa = t2v_metrics.VQAScore(model=vqa_model, device=DEVICE)

    if mode == "dataset":
        dataset_queries = get_queries('data/queries.txt')
    else:
        dataset_queries = input("Describe the CAD model that you want to generate:\n")

    macro_store_path = 'results/code'

    # Iterate through all queries
    for idx, query in enumerate(dataset_queries):
        print(f"Starting query number {idx}...")
        # Get direct response
        direct_steps_prompt = get_steps_prompt(query)
        direct_steps = get_answers(reasoning_model, reasoning_api_key, direct_steps_prompt, reasoning_temp)
        direct_code_prompt = get_code_prompt(query, direct_steps)
        direct_code = get_answers(code_model, code_api_key, direct_code_prompt, code_temp)
        direct_code = remove_backticks(direct_code)
        direct_code_macro_file_path = f"{macro_store_path}/query_{idx}_direct_attempt_0.FCMacro"
        write_macro(direct_code, direct_code_macro_file_path)

        # PyAutoGUI sequence
        img_path = f"results/code/query_{idx}_direct_attempt_0.png"
        error_msg = gui_sequence(direct_code_macro_file_path, img_path)

        # Get an executable code
        if error_msg is not None:
            error, success_idx, new_code = get_executable_code(direct_code, error_msg, error_iter, code_model, code_api_key, code_temp, idx, direct_code=True)
            if error is None:
                img_path_for_captions = f"results/code/query_{idx}_direct_attempt_{success_idx}.png"
                code_for_refinement = new_code
            else:
                print("Could not get an executable code for this query... Skipping to next query")
                continue

        else:
            img_path_for_captions = img_path
            code_for_refinement = direct_code

        # VQA score check
        vqa_score = get_vqa_score(img_path_for_captions, query, vqa)

        # Refine if VQA score check is not passed
        if vqa_score < vqa_threshold:
            print("Directly generated code is not correct... Beginning refinement...")
            # Get captions

            caption = get_captions(img_path_for_captions, processor, model)

            # Get the best possible code
            get_refined_outputs(caption, query, code_for_refinement, refine_iter, code_model, code_api_key, code_temp, idx, 
                                error_iter, vqa, vqa_threshold, processor, model)
            
        else:
            print("Stopping criteria is reached with direct model output. No need of refinement...")



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--code_gen_model", type=str, default="codellama", required=True)
    args.add_argument("--reasoning_model", type=str, default="codellama", required=True)
    args.add_argument("--error_iterations", type=int, default=3)
    args.add_argument("--refine_iterations", type=int, default=3)
    args.add_argument("--code_gen_temperature", type=int, default=0.2)
    args.add_argument("--reasoning_temperature", type=int, default=0.8)
    args.add_argument("--code_gen_api_key", type=str, default="fcb5dca384064dce53475051ef6c784761895841b000c09e5611b0344b5466c4")
    args.add_argument("--reasoning_api_key", type=str, default="fcb5dca384064dce53475051ef6c784761895841b000c09e5611b0344b5466c4")
    args.add_argument("--mode", type=str, help="Inferencing on dataset or single inference (dataset or single)", default="dataset")
    args.add_argument("--vqa_model", type=str, default="clip-flant5-xl")
    args.add_argument("--vqa_threshold", type=float, help="Between 0 and 1", default=0.9)

    args = args.parse_args()

    get_3d(args.model, args.error_iterations, args.refine_iterations, args.code_gen_temperature, args.reasoning_temperature, 
           args.code_gen_api_key, args.reasoning_api_key, args.mode, args.vqa_model, args.vqa_threshold)
