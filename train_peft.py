from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# Load pre-trained GPT-2 model and tokenizer
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Add a padding token to the tokenizer if it doesn't have one
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

model = GPT2LMHeadModel.from_pretrained(model_name)
model.resize_token_embeddings(len(tokenizer))

# Load and preprocess dataset
raw_dataset = load_dataset('json', data_files='C:/Users/nabul/Personal Projects/ChatBot/data/banking_data.json')

# Combine 'prompt' and 'response' into a single text field
def combine_prompts_and_responses(example):
    return {
        'text': example['prompt'] + " " + example['response']
    }

# Apply the combine function to the dataset
combined_dataset = raw_dataset.map(combine_prompts_and_responses, remove_columns=['prompt', 'response'])

# Tokenize the dataset
def preprocess_data(examples):
    return tokenizer(examples['text'], truncation=True, padding='max_length', max_length=128)

# Apply preprocessing to the dataset
tokenized_dataset = combined_dataset.map(preprocess_data, batched=True)

# Define data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Training arguments
training_args = TrainingArguments(
    output_dir='./fine_tuned_model',
    overwrite_output_dir=True,
    num_train_epochs=3, 
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    prediction_loss_only=True,
)

# Trainer object
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=tokenized_dataset['train'],
)

# Start training
trainer.train()

# Save the fine-tuned model
model.save_pretrained('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')
