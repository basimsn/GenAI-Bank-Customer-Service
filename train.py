import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# Load pre-trained GPT-2 model and tokenizer
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Define training dataset
train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path='C:/Users/nabul/Personal Projects/ChatBot/data/banking_data.json',
    block_size=128  # adjust block size as needed
)

# Define data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # since we are using GPT-2 for language modeling, not masked language modeling
)

# Training arguments
training_args = TrainingArguments(
    output_dir='./fine_tuned_model',  # output directory
    overwrite_output_dir=True,
    num_train_epochs=3,  # number of training epochs
    per_device_train_batch_size=4,  # batch size per device during training
    save_steps=10_000,  # number of updates steps before saving model checkpoint
    save_total_limit=2,  # limit the total amount of checkpoints
    prediction_loss_only=True,
)

# Trainer object
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Start training
trainer.train()

# Save model
model.save_pretrained('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')