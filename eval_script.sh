lm_eval \
	--model vllm \
	--model_args pretrained=Qwen/Qwen2.5-Math-1.5B-Instruct,tensor_parallel_size=1,dtype=auto,gpu_memory_utilization=0.9,max_model_len=4096 \
	--system_instruction "Please reason step by step, and put your final answer within \\boxed{}." \
	--batch_size auto \
	--apply_chat_template \
	--gen_kwargs top_p=0.8,temperature=0.7,max_gen_toks=4096 \
	--tasks ksat_math_2025_calculus \
	--output_path results \
	--log_samples
