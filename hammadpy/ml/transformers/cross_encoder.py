from typing import List, Dict, Tuple, Optional, Union
from sentence_transformers import CrossEncoder

"""
hammadpy/ml/transformers/cross_encoder.py
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the XEncoder class which uses sentence transformers
to score sentence pairs using a CrossEncoder model.

Classes:
    XEncoder: This class uses a SentenceTransformer model to score sentence pairs using a CrossEncoder model.

Methods:
    rank(self, query: str, x: List[str], y: List[str]) -> List[Tuple[int, float]]: Re-ranks pairs formed by two lists of chunks based on their relevance to a single query using the CrossEncoder model.
"""

#==============================================================================#

class XEncoder:
    def __init__(self, model_name: Optional[str] = None, max_length: Optional[int] = None):
        """
        Initializes the XEncoder with a specified model.

        Parameters
        ----------
            model_name : str, optional
                the name of the CrossEncoder model to use (default is "cross-encoder/ms-marco-MiniLM-L-12-v2")
            max_length : int, optional
                the maximum length of the input sequences (default is None)

        Raises
        ------
        ValueError
            If the model name is None
        """
        default_model = "cross-encoder/ms-marco-MiniLM-L-12-v2"  # Default to MS MARCO model
        self.model = CrossEncoder(model_name or default_model, max_length=max_length)

    def rank(self, query: str, x: List[str], y: List[str]) -> List[Tuple[int, float]]:
        """
        Re-ranks pairs formed by two lists of chunks based on their relevance to a single query using the CrossEncoder model.

        Parameters
        ----------
            query : str
                the query to use for re-ranking
            x : List[str]
                the first list of chunks
            y : List[str]
                the second list of chunks

        Returns
        -------
            List[Tuple[int, float]]
        """
        min_length = min(len(x), len(y))
        x = x[:min_length]
        y = y[:min_length]
        pairs = [(query, chunk1 + " " + chunk2) for chunk1, chunk2 in zip(x, y)]
        scores = self.model.predict(pairs)
        index_with_score = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

        return index_with_score
    
#==============================================================================#
