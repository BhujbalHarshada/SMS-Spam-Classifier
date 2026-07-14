import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    """
    Preprocess the input text by:
    1. Converting to lowercase
    2. Tokenizing
    3. Removing special characters
    4. Removing stopwords
    5. Applying stemming
    """

    # Convert to lowercase
    text = text.lower()

    # Tokenize
    text = nltk.word_tokenize(text)

    # Keep only alphanumeric words
    words = []

    for word in text:
        if word.isalnum():
            words.append(word)

    # Remove stopwords and punctuation
    filtered_words = []

    for word in words:
        if (
            word not in stopwords.words("english")
            and word not in string.punctuation
        ):
            filtered_words.append(word)

    # Apply stemming
    stemmed_words = []

    for word in filtered_words:
        stemmed_words.append(ps.stem(word))

    return " ".join(stemmed_words)