from sentence_transformers import SentenceTransformer, util
import torch
from typing import List, Tuple

"""
hammadpy/ml/transformers/sentence_similarity.py
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the SentenceSimilarity class which uses sentence transformers
to compute the cosine similarity between two lists of sentences.

Classes:
    SentenceSimilarity: This class uses a SentenceTransformer model to compute the cosine similarity between two lists of sentences.

Methods:
    compute_similarity(self, sentences1: List[str], sentences2: List[str]) -> List[Tuple[str, str, float]]: Computes the cosine similarity between two lists of sentences.
"""

#==============================================================================#

class SentenceSimilarity:
    """
    A class used to compute the cosine similarity between two lists of sentences using a SentenceTransformer model.

    Parameters
    ----------
    model : SentenceTransformer
        a SentenceTransformer model used to compute sentence embeddings

    Methods
    -------
    compute_similarity(sentences1: List[str], sentences2: List[str]) -> List[Tuple[str, str, float]]:
        Computes the cosine similarity between two lists of sentences.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Constructs all the necessary attributes for the SentenceSimilarity object.

        Parameters
        ----------
            model_name : str, optional
                the name of the SentenceTransformer model to use (default is "all-MiniLM-L6-v2")
        """
        self.model = SentenceTransformer(model_name)

    def compute_similarity(self, sentences1: List[str], sentences2: List[str]) -> List[Tuple[str, str, float]]:
        """
        Computes the cosine similarity between two lists of sentences.

        Parameters
        ----------
            sentences1 : List[str]
                the first list of sentences
            sentences2 : List[str]
                the second list of sentences

        Returns
        -------
            List[Tuple[str, str, float]]
                a list of tuples, each containing a pair of sentences and their cosine similarity
        """
        embeddings1 = self.model.encode(sentences1, convert_to_tensor=True)
        embeddings2 = self.model.encode(sentences2, convert_to_tensor=True)
        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        return [(sentences1[i], sentences2[j], cosine_scores[i][j].item()) for i in range(len(sentences1)) for j in range(len(sentences2))]

#==============================================================================#
