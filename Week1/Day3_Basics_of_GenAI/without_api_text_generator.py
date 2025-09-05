
from transformers import pipeline

# Load a free text generation model from Hugging Face
generator = pipeline("text-generation", model="gpt2")  # You can try other models too

def generate_text(prompt):
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']

# Run your prompt
user_prompt = input("Enter your prompt: ")
output = generate_text(user_prompt)
print("\nGenerated Response:\n", output)
