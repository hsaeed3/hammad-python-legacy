from typing import List, Optional, Tuple
from sentence_transformers import SentenceTransformer

"""
hammadpy/ml/transformers/sentence_embedder.py
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the SentenceBERT class which uses sentence transformers
to generate embeddings for a list of sentences.

Classes:
    SentenceBERT: This class uses a SentenceTransformer model to generate embeddings for a list of sentences.

Methods:
    encode(self, sentences: List[str]) -> List[Tuple[str, List[float]]]: Encodes a list of sentences into embeddings.
"""

#==============================================================================#

class SentenceBERT:
    """
    A class for generating sentence embeddings using the SentenceTransformers library.
    
    Attributes
    ----------
    model : SentenceTransformer
        a SentenceTransformer model used to generate sentence embeddings

    Methods
    -------
    encode(sentences: List[str]) -> List[Tuple[str, List[float]]]:
        Encodes a list of sentences into embeddings.
    """

    def __init__(self, model_name: Optional[str] = "all-MiniLM-L6-v2"):
        """
        Initializes the SentenceEmbedder with a specified model.

        Parameters
        ----------
            model_name : str, optional
                the name of the SentenceTransformer model to use (default is "all-MiniLM-L6-v2")
        """
        if not model_name:
            raise ValueError("Model name cannot be None")
        self.model = SentenceTransformer(model_name)

    def encode(self, sentences: List[str]) -> List[Tuple[str, List[float]]]:
        """
        Encodes a list of sentences into embeddings.

        Parameters
        ----------
            sentences : List[str]
                the list of sentences to encode

        Returns
        -------
            List[Tuple[str, List[float]]]
                a list of tuples containing the original sentences and their embeddings
        """
        if not sentences:
            raise ValueError("Sentences list cannot be empty")
        embeddings = self.model.encode(sentences)
        return list(zip(sentences, embeddings))

#==============================================================================#

if __name__ == "__main__":
    embedder = SentenceBERT()
    sentences = [
        "This framework generates embeddings for each input sentence",
        "Sentences are passed as a list of string.",
        "The quick brown fox jumps over the lazy dog."
    ]
    embeddings = embedder.encode_sentences(sentences)
    for sentence, embedding in embeddings:
        print("Sentence:", sentence)
        print("Embedding:", list(embedding))
