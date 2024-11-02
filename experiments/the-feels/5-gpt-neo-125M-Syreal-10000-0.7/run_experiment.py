from transformers import GPTNeoForCausalLM, GPT2Tokenizer

# Load model and tokenizer
model_name = "EleutherAI/gpt-neo-125M"  # Example; adjust based on the model you have
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Define prompt
prompts = ["Syreal feels"]

# Settings for generation
num_samples = 10000  # Number of samples per prompt
max_length = 10  # Prompt length + 1 word
temperature = 0.7  # Adjust to control randomness

# Function to generate one-word completions for each prompt and save to file
def generate_and_save_to_file(prompts, filename="generation_output.txt", num_samples=10, max_length=10, temperature=0.7):
    with open(filename, "w") as file:
        for prompt in prompts:
            input_ids = tokenizer(prompt, return_tensors="pt").input_ids
            file.write(f"Prompt: {prompt}\n")
            print(f"Prompt: {prompt}")
            
            for i in range(num_samples):
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
                file.write(f"{generated_word}\n")
                print(f"Generated word {i}: {generated_word}")
            
            file.write("\n")  # Add space between prompts

    print(f"Output saved to {filename}")

# Execute the generation and save to file
generate_and_save_to_file(prompts, "generation_output.txt", num_samples, max_length, temperature)
