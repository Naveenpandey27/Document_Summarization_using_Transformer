# Install transformers with sentencepiece
!pip install transformers[sentencepiece]

# Open and read the file
file_path = open('/content/econnomy.txt', 'r')
FileContent = file_path.read().strip()

# Import and initialize the tokenizer and model from the checkpoint
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

checkpoint = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

# Extract sentences from the document using NLTK
import nltk
nltk.download('punkt')
sentences = nltk.tokenize.sent_tokenize(FileContent)

# Create chunks of sentences that fit within the model's maximum length
chunks = []
chunk = ""
length = 0
count = -1

# Iterate through sentences to create chunks
for sentence in sentences:
    count += 1
    combined_length = len(tokenizer.tokenize(sentence)) + length
    
    if combined_length <= tokenizer.max_len_single_sentence:
        chunk += sentence + " "
        length = combined_length

        if count == len(sentences) - 1:
            chunks.append(chunk.strip())
    else:
        chunks.append(chunk.strip())
        length = 0
        chunk = ""
        chunk += sentence + " "
        length = len(tokenizer.tokenize(sentence))

# Generate summaries for each chunk using the model
inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

for input in inputs:
    output = model.generate(**input)
    print(tokenizer.decode(*output, skip_special_tokens=True))

