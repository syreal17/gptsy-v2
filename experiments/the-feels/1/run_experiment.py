from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

# Load model and tokenizer
model_name = "EleutherAI/gpt-neo-125M"  # Example; adjust based on the model you have
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Define prompt
prompts = ["Lumere feels", "Nika wonders"]

# Settings for generation
num_samples = 10  # Number of samples per prompt
max_length = 10  # Prompt length + 1 word
temperature = 0.7  # Adjust to control randomness

# Generate one-word completions for each prompt
for prompt in prompts:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    print(f"Prompt: {prompt}")
    for _ in range(num_samples):
        output = model.generate(
            input_ids,
            max_length=max_length,
            do_sample=True,
            temperature=temperature,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        # Extract only the added word
        generated_word = generated_text[len(prompt):].strip().split()[0]
        print(f"Generated word: {generated_word}")
    print()
