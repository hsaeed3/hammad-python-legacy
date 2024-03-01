
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== hammadpy ==###################################== Hammad's Python Tools ==##
##== @/experimental/nlp ==######################################################
#==============================================================================#

import nltk
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer

#==============================================================================#

nltk.download('vader_lexicon')

try:
    nlp = spacy.load('en_core_web_sm')
except:
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

#==============================================================================#

class NLPTools:
    """
    Provides convenient utility functions for natural language processing tasks.
    """

    def analyze_sentiment(self, text: str) -> str:
        """
        Analyzes the sentiment of a text string.

        Args:
            text (str): The text to analyze.

        Returns:
            str: Either 'POSITIVE' or 'NEGATIVE' based on sentiment analysis.
        """
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)
        return "POSITIVE" if score['compound'] >= 0.05 else "NEGATIVE" 

    def tokenize(self, text: str) -> list:
        """  
        Tokenizes a text string into a list of words.

        Args:
            text (str): The text to tokenize.

        Returns:
            list: A list of tokens (words).
        """
        doc = nlp(text)
        return [token.text for token in doc]

    def pos_tags(self, text:str) -> list:
        """
        Provides part-of-speech tags for words in a text string.

        Args:
            text (str): The text to analyze.

        Returns:
            list: A list of tuples, where each tuple is (word, part-of-speech tag).
        """
        doc = nlp(text)
        return [(token.text, token.pos_) for token in doc]

    def named_entities(self, text: str) -> list:
        """
        Extracts named entities (people, organizations, locations, etc.) from a text string.

        Args:
            text (str): The text to analyze.

        Returns:
            list: A list of tuples, where each tuple is (named entity, entity type).
        """
        doc = nlp(text)
        return [(entity.text, entity.label_) for entity in doc.ents]
    
    def extract_keywords(self, text: str, pos_filter: list = ['NOUN', 'PROPN', 'ADJ'], top_n: int = 5) -> list:
        """
        Extracts important keywords from text, optionally filtering by parts of speech.

        Args:
            text (str): The text to analyze.
            pos_filter (list, optional):  Parts of speech to keep (e.g., nouns, adjectives). 
                                        Defaults to ['NOUN', 'PROPN', 'ADJ'].
            top_n (int, optional): The maximum number of keywords to return. Defaults to 5.

        Returns:
            list: A list of extracted keywords.
        """
        doc = nlp(text)
        keywords = []
        for token in doc:
            if token.pos_ in pos_filter and not token.is_stop:
                keywords.append(token.text)
        return keywords[:top_n]
    
    def lemmatize(self, text: str) -> list:
        """
        Returns the lemmas (base forms) of words in a text.

        Args:
            text (str): The text to lemmatize.

        Returns:
            list: A list of lemmatized words.
        """
        doc = nlp(text)
        return [token.lemma_ for token in doc]
    
    def clean_text(self, text: str, remove_stopwords: bool = True, stemmer: str = "porter") -> str:
        """
        Performs basic text cleaning, including tokenization, stopword removal, and stemming.

        Args:
            text (str): The text to clean.
            remove_stopwords (bool, optional): Whether to remove common stop words. Defaults to True.
            stemmer (str, optional): Type of stemmer to use ('porter', 'snowball', etc.). Defaults to 'porter'.

        Returns:
            str: The cleaned text.
        """
        # Tokenize
        tokens = nltk.word_tokenize(text)

        # Stop word Removal
        if remove_stopwords:
            stop_words = set(nltk.corpus.stopwords.words('english'))
            tokens = [word for word in tokens if word not in stop_words]

        # Stemming
        stemmer = nltk.stem.PorterStemmer()  # Or select another stemmer
        tokens = [stemmer.stem(word) for word in tokens]

        return ' '.join(tokens)


    