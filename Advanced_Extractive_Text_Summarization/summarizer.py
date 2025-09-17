"""
Advanced Extractive Text Summarization Model
Issue #100 for king04aman/All-In-One-Python-Projects
"""
import nltk
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')

def extract_sentences(text):
    return nltk.sent_tokenize(text)

def score_sentences(sentences):
    tfidf = TfidfVectorizer().fit_transform(sentences)
    scores = tfidf.sum(axis=1).A1
    features = []
    for i, sent in enumerate(sentences):
        length = len(sent)
        position = i / len(sentences)
        doc = nlp(sent)
        entities = len(doc.ents)
        features.append([scores[i], length, position, entities])
    return np.array(features)

def cluster_sentences(features, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(features)
    return labels

def summarize(text, n_clusters=3):
    sentences = extract_sentences(text)
    features = score_sentences(sentences)
    labels = cluster_sentences(features, n_clusters)
    summary = []
    for cluster in range(n_clusters):
        idx = np.where(labels == cluster)[0]
        if len(idx) > 0:
            best = idx[np.argmax(features[idx, 0])]
            summary.append(sentences[best])
    return "\n".join(summary)

if __name__ == "__main__":
    sample_text = """
    Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through language. NLP techniques are used to analyze text, extract information, and generate summaries. Extractive summarization selects key sentences from the original text to create a concise summary. Advanced models use features like TF-IDF, sentence length, position, and named entities to score sentences. Clustering helps group related sentences and highlight critical points from different themes. This approach is useful for summarizing reports, research papers, and news articles.
    """
    print("Summary:\n", summarize(sample_text))
