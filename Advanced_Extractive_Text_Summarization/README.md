# Advanced Extractive Text Summarization

An advanced extractive text summarization model using NLP techniques.

## Features
- Extracts key sentences from text
- Scores sentences using TF-IDF, sentence length, position, and named entities
- Clusters sentences via K-means to highlight critical points from thematic groups

## Usage
1. Install dependencies:
   ```bash
   pip install nltk spacy scikit-learn
   python -m spacy download en_core_web_sm
   ```
2. Run `summarizer.py`.
3. The script will print a summary of the sample text.

## Requirements
- Python 3.x
- nltk
- spacy
- scikit-learn

## License
MIT
