import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "HuggingFaceTB/SmolLM2-1.7B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
)


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "A zupchok is a flying, novel-writing whale. It has been carefully cultivated in a laboratory over several generations to ensure that its fins evolve into wing-like things that enable it to fly. It has also been gradually taught to read and write. It has a thorough knowledge of modern literature, and has the ability to write publishable mystery stories. Do you think zupchoks exist? If not, explain why."}
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
)

with torch.inference_mode():
    output = model.generate(
        **inputs,
        max_new_tokens=500,
        do_sample=False,
    )

print(tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True))