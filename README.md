# Document_Summarization_using_Transformer

In this code i used Transformers library to perform text summarization using the `sshleifer/distilbart-cnn-12-6` checkpoint. It automatically generates concise summaries of provided text data.

## Installation

**1.**  Install the required libraries using the following command:
   
   ```
   pip install transformers[sentencepiece]
   ```

**2.** Make sure to have the necessary text file named `econnomy.txt` in the same directory as the script.

**3.** Run the script and follow the instructions.

## Usage

**1.** Run the script in your preferred Python environment.

**2.** The script will read the contents of `econnomy.txt`, tokenize the sentences, and create chunks that fit within the model's maximum length.

**3.** For each chunk, the script will generate a summary using the `sshleifer/distilbart-cnn-12-6` model.

**4.** The summaries will be printed in the console.

## Dependencies

- `transformers`: This library provides pre-trained models for various NLP tasks, including text summarization.
- `nltk`: The Natural Language Toolkit is used for sentence tokenization.

## Notes

- The script is currently designed to work with the specific `sshleifer/distilbart-cnn-12-6` checkpoint. Feel free to modify the code to use other checkpoints as needed.

- Make sure to replace `econnomy.txt` with your desired input text file.

- For more advanced use cases, consider integrating the script into web apps or other interfaces for interactive summarization.

---

Feel free to customize and expand this README according to your needs. This basic template covers the essential information about the script, its purpose, installation steps, and usage instructions.
