"""lyrics-generator.py

Generate lyrics for songs.

"""

from datasets import load_dataset
from datasets import load_from_disk

from transformers import AutoTokenizer
from transformers import AutoTokenizer,AutoModelForCausalLM
from transformers import DataCollatorForLanguageModeling
from transformers import AutoModelForCausalLM, TrainingArguments

from trl import SFTTrainer

def def_model(text):
    dataset = load_dataset("text", data_files= "data_song.txt", sample_by="paragraph")
    data = dataset["train"]

    # Chargement du modèle & tokenizer : version distillée de GPT-2
    model = AutoModelForCausalLM.from_pretrained("distilgpt2",
                                                #load_in_4bit=True,
                                                #device_map='auto'
                                                #ignore_mismatched_sizes=True
                                                )
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    tokenizer.pad_token = tokenizer.eos_token

    data_collator= DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir="testt",
        per_device_train_batch_size=4,
        num_train_epochs=7,
        save_steps=100,
        learning_rate=5e-6)

    #Entraînement du modèle avec SFTT pour réduire le temps & le coût de traitement
    trainer = SFTTrainer(
        model=model,
        train_dataset=data,
        dataset_text_field="text",
        max_seq_length=1024,
        tokenizer=tokenizer,
        args=training_args)

    trainer.train()

    # Enregistrement du modèle
    model.save_pretrained("trained-model")
    tokenizer.save_pretrained("trained-model")


    # Génération du texte
    prompt = text
    inputs = tokenizer(prompt, return_tensors="pt").to('cpu')
    generate_ids = model.generate(inputs.input_ids, max_length=300,no_repeat_ngram_size=3 )
    generated_lyrics = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)[0]


    return generated_lyrics
